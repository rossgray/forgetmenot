from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import PersonForm
from .models import Person


def index(request):
    return HttpResponse("Hello, world. You're at the occasions index.")


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person