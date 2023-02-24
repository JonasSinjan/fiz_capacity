import urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time

data = {}

def current_capacity():
  contents = urllib.request.urlopen("https://intern.sport.uni-goettingen.de/fizdb/getjson.php?action=fizcapacity").read()
  str_b = contents.decode("utf-8")
  capacity = str_b.split(':')[1][:4]
  if '}' in capacity:
    capacity = capacity.strip("}")
  maxValue = 80
  number = round(float(capacity)*maxValue)
  print(f" Fiz Goettingen: {capacity}")
  print(f" Current: {number}/80")
  time = datetime.now()
  data[f"{time.hour}:{time.minute}"] = number


for x in range(100):
  print(datetime.now())
  current_capacity()
  time.sleep(300)

# scheduler = BlockingScheduler()
# scheduler.add_job(current_capacity, 'interval', minutes = 15)
# scheduler.start()
