from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tareas
from .forms import TareaForm

# Create your views here.

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class ListaTareas(ListView):
    template_name = 'tareas/tareas_list.html'

    def get_queryset(self):
        palabra = self.request.GET.get('kword', '')
        buscar = (Q(name__icontains=palabra) | Q(description__icontains=palabra))
        lista = Tareas.objects.filter(buscar)
        return lista

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TareaCreate(CreateView):
    form_class = TareaForm
    template_name = 'tareas/tareas_create_form.html'
    success_url = reverse_lazy('lista-tareas')

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TareaUpdate(UpdateView):
    model = Tareas
    form_class = TareaForm
    template_name = 'tareas/tareas_update_form.html'
    success_url = reverse_lazy('lista-tareas')

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TareaDelete(DeleteView):
    model = Tareas
    success_url = reverse_lazy('lista-tareas')