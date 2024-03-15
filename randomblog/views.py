from django.shortcuts import render, redirect
from .random_blog import random_url_get
import random, webbrowser

# Create your views here.

def indexfunc(request):
    return render(request, 'index.html', {})

def randombtnfunc(request):
    topiclist = []
    article_list = []
    site_selector = random.randint(0,2)
    if site_selector == 0:
        random_url_get('https://hatenablog.com/topics/journal', '.topic-nav-item-link', topiclist)
        print(topiclist)
        random_url_get(random.choice(topiclist), '.entry-link', article_list)
        print(article_list)
    elif site_selector == 1:
        random_url_get('https://ameblo.jp', '.spui-LinkButton--neutral', topiclist)
        print(topiclist)
        random_url_get(random.choice(topiclist), '.RankingItem_Link__1CxHV', article_list)
        print(article_list)
    else:
        random_url_get('https://blog.fc2.com/ranking/', '.gtm-L-genre_list', topiclist)
        topiclist2 =  ['https://blog.fc2.com/' + al for al in topiclist]
        removedtopic = topiclist2.pop()
        print(topiclist2)
        random_url_get(random.choice(topiclist2), '.gtm-entry_link', article_list)
        print(article_list)


    randomurl = random.choice(article_list)
    print(randomurl)
    return render(request, 'randombtn.html', {'randomurl':randomurl})
    # return redirect(randomurl)