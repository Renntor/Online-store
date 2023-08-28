from django.shortcuts import render
from django.core import management

from catalog.forms import ProductForm, VersionForm
from catalog.models import Contact, Product, Version
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory


# Create your views here.


class ContactListView(ListView):
    """
    Контролер для вывода контактов
    """
    model = Contact
    template_name = 'catalog/contact.html'


class ProductDetailView(DetailView):
    """
    Контролер для детальной информации продуктов
    """
    model = Product
    context_object_name = 'article'


class ProductListView(ListView):
    """
    Контролер для показа продуктов
    """
    model = Product
    template_name = 'catalog/home.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     version = Version.objects.filter(current_version=True)[0]
    #     context['version'] = version.number_version
    #     return context


class ProductCreateView(CreateView):
    """
    Контролер для добавления продуктов
    """
    model = Product
    form_class = ProductForm, VersionForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context['formset'] = formset
        return context

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()


        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
