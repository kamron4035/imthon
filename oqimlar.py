from threading import Thread
from httpx import get
from datetime import timedelta
import redis
con = redis.Redis(host='localhost', port=6385, decode_responses=True)


def therad(site):
    response = get(f"https://{site}/")
    data = response.content
    con.set(name=site, value=data, ex=timedelta(seconds=60))


thr1 = Thread(target=therad,args=('olx.uz',))
thr2 = Thread(target=therad,args=('kun.uz',))
thr3 = Thread(target=therad,args=('uzum.uz',))
thr4 = Thread(target=therad,args=('wikipedia.org',))
thr5 = Thread(target=therad,args=('qalampir.uz',))

#__starts
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr5.start()
#__join
thr1.join()
thr2.join()
thr3.join()
thr4.join()
thr5.join()

