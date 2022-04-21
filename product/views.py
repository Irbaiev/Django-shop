from django.views.generic import *
from django.shortcuts import get_object_or_404, render

from .models import Product, Grade
from .forms import CommentForm

class Homeviews(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class Addproduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'
    context_object_name = 'add_product'
    success_url = '/add-product'

def Product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    grade = Grade.objects.filter(products=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.products = product
            form.save()
    else:
        form = CommentForm()
    return render(request, 'product-detail.html', {'product':product, 'grade':grade, 'form':form})



class Update_product(UpdateView):
    model = Product
    template_name = 'update.html'
    fields = '__all__'
    success_url = '/'

class Delete_product(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = '/'



