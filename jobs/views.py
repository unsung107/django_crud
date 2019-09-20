from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
import requests
from pprint import pprint

# Create your views here.
fake = Faker('ko_KR')
def past_job(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        temp = Job.objects.filter(name=name)
        if not temp :
            job = Job()
            job.name = name
            job.past_job = fake.job()
            job.save()
        
        else:
            job = get_object_or_404(Job, name=name)
        job_name = job.past_job.split()[-1]
        url = f'https://api.giphy.com/v1/gifs/search?api_key=KL6K2v0CUvZrECUq4d9dIJnSBuZgtRgf&q={job_name}&limit=1'
        data = requests.get(url).json()
        if data['data']:
            image = data['data'][0]['images']['downsized_medium']['url']
        else:
            image = 'https://pbs.twimg.com/profile_images/770139154898382848/ndFg-IDH_400x400.jpg'

        context = {
                'name':job.name,
                'job':job.past_job,
                'image':image
            }
        return render(request, 'jobs/past_job.html', context)
    else:
        redirect('jobs:index')


        

def index(request):
    return render(request, 'jobs/index.html')

