from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import TSwift, Award
from .forms import DatingHistoryForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tswifts_index(request):
    tswifts = TSwift.objects.all()
    return render(request, 'tswifts/index.html', {'tswifts': tswifts})

def tswifts_detail(request, tswift_id):
    tswift = TSwift.objects.get(id=tswift_id)
    id_list = tswift.awards.all().values_list('id')
    awards_tswift_doesnt_have = Award.objects.exclude(id__in=id_list)
    datinghistory_form = DatingHistoryForm()
    return render(request, 'tswifts/detail.html', {'tswift':tswift, 
        'datinghistory_form': datinghistory_form, 'awards': awards_tswift_doesnt_have})

def add_datinghistory(request, tswift_id):
    form = DatingHistoryForm(request.POST)
    if form.is_valid():
        new_datinghistory = form.save(commit=False)
        new_datinghistory.tswift_id = tswift_id
        new_datinghistory.save()
    return redirect('detail', tswift_id=tswift_id)

class TSwiftCreate(CreateView):
    model = TSwift
    fields = ['name', 'year', 'songs', 'taylors_version']

class TSwiftUpdate(UpdateView):
    model = TSwift
    fields = ['songs', 'taylors_version']

class TSwiftDelete(DeleteView):
    model = TSwift
    success_url = '/tswifts'

class AwardList(ListView):
    model = Award

class AwardDetail(DetailView):
    model = Award

class AwardCreate(CreateView):
    model = Award
    fields = '__all__'
    
class AwardUpdate(UpdateView):
    model = Award
    fields = ['category', 'result']

class AwardDelete(DeleteView):
    model = Award
    success_url = '/awards'
    
def assoc_award(request, tswift_id, award_id):
    TSwift.objects.get(id=tswift_id).awards.add(award_id)
    return redirect('detail', tswift_id=tswift_id)

def unassoc_award(request, tswift_id, award_id):
    TSwift.objects.get(id=tswift_id).awards.remove(award_id)
    return redirect('detail', tswift_id=tswift_id)