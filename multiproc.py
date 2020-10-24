from main import b_feed_func, stop_func
from apihost import apifunc, apihold
import ray.remote_function
import time
ray.init()



@ray.remote
def func1():
    b_feed_func()
    if b_feed_func() == 0:
        print('... Exit')




@ray.remote
def func2():
    while True:
        apifunc()









ret_id1 = func1.remote()
ret_id2 = func2.remote()

#ret1, ret2 = ray.get([ret_id1, ret_id2])
ret1 = ray.get([ret_id1])




