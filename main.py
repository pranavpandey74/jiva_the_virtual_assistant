import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import wikipedia
from googletrans import Translator
import os
import pyautogui
import wikipedia as googleScrap
import psutil
import time
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 170)


def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()


def takequery():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your query :  {query}\n")

    except:
        Speak(" ")
        query = takequery()

    return query.lower()

def wish():
    Speak("Hello sir i am jiva .")
    Speak("Initializing  and Starting all systems applications")
    Speak("Installing and checking all drivers")
    Speak("Wait a moment sir")
    Speak("All drivers are up and running")
    Speak("All systems have been activated")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        Speak("Good Morning")
    elif hour > 12 and hour < 18:
        Speak("Good afternoon")
    else:
        Speak("Good evening")
def TaskExe():
    wish()
    Speak("Now I am online")
    Speak("How can i help you ?")

    def Music():

        webbrowser.open('https://music.youtube.com/watch?v=4jUkciRhqPc&list=RDAMPLRDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g')
        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")

        if 'tor browser' in query:
            os.startfile("C:\\Users\\PRANAV KUMAR PANDEY\\Desktop\\Tor Browser\\Browser\\firefox.exe")

        elif 'zoom' in query:
            os.startfile("C:\\Users\\PRANAV KUMAR PANDEY\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your query Has Been Completed Sir!")

    def Temp():
        search = "temperature in ranchi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} ")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takequery()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takequery()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            Speak("no problem sir")

    def SpeedTest():
        import speedtest
        Speak("Checking speed....")
        speed = speedtest.Speedtest()
        uploading = speed.upload()
        download = speed.download()
        correct_Up = int(uploading/800000)
        correct_down = int(int(download) / 800000)

        if 'uploading speed' in query:
            Speak(f"uploading speed is {correct_Up}mbps")
        elif 'downloading speed' in query:
            Speak(f"downloading speed is {correct_down}mbps")
        else:
            Speak(f"uploading speed is {correct_Up}mbps and downloading speed is {correct_down}mbps")

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = takequery()

        if 'self confidence' in name:

            os.startfile('F:\\confidential document\\coaching dhundo files\\my '
                         'books\\SelfConfidenceUnleashed\\Self-Confidence.pdf')
            book = open('F:\\confidential document\\coaching dhundo files\\my '
                        'books\\SelfConfidenceUnleashed\\Self-Confidence.pdf', 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = takequery()
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takequery()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text, 'hi')
                textm = textHin.text
                speech = gTTS(text=textm)
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'java' in name:
            os.startfile('F:\\java.pdf')
            book = open('F:\\java.pdf', 'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = takequery()
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takequery()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text, 'hi')
                textm = textHin.text
                speech = gTTS(text=textm)
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")
        elif 'zoom' in query:
            os.system("TASKKILL /F /im Telegram.exe")
        elif 'tor browser' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Speak("Your query Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your query ?")
        comm = takequery()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def TakeHindi():
        query = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            query.pause_threshold = 1
            audio = query.listen(source)

            try:
                print("Recognizing.....")
                query = query.recognize_google(audio, language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak(Text)

    def ChromeAuto():
        Speak("Chrome Automation started!")

        query = takequery()

        if 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

    def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takequery()
        path1name = path + ".png"
        path1 = "F:\\confidential document\\jiva\\screenshot" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("F:\\confidential document\\jiva\\screenshot")
        Speak("Here Is Your ScreenShot")

    def whatsapp():
        Speak("Sir tell me the name of person!")
        name = takequery()
        print(name)
        if 'pranav' in name:
            Speak("sir tell me the message!")
            msg = takequery()
            Speak(msg)
            Speak("please tell me the time in hour")
            hour = takequery()
            Speak('thankyou and tell me the minutes ?')
            minute = takequery()
            pywhatkit.sendwhatmsg("+918340112546", msg, hour, minute, 15)
            Speak('ok sir , sending the message !')
        elif 'abhay sir' in name:
            Speak("sir tell me the message!")
            msg = takequery()
            Speak(msg)
            Speak("sir tell me the time")
            Speak("please tell me the time in hour")
            hour = takequery()
            Speak('thankyou and tell me the minutes ?')
            minute = takequery()
            pywhatkit.sendwhatmsg("+919470564054", msg, hour, minute, 15)
            Speak('ok sir , sending the message !')
        else:
            Speak("Network Error occured !!!")
    while True:
        query = takequery()

        if 'hello' in query:
            Speak("Hello Sir , I Am jiva .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'i a good' in query:
            Speak("oh! that amazing..")

        elif 'time' in query:
            time1 = datetime.datetime.now().strftime('%I:%M %p')
            Speak('Current time is ' + time1)


        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            Speak(info)

        elif 'i love you' in query:
            Speak('sorry sir ')
            Speak('I don\'t know what you are Speaking')
            Speak('but i can love you but i need a time to understand')
            Speak('you can teach me the how to love someone')


        elif 'shut ' in query:
            Speak('Sorry sir for my mistake')
        elif 'appritiate me' in query:
            Speak('Pranav sir you are intelligent and smart')


        elif 'are you single' in query:
            Speak('No sir ,I am not in any relationship ')

        elif 'you like jarvis' in query:
            Speak('jarvis is a AI just like me')
            Speak('i like you sir i don\'t like jarvis ')
            Speak('i only follow your query sir')



        elif 'alexa' in query:
            Speak("Who is alexa ???")

        elif 'sorry i mean jiva' in query:
            Speak("no i don/'t want to Speak with you")
            Speak("say sorry or i am going")
            sorry = takequery()
            if 'sorry' in sorry:
                Speak("it/'s okay pranav sir ")
                Speak("now please tell me how can i help you")
            else:
                Speak("okay sir bye have a nice day")
                break

        elif 'you are bad girl' in query:
            Speak('No sir , who told you ')
            Speak('you know me na ...i am a good girl ')

        elif 'tell me about pranav' in query:
            Speak('my creator is pranav pandey')
            Speak('he is such a nice person ')
            Speak('he is currently working as a coding instructor in nist academy')
            Speak('and he is currently pursuing MscIT from doctor shyama prashad mukherjee university')

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up jiva!")
            break

        elif 'wake up' in query:
            Speak('i am online again sir')
            Speak('How may i help you')
            query = takequery()

        elif "where is" in query:
            data1 = query.split(" ")
            location = data1[2]
            Speak("Hold on Sir, I will show you where " + location + " is.")
            os.system("chrome quantum https://www.google.com/maps/place/" + location + "/&amp;")


        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("jeeva", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jeeva", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch webpage' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takequery()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jeeva", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 3)
            Speak(f"According To Wikipedia : {wiki}")

        elif "what is" in query:
            query = query
            query = query.replace("what is ", "")
            wiki_says = wikipedia.summary(query)
            Speak(wiki_says)

        elif 'screenshot' in query:
            screenshot()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open tor' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close tor' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takequery()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@22.7570593,86.2260032,13z')

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = takequery()

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now > time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0, 0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root, text="Youtube Video Downloader", font='arial 15 bold').pack()
            link = StringVar()
            Label(root, text="Paste Yt Video URL Here", font='arial 15 bold').place(x=160, y=60)
            Entry(root, width=70, textvariable=link).place(x=32, y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root, text="Downloaded", font='arial 15').place(x=180, y=210)

            Button(root, text="Download", font='arial 15 bold', bg='pale violet red', padx=2,query=VideoDownloader).place(x=180, y=150)

            root.mainloop()
            Speak("Video Downloaded")

        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that", "")
            remeberMsg = remeberMsg.replace("jeeva", "")
            Speak("You Tell Me To Remind You That :" + remeberMsg)
            remeber = open('data.txt', 'w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt', 'r')
            Speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            query = query.replace("jiva", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            gweb = 'https://www.google.com/search?q=' + query
            webbrowser.open(gweb)
            Speak('done pranav sir')


        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jeeva", "")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'temperature' in query:
            Temp()

        elif 'read book' in query:
            Reader()
        elif 'whatsapp message' in query:
            query = same.replace("jeeva", "")
            same = query.replace("send", "")
            query = query.replace("whatsapp message", "")
            query = query.replace("to", "")
            name = query

            if 'buddy' in name:
                numb = "8340112546"
                Speak(f"What's The Message For {name}")
                mess = takequery()
                pywhatkit.whatsapp(numb, mess)

            elif 'shubham' in name:
                numb = "123524648"
                Speak(f"What's The Message For {name}")
                mess = takequery()
                pywhatkit.whatsapp(numb, mess)

            elif 'now' in name:
                gro = "LVSfnl4CGMhA62qK2Tex9Z"
                Speak(f"What's The Message For {name}")
                mess = takequery()
                pywhatkit.Whatspp_Grp(gro, mess)


