from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings

import json, os

# Create your views here.
f = open(os.path.join(settings.BASE_DIR, 'blog\\static\\blog\\attachments\\blogs.json'))
jsonData = json.load(f)
f.close()
sorted_data = sorted(jsonData, key=lambda i : i['date'], reverse=True)

# print(len(jsonData))
# print(jsonData)

def index(request):
    # print(jsonData)
    return render(request, 'blog/index.html',{"posts" : list(sorted_data[:3])})

def posts(request):
    return render(request, 'blog/all_posts.html',{"posts" : list(sorted_data)})

def post(request, slug):
    data = [post for post in jsonData if post['slug'] == slug ]
    return render(request, 'blog/post_details.html',{"post" : data[0]})