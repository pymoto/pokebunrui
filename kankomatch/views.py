from django.shortcuts import render
from django.conf import settings
from .placesAPI import placesAPImasterfunc
from .openAIAPI import explain_about_place_func, keyword_extract_func

# Create your views here.
def indexfunc(request):
    template_name = 'index.html'
    return render(request, template_name, {})

def kankomatchfunc(request):
    context = {}
    template_name = 'kankomatch.html'
    for i in range(3):
        result = placesAPImasterfunc(settings.GOOGLE_API_KEY)
        if result != None:
            place_id, place_name, review_text, photo_urls, formatted_address = result
            place_explain = explain_about_place_func(place_name)
            keywords = keyword_extract_func(review_text)
            context.update([('place_id{}'.format(i), place_id), ("place_name{}".format(i), place_name),  ("place_explain{}".format(i), place_explain), ('keywords{}'.format(i), keywords), ('photo_urls{}'.format(i), photo_urls), ('formatted_address{}'.format(i), formatted_address)])

    return render(request, template_name, context)
