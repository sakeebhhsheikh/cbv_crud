from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import customer

# Create your views here.
# def register(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         contact = request.POST.get('contact')
#         obj = customer(cust_name=name, cust_contact=contact)
#         obj.save()
    
#     objs = customer.objects.all()
#     return render(request, 'crudapp/register.html', {'data': objs})

# def update(request):
#     if request.method=='POST':
#         obj = customer.objects.get(id=request.POST.get('id'))
#         obj.cust_name = request.POST.get('name')
#         obj.cust_contact = request.POST.get('contact')
#         obj.save()
        
#         return redirect('/')
#     if not request.GET.get('id') :
#         return redirect('/') 
#     obj = customer.objects.get(id=request.GET.get('id'))
#     return render(request, 'crudapp/update.html', {'obj': obj})

# def delete(request):
#     if request.GET.get('id'):
#         obj = customer.objects.get(id=request.GET.get('id'))
#         obj.delete()
#     return redirect('/')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Register(CreateView):
    model = customer
    fields = '__all__'
    # form_class = CustomerFrom #(Optional)
    template_name = 'crudapp/register.html'
    success_url = '/'

    # queryset = customer.objects.all()
    # context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = customer.objects.all() 
        return context
    
class Update(UpdateView):
    model = customer
    fields = '__all__'
    template_name = 'crudapp/update.html'
    success_url = '/'

class Delete(DeleteView):
    model = customer
    template_name = 'crudapp/delete.html'
    success_url = reverse_lazy("Register")