from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hiker, Gear

class HikerCreate(CreateView):
  model = Hiker
  fields = ['name']

class HikerUpdate(UpdateView):
  model = Hiker
  fields = ['name']

class HikerDelete(DeleteView):
  model = Hiker
  success_url = '/hikers/'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def hikers_index(request):
  hikers = Hiker.objects.all()
  return render(request, 'hikers/index.html', { 'hikers': hikers })

def hikers_detail(request, hiker_id):
  hiker = Hiker.objects.get(id=hiker_id)
  gears_hiker_doesnt_have = Gear.objects.exclude(id__in = hiker.gears.all().values_list('id'))
  return render(request, 'hikers/detail.html', {
    'hiker': hiker,
    'gears': gears_hiker_doesnt_have
})

def assoc_gear(request, hiker_id, gear_id):
  Hiker.objects.get(id=hiker_id).gears.add(gear_id)
  return redirect('detail', hiker_id=hiker_id)