from django.shortcuts import render
import csv, random, os, requests

# Create your views here.

# Django プロジェクトのベースディレクトリを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV ファイルへのパスを指定
CSV_FILE_PATH = os.path.join(BASE_DIR, 'pokebunrui.csv')

# def homefunc(request):
#     return request

def pokebunruifunc(request):
    template_name = 'pokebunrui.html'
    with open ('pokebunrui.csv', 'r') as pb:
        reader = csv.reader(pb)
        l = [row for row in reader]
        choiced = random.choice(l)
        bunrui = choiced[2]
        poke_name = choiced[1]
    
    num = choiced[0]
    s = num.zfill(4)
    poke_url = 'https://zukan.pokemon.co.jp/detail/' + s

    api_url = "https://pokeapi.co/api/v2/pokemon/" + num

    r = requests.get(api_url, timeout=5)
    r = r.json()

    # poke_id    = r['id']
    # poke_name  = r['name']
    poke_image = r['sprites']['front_default']
    poke_types = r['types'][0]['type']['name']

    poke_type_jp = None
    with open ('poke_type.csv', 'r') as pt:
        ptreader = csv.reader(pt)
        type_transrate = [row for row in ptreader]
        for i in range(len(type_transrate)):
            if type_transrate[i][1] == poke_types:
                poke_type_jp = type_transrate[i][0]



        # while True:
        #     if input(choiced[2]) == choiced[1]:
        #         print('〇')
        #         break
        #     else:
        #         print('✕')
    context = {'bunrui':bunrui, 'poke_name':poke_name, 'poke_url':poke_url, \
               'poke_image':poke_image, 'poke_type_jp':poke_type_jp}
    return render(request, template_name, context)
