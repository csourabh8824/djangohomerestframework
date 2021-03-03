from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse

from .forms import ProductForm




class ProductView(View):
    form_class = ProductForm
    template_name = 'product_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product-add'))

        return render(request, self.template_name, {'form': form})