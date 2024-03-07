from django.shortcuts import render
import csv, random, os

# Create your views here.

# Django プロジェクトのベースディレクトリを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CSV ファイルへのパスを指定
CSV_FILE_PATH = os.path.join(BASE_DIR, 'pokebunrui.csv')

# def homefunc(request):
#     return request

def pokebunruifunc(request):
    template_name = 'pokebunrui.html'
    with open (CSV_FILE_PATH, 'r') as pb:
        reader = csv.reader(pb)
        l = [row for row in reader]
        choiced = random.choice(l)
        bunrui = choiced[2]
        poke_name = choiced[1]

        # while True:
        #     if input(choiced[2]) == choiced[1]:
        #         print('〇')
        #         break
        #     else:
        #         print('✕')
    context = {'bunrui':bunrui, 'poke_name':poke_name}
    return render(request, template_name, context)
