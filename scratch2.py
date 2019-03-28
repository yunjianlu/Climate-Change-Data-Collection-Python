# def multuplier(lst):
#     return  list(map(lambda x: x * 2, lst))
#
#
#
# list1 = [1,2,5,8,16,32]
# print (multuplier(list1))


import time
import urllib.request as rq
urls = [
    'http://www.python.org',
    'http://www.python.org/about/'
    ]

def single_fetch():
   start_time = time.time()
   list(map(lambda url: print(url, len(str(rq.urlopen(url).read()))), urls))
   end_time = time.time()
   print(f"=== threads=1, duration={end_time-start_time} ===")



from multiprocessing.dummy import Pool
import urllib.request as rq



def parallel_fetch():
   threads = 4
   start_time = time.time()
   pool = Pool(threads)
   pool.map(lambda url: print(url, len(str(rq.urlopen(url).read()))), urls)
   pool.close()
   pool.join()
   end_time = time.time()
   print(f"=== threads={threads}, duration={end_time-start_time} ===")





a = single_fetch()
b = parallel_fetch()