
import pyttsx3 # it convert text to speech
import speech_recognition as sr # convert speech into text
import datetime
import os # it provide the interaction between user and operating system
import cv2 # use to access your web cam and capture pictures
import random
from requests import get # request web page and The get() method sends a GET request to the specified url.
import wikipedia
import webbrowser # simply calling the open() function from this module will open url using the default browser
#import pywhatkit as kit # for sending WhatsApp messages
import smtplib # used to send mail
import sys #provides various functions and variables that are used to manipulate different parts of the Python runtime environment.
import time
import pyjokes # for jokes
import requests
import pyautogui # simulate mouse cursor moves and clicks as well as keyboard button presses.
import pyaudio # To record or play audio, open a stream on the desired device with the desired audio parameters using pyaudio.
from email.mime.text import MIMEText # use for transfer one or mutiple attachments
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path # use for path directory


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("i am jarvis sir. please tell me how may i help you")


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prateekkumar2681@gmail.com', 'Prateek@1503')
    server.sendmail('prateekkrsmart@gmail.com', to, content)
    server.close()




#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="YOUR_API_HERE"'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__": #main program
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')


        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = r"H:\Jarvis\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))



        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+917361934985", "this is testing protocol",4,13)
            time.sleep(120)
            speak("message has been sent")

        elif "song on youtube" in query:
            kit.playonyt("see you again")

        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')
        elif "email to Pratik" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to,content)
                speak("Email has been sent to Prateek")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to avi")


        elif "ok go to sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()



        #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")


        #to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        ###########################################################################################################################################
        ###########################################################################################################################################



        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()


        elif "email to Pratik" in query:

            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'prateekkumar2681@gmail.com' # Your email
                password = '123456' # Your email account password
                send_to_email = 'prateekkrsmart@gmail.com' # Whom you are sending the message to
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query   # The Subject in the email
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2  # The message in the email
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")    # The File attachment in the email

                speak("please wait,i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to Prateek")

            else:
                email = 'prateekkumar2681@gmail.com' # Your email
                password = 'Prateek@1503' # Your email account password
                send_to_email = 'prateekkrsmart@gmail.com' # Whom you are sending the message to
                message = query # The message in the email

                server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
                server.starttls() # Use TLS
                server.login(email, password) # Login to the email server
                server.sendmail(email, send_to_email , message) # Send the email
                server.quit() # Logout of the email server
                speak("email has been sent to Prateek")


        #speak("sir, do you have any other work")

