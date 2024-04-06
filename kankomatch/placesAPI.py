# -*- coding: utf-8 -*-


import requests

import random

import unicodedata

def generate_random_location():
    # 日本の緯度経度範囲
    # min_lat, max_lat = 24.396308, 45.551483
    # min_lng, max_lng = 122.93457, 153.986672

    min_lat, max_lat = 34.858363, 43.265009
    min_lng, max_lng = 138.02124, 141.690673
    # ランダムな緯度経度を生成
    lat = random.uniform(min_lat, max_lat)
    lng = random.uniform(min_lng, max_lng)
    return lat, lng

def get_nearby_place_id(api_key, location, radius=10000, keyword=None):
        endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            "key": api_key,
            "location": f"{location[0]},{location[1]}",
            "radius": radius,
            'type': 'tourist_attraction',  # 観光地のみを検索
            'language': 'ja'
        }
        if keyword:
            params["keyword"] = keyword
        response = requests.get(endpoint, params=params)
        data = response.json()
        if data["status"] == "OK" and data.get("results"):
            place_id = data["results"][0]["place_id"]
            place_name = data["results"][0]["name"]
            return place_id, place_name
        else:
            print("Error:", data["status"])
            print('retry')
            return None
    
def get_place_details(api_key, place_id):
    endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "key": api_key,
        "place_id": place_id,
        "fields": "reviews,photos,formatted_address",
        "language": "ja"
    }
    response = requests.get(endpoint, params=params)
    response.encoding = response.apparent_encoding
    data = response.json()
    if data["status"] == "OK":
        return data["result"]
    else:
        print("Error:", data["status"])
        return None
    
def remove_emoji(text):

    # 絵文字、空白、改行を除去して一行の文章に変換
    text_no_emoji = ''.join(char for char in text if unicodedata.category(char) != 'So')
    text_one_line = ''.join(text_no_emoji.split())

    print(text_one_line)
    return text_one_line

def get_photo(photo_reference, api_key, max_width=400):
    endpoint = "https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "key": api_key,
        "photoreference": photo_reference,
        "maxwidth": max_width
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.content
    else:
        return None

def placesAPImasterfunc(api_key):
    while True:
        # ランダムな座標を生成
        location = generate_random_location()
        print("Random Location:", location)
        # 近くの施設の Place ID を取得
        if get_nearby_place_id(api_key, location):
            place_id, place_name = get_nearby_place_id(api_key, location)
            print("Nearby Place ID:", place_id)
            print("Place Name:", place_name)
            place_details = get_place_details(api_key, place_id)
            if place_details:
                # レビューを表示
                if "photos" in place_details:
                    photo_urls = []
                    for i in range(min(5, len(place_details["photos"]))):
                        if place_details["photos"][i]["photo_reference"]:
                            photo_reference = place_details["photos"][i]["photo_reference"]
                            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?key={api_key}&photoreference={photo_reference}&maxwidth=400"
                            photo_urls.append(photo_url)
                else:
                    photo_urls = None

                if "formatted_address" in place_details:
                    formatted_address = place_details["formatted_address"]
                else:
                    formatted_address = None

                if "reviews" in place_details:
                    whole_review = ""
                    for review in place_details["reviews"]:
                        # print("Author:", review.get("author_name", "Unknown"))
                        # print("Rating:", review.get("rating", "No rating"))
                        review_text = review.get("text", "No text")
                        # print("Text:", review_text)
                        # print("Text:", review_text)

                        # print()
                        whole_review += review_text
                    # print(whole_review)
                    treated_review_text = remove_emoji(whole_review)
                    return place_id, place_name, treated_review_text, photo_urls, formatted_address
                else:
                    print("No reviews found")
                    treated_review_text = None
                    return place_id, place_name, treated_review_text, photo_urls, formatted_address
        else:
            print("Nearby Place ID:", "No Data")
            print("Place Name:", "No Data")
            print('retry')