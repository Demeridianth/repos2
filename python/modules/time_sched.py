import schedule
import time

def job(t):
    print ("I'm working...", t)
    return

schedule.every().day.at("18:26").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(10) # wait 10 seconds