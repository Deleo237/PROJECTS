from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact="")
    lowskills = profile.skill_set.filter(description="")
    context={'profile': profile, 'topskills': topskills, 'lowskills': lowskills}
    return render(request, 'users/user-profile.html', context)