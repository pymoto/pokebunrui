import openai
from django.conf import settings

def explain_about_place_func(place_name):
    if place_name:

        client = openai.OpenAI(api_key = settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
                model="gpt-4-0125-preview",
                messages=[
                {"role": "system", "content": "この場所について50文字程度で説明してください。場所についての情報がない場合は「情報なし」とだけ答えてください。"},
                {"role": "user", "content": place_name},
            ],
        )
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()
    else:
        return None

def keyword_extract_func(text_for_gpt):
    client = openai.OpenAI(api_key = settings.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "次の文章からキーワードをコンマ区切りで10個抽出してください。文章が存在しなければ「口コミは存在しません」と返してください。"},
            {"role": "user", "content": text_for_gpt},
        ],
    )

    return response.choices[0].message.content.strip()