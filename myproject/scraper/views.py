from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import os

def scrape(request):
    if request.method == 'POST':
        url = request.POST['url']
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a')
        return render(request, 'scraper/result.html', {'links': links, 'url': url})
    else:
        return render(request, 'scraper/home.html')