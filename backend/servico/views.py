from django.shortcuts import render
from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)


from .forms import OrdemServicoForm, ServicoForm
from .models import OrdemServico, Servico


def ordem_servico_list(request):
    template_name = 'servico/ordem_servico_list.html'
    object_list = OrdemServico.objects.all()

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(situacao=search)

    context = {'object_list': object_list}
    return render(request, template_name, context)


def ordem_servico_create(request):
    template_name = 'servico/ordem_servico_form.html'
    context = {'form': OrdemServicoForm}
    return render(request, template_name, context)


def ordem_servico_detail(request, pk):
    template_name = 'servico/ordem_servico_detail.html'
    instance = OrdemServico.objects.get(pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def ordem_servico_update(request, pk):
    ...


def ordem_servico_delete(request, pk):
    ...


class ServicoListView(ListView):
    model = Servico
    paginate_by = 20

    def get_queryset(self):
        qs = self.model.objects.all()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(Q(titulo__icontains=search))
        return qs


class ServicoDetailView(DetailView):
    model = Servico


class ServicoCreateView(CreateView):
    model = Servico
    form_class = ServicoForm


class ServicoUpdateView(UpdateView):
    model = Servico
    form_class = ServicoForm


# class ServicoDeleteView(DeleteView):
#     model = Servico
#     success_url = reverse_lazy('servico:servico_list')
