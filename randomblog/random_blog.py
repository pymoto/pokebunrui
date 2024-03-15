import requests, bs4, random, webbrowser

def random_url_get(page_link, class_info, use_list):
    res = requests.get(page_link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select(class_info)
    for elem in elems:
        use_list.append('{}'.format(elem.get('href')))