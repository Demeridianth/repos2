import schedule

def job():
    print('start working')

schedule.every(1).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at('10:30').do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at('12:15').do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()

# lol