import requests
import json
from bs4 import BeautifulSoup
import csv

links = #Put links to search here

mycsv = csv.writer(open('OUTPUTCSV.csv', 'wb'))

for link in links:
    req = requests.get(link).text
    soup = BeautifulSoup(req, "html.parser")
    scripts = soup.find_all("script")
    for script in scripts:
        if script.text[:18] == "window._sharedData":
            break

    data = json.loads(script.contents[0][21:-1])
    # print(json.dumps(data, indent=4))
    print("caption: " + data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_caption"]["edges"][0]["node"]["text"].encode('utf-8'))
    print("user: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))
    print("full name: " + data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["full_name"].encode('utf-8'))
    print("comments: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    print("likes: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    print("url: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))
    print("location: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["location"]))

    print("################################################")

    mycsv.writerow([str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]), data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_caption"]["edges"][0]["node"]["text"].encode('utf-8'), 
        str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]), str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]), link, str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"])])





