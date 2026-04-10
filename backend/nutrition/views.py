from django.shortcuts import get_object_or_404, render

from .models import DietPlan


def plan_list(request):
    return render(request, "nutrition/list.html", {"plans": DietPlan.objects.all()})


def plan_detail(request, pk):
    plan = get_object_or_404(DietPlan, pk=pk)
    return render(request, "nutrition/detail.html", {"plan": plan})
