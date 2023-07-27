from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TSwift

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
    return render(request, 'tswifts/detail.html', {'tswift':tswift})

class TSwiftCreate(CreateView):
    model = TSwift
    fields = '__all__'

class TSwiftUpdate(UpdateView):
    model = TSwift
    fields = ['songs', 'taylors_version']

class TSwiftDelete(DeleteView):
    model = TSwift
    success_url = '/tswifts'


# taylors = [
#     {'name': 'Debut Taylor', 'year': 2006, 'songs': ['Teardrops on My Guitar', 'Tim McGraw', 'Our Song']},
#     {'name': 'Fearless Taylor', 'year': 2008, 'songs': ['Love Story', 'You Belong With Me']},
#     {'name': 'Speak Now Taylor', 'year': 2010, 'songs': ['Mean', 'Dear John', 'Enchanted', 'Back to December']},
#     {'name': 'Red Taylor', 'year': 2012, 'songs': ['All Too Well', '22', 'I Knew You Were Trouble']},
#     {'name': '1989 Taylor', 'year': 2014, 'songs': ['Blank Space', 'Bad Blood', 'Style', 'Wildest Dreams']},
#     {'name': 'Reputation Taylor', 'year': 2017, 'songs': ['Delicate', 'Getaway Car', 'Gorgeous', '...Ready For It']},
#     {'name': 'Lover Taylor', 'year': 2019, 'songs': ['Cruel Summer', 'Lover', 'Miss Americana & the Heartbreak Prince', 'London Boy']},
#     {'name': 'Midnights Taylor', 'year': 2022, 'songs': ['Karma', 'Anti-Hero', 'Paris', 'Maroon']},
# ]