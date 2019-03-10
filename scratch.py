# print(type("hello"))
#
#
# def apply(f, x):
#    return f(x)
#
# apply(lambda x: x * 3, 10)
#
# doubles = []
# l = range(10)
# for element in l:
#     doubles.append(element * 2)
#
# doubles2 = []
#
# doubles2 = list(map(lambda x: x * 2, l))
# print(doubles2)
import time
import time
import urllib.request as rq
#
# url = "http://www.google.com"
# tem = (str(rq.urlopen(url).read()))
# for ele in tem:
#     print (ele)

# print(url, (str(rq.urlopen(url).read())))


urls = [
    'http://www.python.org',
    'http://www.python.org/about/'
]


def single_fetch():
   start_time = time.time()
   list(map(lambda url: print(url, len(str(rq.urlopen(url).read()))), urls))
   end_time = time.time()
   print(f"=== threads=1, duration={end_time-start_time} ===")


single_fetch()