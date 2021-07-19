import json
import schedule
from notifypy import Notify
from time import sleep
from datetime import datetime
from random_word import RandomWords

def my_log(message):
    '''This Function Write Message In Log File'''
    with open("logfile.txt", "a") as f:
        f.write(f"{message} {datetime.now()}\n")

def vocabulary_notify():
    '''This Function Return Random English Word With It's Meaning'''
    try:
        #Fetch Word And Meaning
        WordData = RandomWords().word_of_the_day()
        WordDict = json.loads(WordData)
        Word = WordDict['word']
        Meaning = WordDict['definations'][0]['text']

        #Send Notification
        Notification = Notify()
        Notification.title = Word
        Notification.message = Meaning
        Notification.icon = "icon/word.png"
        Notification.send()
    except:
        print('Something Went Wrong..!')

def water_notify():
    '''This Function Send Notification For Drinking Water'''
    try:
        #Create Log
        my_log("Drank Water :- ")

        #Send Notification
        Notification = Notify()
        Notification.title = 'Water Reminder'
        Notification.message = 'You Have Passed 40 Minutes So You Have To Drink Water Now. Please Drink Water'
        Notification.icon = "icon/water.png"
        Notification.send()
    except:
        print('Something Went Wrong..!')

def eyes_notify():
    '''This Function Send Notification For Eyes Relax'''
    try:
        #Create Log
        my_log("Relaxed Eyes :- ")

        #Send Notification
        Notification = Notify()
        Notification.title = 'Relax Eyes Reminder'
        Notification.message = 'You Have Passed 50 Minutes So You Have To Relax Your Eyes Now. Please Relax Your Eyes'
        Notification.icon = "icon/eyes.png"
        Notification.send()
    except:
        print('Something Went Wrong..!')

def exercise_notify():
    '''This Function Send Notification For Exercise'''
    try:
        #Create Log
        my_log("Did Exercise :- ")

        #Send Notification
        Notification = Notify()
        Notification.title = 'Exercise Reminder'
        Notification.message = 'You Have Passed 1 Hour So You Have To Do Exercise Now. Please Do Exercise'
        Notification.icon = "icon/exercise.png"
        Notification.send()
    except:
        print('Something Went Wrong..!')


if __name__ == "__main__":

    #Schedule Word Notification Daily At 10:30 AM
    schedule.every().day.at("10:30").do(vocabulary_notify)
    
    #Schedule Water Reminder Every 40 Mintues
    schedule.every(40).minutes.do(water_notify)
    
    #Schedule Relax Eyes Reminder Every 50 Mintues
    schedule.every(50).minutes.do(eyes_notify)
    
    #Schedule Exercise Reminder Every 60 Mintues
    schedule.every().hour.do(exercise_notify)

    #Checks Whether Scheduled Task Is Pending To Run Or Not
    while True:
        schedule.run_pending()
        sleep(1)