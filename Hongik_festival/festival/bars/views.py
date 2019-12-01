from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bar, BarLike


def bar_list(request):
    bars = Bar.objects.all()
    return render(request, 'bar_list.html', {'bars':bars})

@login_required
def bar_detail(request, bar_id):
    bar = get_object_or_404(Bar, id=bar_id)
    return render(request, 'detail.html', {'bar' : bar})

@login_required
def bar_like(request, bar_id):
    user = request.user
    bar = get_object_or_404(Bar, id=bar_id)
    try:
        preexisiting_like = BarLike.objects.get(creator=user, bar=bar)
        preexisiting_like.delete()
        return redirect('/bars/')
    except BarLike.DoesNotExist:
        bar_like = BarLike()
        bar_like.bar = bar
        bar_like.creator = user
        bar_like.save()
        return redirect('/bars/')
    return redirect('/bars/')
