from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models, forms
from .forms import InvForm
from django.views import generic
from django.views import generic
from . import models
from django.shortcuts import get_object_or_404, redirect, render

class EditInvView(generic.UpdateView):
    template_name = "catalog/edit_inv.html"
    form_class = forms.InvForm
    success_url = "/catalog/"

    def get_object(self, **kwargs):
        inv_id = self.kwargs.get("id")
        return get_object_or_404(models.Inventory, id=inv_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditInvView, self).form_valid(form=form)



class DeleteInvView(generic.DeleteView):
    template_name = "catalog/confirm_delete.html"
    success_url = "/catalog/"

    def get_object(self, **kwargs):
        inv_id = self.kwargs.get("id")
        return get_object_or_404(models.Inventory, id=inv_id)


class CreateInvView(generic.CreateView):
    template_name = "catalog/create_inv.html"
    form_class = forms.InvForm
    success_url = "/catalog/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateInvView, self).form_valid(form=form)



class InvDetailView(generic.DetailView):
    template_name = "catalog/invs_detail.html"
    context_object_name = "inv_id"

    def get_object(self, **kwargs):
        inv_id = self.kwargs.get("id")
        return get_object_or_404(models.Inventory, id=inv_id)

class InvListView(generic.ListView):
    template_name = "catalog/invs_list.html"
    context_object_name = "inv"
    model = models.Inventory
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Comment(generic.DetailView):
    template_name = "catalog/details.html"
    context_object_name = "comment"
    model = models.ReviewInv
    ordering = ["-id"]

    def get_object(self):
        inv_id = self.kwargs.get("id")
        return get_object_or_404(models.Inventory, id=inv_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = InvForm()
        context['form'] = form
        return context

    def post(self, request, id):
        inventory = get_object_or_404(models.Inventory, id=id)
        form = InvForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.inventory = inventory
            review.save()
            return redirect('comment-detail', id=inventory.id)
        return render(request, 'catalog/details.html', {'form': form, 'inventory': inventory})

