from datetime import date
import ctypes
import shutil
import os
import requests
import time
start_time = time.time()


r = requests.get(
    'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US').json()

url = 'https://www.bing.com' + r['images'][0]['url']
#url = 'https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg'
r2 = requests.get(url, stream=True)
if r2.status_code == 200:
    with open('bing-wp-img.jpg', 'wb') as f:
        r2.raw.decode_content = True
        shutil.copyfileobj(r2.raw, f)

ctypes.windll.user32.SystemParametersInfoW(
    20, 0, f'{os.getcwd()}\\bing-wp-img.jpg', 0)


print("--- %s seconds ---" % (time.time() - start_time))
