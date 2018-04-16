from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import User, Idea, Comment

class IndexView(generic.ListView):
    model = Idea
    template_name = 'ideas/index.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return "hi"