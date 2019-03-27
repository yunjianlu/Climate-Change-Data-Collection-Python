"""
This class is to open an URL, dig into it and finds the usefull data, such as temperature or sea level,
make a copy from it,store them into local txt file

"""

import json
from enum import Enum
import requests
import time

#get data from web and store it in to local file
class OxfordDictionary:

    # retrive data from The world Bank
    the_world_data_bank = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/type/var/start/end/ISO3[.ext]"



    app_id = '90aee85f'
    app_key = 'da42e57c65311bffa5ea9db494ac245a'

    def search(self, word):
        language = 'en'

        word_id = word

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

        r = requests.get(url, headers={'app_id': self.app_id, 'app_key': self.app_key})
        if r.status_code != 200:
            raise Exception(f"Something wrong due to status code { r.status_code}")
        resp = r.json()

        # rap the results into Dict Entry
        part_of_speech =(((resp["results"][0])["lexicalEntries"])[0])["lexicalCategory"]
        definition = (((((resp["results"][0])["lexicalEntries"])[0])["entries"][0])["senses"][0])["definitions"][0]
        try:
            example = ((((((resp["results"][0])["lexicalEntries"])[0])["entries"][0])["senses"][0])["examples"][0])["text"]
        except:
            example = None


        for ele in resp:
            if ele.isdigit:
                data_for_day = ele

        dic= ""
        dic += (word, part_of_speech, definition, example)
        return dic

    # TODO: store the data into jason file, later compute it as graphing.

# if want to search something and store it into local.
if "__main__" == __name__:
    while True:
        word_for_seach =  input("what word do yo want to look at")
        dict = OxfordDictionary()
        print(dict.search(word_for_seach))
















