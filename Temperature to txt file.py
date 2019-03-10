"""
This class is to open an URL, dig into it and finds the usefull data, such as temperature or sea level,
make a copy from it,store them into local txt file

"""
import urllib.request as rq
import time




class ValiddatingURL:
    URL = "http://www.python.org"

    def __init__(self, URL):
        if type(URL) is not str:
            raise TypeError("Not a valid URL")





















