from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Index
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# для создания пользователя
from django.views.generic.edit import CreateView

from .forms import UpdateItemForm
from .models import Mebel


def show_all(request):
    mebels = Mebel.objects.all().order_by("-price")
    return render(
        request,
        'app_1/show_all.html',
        {'mebels': mebels}
    )


def show_all_admin(request):
    form = UpdateItemForm()
    mebels = Mebel.objects.all().order_by("-price")
    return render(
        request,
        'app_1/show_admin_item.html',
        {
            'form': form,
            'mebels': mebels
        }
    )


def show_item(request, item_id):
    item = Mebel.objects.get(pk=item_id)
    return render(
        request,
        'app_1/show_item.html',
        {'item': item}
    )


def update_item(request, item_id):
    if request.method == 'POST':
        new_description = dict(request.POST).get('description', '')
        new_price = dict(request.POST).get('price', '')
        Mebel.objects.filter(pk=item_id).update(
            price=new_price[0],
            description=new_description[0]
        )

    return redirect('items_admin')


def delete_item(request, item_id):
    Mebel.objects.filter(pk=item_id).delete()
    return redirect('items_admin')


def main(request):
    return redirect('main')


def page_not_found(request, *args, **argv):
    return redirect('main')

def login(request):
    return render(request, 'app_1/login.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def list_index(request):
    index = Index.objects.all()
    paginator = Paginator(index,15)
    title = 'index'
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, 'index.html', context={'title':title, 'page_obj':page_obj} )
