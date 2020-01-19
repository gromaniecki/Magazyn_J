from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Produkty,Kategoria
from .forms import *
from koszyk.models import Cart

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.



def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        kats = Kategoria.objects.all()
        produkty = Produkty.objects.filter(nazwa__icontains=q)
        produkty |= Produkty.objects.filter(opis__icontains=q)
        produkty |= Produkty.objects.filter(numer__icontains=q)
        context = {'query' : q,
                   'produkty' : produkty,
                   'kats'   : kats,}
        template = 'produkty/result.html'
    else:
        context = {}
        template = 'produkty/index.html'

    return render(request,template,context)


def detail(request, produkt_id,):
   # cart = get_object_or_404(Cart, id=cart_id)
    produkt = Produkty.objects.get(pk=produkt_id)
    kats = Kategoria.objects.all()
    context = {'produkt': produkt, 'kats': kats, }
    return render(request, 'produkty/detail_block.html', context )

def detail_m(request, produkt_id, c_id):
    produkt = Produkty.objects.get(pk=produkt_id)
    kats = Kategoria.objects.all()
    context = {'produkt': produkt, 'kats': kats, 'c_id':c_id,}
    return render(request, 'produkty/detail_m.html', context )

def index(request):
    prod_list = Produkty.objects.all()
    kats = Kategoria.objects.all()
    template = loader.get_template('produkty/index.html')
    context = {
        'prod_list': prod_list,
        'kats': kats,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)

        else:
            pass
            #messages.error(request,"Dupa")
    return render(request,'produkty/login.html')

def logout_view(request):
    logout(request)

def kategorie(request, cart_id):
    kats = Kategoria.objects.all()
    #cart = Cart.objects.get(pk=cart_id)
    c_id = cart_id
    template = 'produkty/kategorie.html'
    context = {
        'kats': kats, 'c_id': c_id,
    }
    return render(request, template , context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse(kats)

def kategoria(request,id):
    kategoria_widok = Produkty.objects.filter(kategoria=id)
    kat = Kategoria.objects.get(pk=id)
    kats = Kategoria.objects.all()
    form1 = Zamowienie()
    context = {
        'kategoria_widok'   : kategoria_widok,
        'kat'               : kat,
        'kats'              : kats,
        'form1'             : form1,  }
    return render(request, 'produkty/katf kopia.html', context)

def kat_m(request,id, c_id):
    kategoria_widok = Produkty.objects.filter(kategoria=id)
    kat = Kategoria.objects.get(pk=id)
    kats = Kategoria.objects.all()
    #cart = Cart.objects.get(pk=c_id)
    #c_id = cart.id
    form1 = Zamowienie()
    context = {
        'kategoria_widok'   : kategoria_widok,
        'kat'               : kat,
        'kats'              : kats,
        'form1'             : form1,
        'c_id'              : c_id,  }
    return render(request, 'produkty/kat_m.html', context)

def zamowienie(request):
    form = Zamowienie()
    prod_list = Produkty.objects.all()
    context = {
        "form" : form,
        'prod_list': prod_list,
    }
    return render(request,'produkty/zamow.html',context)

def choice(request):
    return render(request,'registration/choice.html')

def przyjmij(request):
    form_p = Przyjmij(request.POST or None)
    if form_p.is_valid():
        form_p.save()
        print('dodano produkt')
        return redirect("przyjmij")
    context = {'form_p':form_p}
    return render(request, 'produkty/add_towar.html', context)
