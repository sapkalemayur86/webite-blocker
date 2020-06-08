import time
from datetime import datetime as dt
host_path="/etc/hosts"
redirect="127.0.0.1"
web_list=["facebook.com","www.facebook.com","www.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print('working hours')
        with open(host_path,'r+')as file:
            content=file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+'\n')
        time.sleep(5)

    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
