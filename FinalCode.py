import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import random
import wolframalpha
import pyjokes
from datetime import date
from googlesearch import search
from PyDictionary import PyDictionary
print("\n\n\n")
print("###########INSTRUCTIONS############")
print("#just speak what you want when the Assistant starts listening.")
print("#You can Use Specific Keywords for specific functions:-")
print("-------KEYWORDS--------|---------FUNCTION-------|")
print("1)    WIKIPEDIA        |         WIKIPEDIA      |")
print("2)     SEARCH          |       GOOGLE SEARCH    |")
print("3)     ALPHA           |      WOLFRAM SEARCH    |")
print("4)   TIME/DATE         |        TIME/DATE       |")
print("5) MEANING OF <WORD>   |        DICTIONARY      |")
print("6)****I AM BORED*******|RANDOM programming JOKES|")
print("7) OPEN <SOMETHING>    |OPEN VARIOUS SITES/APPS |(Like downloads,codeblocks,spotify etc.)")
print("8)    SHUT DOWN        |  SHUTS YOUR LAPPY DOWN |")
print("-----------------------|------------------------|")
print("\n")
print("**you can also open some common websites LIKE:")
print("->google; youtube; google_drive; facebook; instagram; twitter; Stack_Overflow; Git_Hub;")
print("->IITR MAIN WEBSITE ; CHANNEL I ;")
print("***YOU! CAN ALSO OPEN SOME COMMON APPS ON YOUR PC LIKE:")
print("@->CODE_BLOCKS  @->SPOTIFY  @->PLAY MUSIC")

client = wolframalpha.Client('TUXL5R-5WYA3T7LVP')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("how can I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.pause_threshold = 0.8
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        #group of "open" keyword related programmes
        if 'open' in query:
            if 'open youtube' in query or 'open you tube' in query:
              webbrowser.open_new_tab("youtube.com")

            elif 'open google scholar' in query:
              webbrowser.open("https://scholar.google.com/")

            elif 'open google' in query:
              webbrowser.get(chrome_path).open_new_tab("google.com")

            elif 'open reddit' in query:
              webbrowser.open_new_tab("reddit.com")

            elif 'open google drive' in query:
              webbrowser.open("drive.google.com")

            elif 'open facebook' in query:
              webbrowser.open("www.facebook.com")

            elif 'open instagram' in query:
              webbrowser.open("www.instagram.com")

            elif 'open geeksforgeeks' in query:
              webbrowser.open("https://www.geeksforgeeks.org")

            elif 'open stackoverflow' in query:
              webbrowser.open_new_tab("stackoverflow.com")
            elif 'open stack overflow' in query:
              webbrowser.open_new_tab("stackoverflow.com")

            elif 'open codechef' in query:
                 webbrowser.open_new_tab("www.codechef.com")
            elif 'open code chef' in query:
                 webbrowser.open_new_tab("www.codechef.com")

            elif 'open udemy' in query:
              webbrowser.open("www.udemy.com")

            elif 'open learncpp' in query:
              webbrowser.open("www.learncpp.com")
            elif 'open learn cpp' in query:
                 webbrowser.get(chrome_path).open("www.learncpp.com")

            elif 'open main website' in query:
              webbrowser.open("www.iitr.ac.in")

            elif 'open channel i' in query:
              webbrowser.open("www.channeli.in")

            elif 'open github' in query or 'open git hub' in query:
              webbrowser.open("www.github.com")

            elif 'open twitter' in query:
              webbrowser.open("www.twitter.com")

            elif 'open movies' in query:
              webbrowser.open("yts.lt")

            elif 'open course' in query:
              webbrowser.open("www.coursera.org")
            elif 'open coursera' in query:
                webbrowser.open("www.coursera.org")

            elif 'open e library' in query:
              webbrowser.open("https://ndl.iitkgp.ac.in/")

            elif 'open photoshop' in query:
              webbrowser.open("www.photoshop.com")

            elif 'open glassdoor' in query:
              webbrowser.open("https://www.glassdoor.co.in/index.htm")

            elif 'open linkedin' in query:
              webbrowser.open("https://in.linkedin.com/")

            elif 'open ted talks' in query:
              webbrowser.open("https://www.ted.com/#/")

            elif 'open code blocks' in query:
              codePath = "C:\\Program Files (x86)\\CodeBlocks\\CodeBlocks.exe"
              os.startfile(codePath)
            elif 'open codeblocks' in query:
             codePath = "C:\\Program Files (x86)\\CodeBlocks\\CodeBlocks.exe"
             os.startfile(codePath)

        elif 'wikipedia' in query:
           try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            if "in" in query:
                query = query.replace("in", "")
            if "search" in query:
                query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
           except:
                print("sorry, could not find a result")
                speak("sorry, could not find a result")
        elif 'activate alpha' in query or 'wolfram alpha' in query or 'wolfram'in query:

            while True:
             print('do you want to ask oral question or a math expression?')
             speak('do you want to ask oral question or a math expression?')
             print('speak oral/mathematics/exit')
             inp=takeCommand()
             if 'oral' in inp:
                 speak("ask question")
                 print("ask question: ")
                 query=takeCommand()
             elif 'mathematics' in inp:
                 print('Please type the question: ')
                 query=input()
             elif 'exit' in inp:
                 break
             try:
               res=client.query(query)
               output=next(res.results).text
               print(output)
               speak(output)
             except StopIteration:
               print('speak again')
             except :
               print("can't find this in library")
             inp=''
             query=''
        elif 'google search' in query:
            query=query.replace("google search","")
            # you have to update this path for your machine for now
            #chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                try:
                    webbrowser.open("https://google.com/search?q=%s" % query)
                except webbrowser.Error:
                    print("unexpected error happened in webbrower")
        elif 'meaning of ' in query:
            query=query.replace("meaning of ","")
            dictionary=PyDictionary()
            try:
                     query=query.replace("what is the meaning of ","")
                     b='here is the meaning of the word'
                     c=b+query
                     speak(c)
                     test_dict=dictionary.meaning(query)
                     res = [ value[i] for key,value in test_dict.items() for i in range(1)]
                     print (str(res[0]))                  # shows most relevent meaning
                     speak(str(res[0]))
            except:
                  print("sorry! word not found...")

        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            y=random.randrange(0,50,1)
            print(songs[y])
            os.startfile(os.path.join(music_dir, songs[y]))

        elif'exit code blocks' in query or 'exit codeblocks' in query:
            os.system("taskkill /f /im codeblocks.exe")

        elif 'exit' in query:
            speak("good bye sir, have a nice day")
            sys.exit()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The Time is : "+strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            print("Present date is : ",end="")
            print(date.today())
            speak(date.today())

        elif'spotify' in query:
            os.startfile("C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe")

        elif 'exit spotify' in query:
            os.system("taskkill /f /im spotify.exe")

        elif'visual studio' in query:
            os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif'code' in query:
            os.startfile("C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'downloads' in query:
            os.startfile("C:\\Users\\hp\\Downloads")
        elif 'download' in query:
            os.startfile("C:\\Users\\hp\\Downloads")

        elif 'exit spotify' in query:
            os.system("taskkill /f /im spotify.exe")

        elif 'i am bored' in query:
            speak('maybe this programmer joke could make you smile.')
            speak(pyjokes.get_joke())

        elif 'shut down' in query:
            os.system("shutdown /s /t 1")
        elif 'shutdown' in query:
             os.system("shutdown /s /t 1")  
