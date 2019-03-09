"""
This class is to open an URL, dig into it and finds the usefull data, such as temperature or sea level,
make a copy from it,store them into local txt file

"""

class ValiddatingURL:
    URL = "www.google.com"

    def __init__(self, URL):
        if type(URL) is not str:
            raise TypeError("Not a valid URL")





















