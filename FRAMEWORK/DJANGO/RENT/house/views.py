from django.shortcuts import render, redirect
from .models import *
import uuid
# Create your views here.


def cites(request):
    cites = Cite.objects.all()
    context = {
        'cites' : cites
    }
    return render(request, 'house/cites.html', context)

def singlecite(request, pk):
    singlecite = Cite.objects.get(cite_id=pk)
    if singlecite.cite_type == 'Apartment':
        moredetail = singlecite.apartment
    elif singlecite.cite_type == 'Studio':
        moredetail = singlecite.studio
    elif singlecite.cite_type == 'Room':
        moredetail = singlecite.room
    else:
        moredetail = singlecite
    context = {
        "singlecite" : singlecite,
        "moredetail" : moredetail
    }
    return render(request, 'house/singlecite.html', context)

def addcite(request):
    if request.method == 'POST':
        citename=request.POST.get('citename')
        address=request.POST.get('address')
        council=request.POST.get('council')
        price=request.POST.get('price')
        numberslot=request.POST.get('numberslot')
        town=request.POST.get('town')
        region=request.POST.get('region')
        citeimage=request.POST.get('citeimage')
        
        # lpk = uuid('57ffe523-7af4-4356-8d4d-dcc883a4ad97')
        owner = Landlord.objects.first()
        newcite = Cite.objects.create(
            cite_name=citename, 
            address=address,
            council=council,
            price=price,
            number_slot=numberslot,
            owner=owner,
            town=town,
            region=region,
            cite_image=citeimage
        )
        newcite.save()
        pk = newcite.cite_id
        return redirect('selecttype', str(pk) )
    return render(request, 'house/addcite.html')

def selecttype(request, pk):
    return render(request, 'house/selecttype.html', pk)

def apartment(request, pk):
    if request.method == 'POST':
        nameofroom = request.POST.get('nameofroom')
        nameofbathroom = request.POST.get('nameofbathroom')
        dimension = request.POST.get('dimension')
        wardrobe = request.POST.get('wardrobe')
        aircondition = request.POST.get('aircondition')
        light = request.POST.get('light')
        water = request.POST.get('water')
        
        singlecite = Cite.objects.get(cite_id=pk)
        newapartment = singlecite.apartment.objects.create(
            name_of_room = nameofroom,
            name_of_bathroom = nameofbathroom,
            dimension = dimension,
            wardrobe = wardrobe,
            air_condition = aircondition,
            light = light,
            water = water,
            
        )
        newapartment.save()
        return redirect('cites')
    return render(request, 'house/apartment.html', pk)

def studio(request, pk):
    if request.method == 'POST':
        dimension = request.POST.get('dimension')
        wardrobe = request.POST.get('wardrobe')
        aircondition = request.POST.get('aircondition')
        light = request.POST.get('light')
        water = request.POST.get('water')
        
        singlecite = Cite.objects.get(cite_id=pk)
        newstudio = singlecite.studio.objects.create(
            dimension = dimension,
            wardrobe = wardrobe,
            air_condition = aircondition,
            light = light,
            water = water,
            
        )
        newstudio.save()
        return redirect('cites')
    return render(request, 'house/studio.html' )

def room(request, pk):
    if request.method == 'POST':
        kitchen = request.POST.get('kitchen')
        dimension = request.POST.get('dimension')
        wardrobe = request.POST.get('wardrobe')
        toilet = request.POST.get('toilet')
        light = request.POST.get('light')
        water = request.POST.get('water')
        
        singlecite = Cite.objects.get(cite_id=pk)
        newroom = singlecite.room.objects.create(
            kitchen = kitchen,
            dimension = dimension,
            wardrobe = wardrobe,
            toilet = toilet,
            light = light,
            water = water,
            
        )
        newroom.save()
        return redirect('cites')
    return render(request, 'house/room.html' )

def updatecite(request, pk):
    return render(request, 'house/updatecite.html')

def deletecite(request, pk):
    return render(request, 'house/deletecite.html')