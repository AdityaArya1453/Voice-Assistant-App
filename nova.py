import pyttsx3
import speech_recognition as sr
import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import random
from requests import get
import wikipedia
import pyjokes
import os
import cv2
import requests
from bs4 import BeautifulSoup
from requests import get
import wikipedia
import webbrowser
import sys
import pyautogui
import PyPDF2
import smtplib
import instaloader
from PyQt5 import QtWidgets, QtCore , QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from NovaGui import Ui_MainWindow
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 # print (voices[0].id)


engine.setProperty('voice',voices[len(voices) -1].id)


# text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



def wish():
#     hour = int(datetime.datetime.now().hour)
#     tt = time.strftime("%I:%M %p")

#     if hour>=0 and hour<=12:
#            speak(f"good morning ")  
#     elif hour >=12 and hour <=18:
#            speak(f"good afternoon ")
#     else:
#            speak(f"good evening")
    speak("Hello sir, I am NOVA . How can I help you")       




def pdf_reader():
        book = open('py3.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages 
        speak(f"total number of pages in this book {pages}")
        speak("sir please enter the page number i have to read")
        pg = int(input("Please enter the page number:"))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)




class MainThread(QThread):
        def __init__(self):
          super(MainThread,self).__init__()
        def run(self):
          self.TaskExecution()


        def take_command(self):
                        r = sr.Recognizer()
                        with sr.Microphone() as  source :
                                print("listening ...")   
                                r.pause_thresghold = 1
                                audio = r.listen(source)
                                # audio = r.listen(source,timeout=5,phrase_time_limit=8)

                        
                        try:

                                print("Recognizing...")  
                                # audio = r.listen(source)
                                # query = r.recognize_google(audio)
                                # query = query.lower()
                                query = r.recognize_google(audio ,language = 'en-in')
                                print(f"user said :{query}") 

                        except Exception as e:
                                # speak("Sir please say that again...") 
                                return "none"
                        query = query.lower()
                        return query  
                        


        # def run(self):
        #         # self.TaskExecution()
        #         speak("please say wake up to continue")
        #         while True:
        #                 self.query = self.take_command()
        #                 if"wake up" in self.query or "are you there" in self.query or "hello" in self.query:
        #                         self.TaskExecution()




        def TaskExecution(self):
                        wish()
                        while True:

                                self.query = self.take_command().lower()

        
                                if "hello" in self.query:
                                        speak("Hello sir, how are you ?")

                                elif "i am fine" in self.query:
                                        speak("that's great, sir")

                                elif "how are you" in self.query:
                                        speak("Perfect, sir")

                                elif "thank you" in self.query:
                                        speak("you are welcome, sir")



                                elif 'play' in self.query:
                                        song = self.query.replace('play', '')
                                        speak('playing' + song)
                                        pywhatkit.playonyt(song)

                                
                                

                                
                                elif " stop  " in self.query:
                                        speak("ok sir ")
                                        os.system("taskkill /f /im chrome.exe")

                                elif "google" in self.query:
                                        from SearchNow import searchGoogle
                                        searchGoogle(self.query)

                                elif "youtube" in self.query:
                                        from SearchNow import searchYoutube
                                        searchYoutube(self.query)

                                elif "wikipedia" in self.query:
                                        from SearchNow import searchWikipedia
                                        searchWikipedia(self.query)


                                
                                

                                elif "temperature" in self.query:
                                        search = "temperature in delhi"
                                        url = f"https://www.google.com/search?q={search}"
                                        r  = requests.get(url)
                                        data = BeautifulSoup(r.text,"html.parser")
                                        temp = data.find("div", class_ = "BNeawe").text
                                        speak(f"current{search} is {temp}")



                                elif "weather" in self.query:
                                        search = "temperature in delhi"
                                        url = f"https://www.google.com/search?q={search}"
                                        r  = requests.get(url)
                                        data = BeautifulSoup(r.text,"html.parser")
                                        temp = data.find("div", class_ = "BNeawe").text
                                        speak(f"current{search} is {temp}")

                                
                                
                                elif 'joke' in self.query:
                                        speak(pyjokes.get_joke())



                                elif "open" in self.query:   #EASY METHOD
                                        query = self.query.replace("open","")
                                        query = self.query.replace("Nova","")
                                        pyautogui.press("super")
                                        pyautogui.typewrite(self.query)
                                        pyautogui.sleep(2)
                                        pyautogui.press("enter") 



                                elif "open google" in self.query:
                                        npath = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
                                        os.startfile(npath)


                                elif "close browser " in self.query:
                                        speak("ok sir ")
                                        os.system("taskkill /f /im chrome.exe") 



                                elif "open youtube" in self.query:
                                                webbrowser.open("www.youtube.com")





                                elif "open google" in self.query:
                                                speak("Sir, what should i search on google?")
                                                cm = self.take_command().lower()
                                                webbrowser.open(f"{cm}")


                                elif "close google" in self.query:
                                        speak("ok sir ")
                                        os.system("taskkill /f /im chrome.exe") 



                                elif "take screenshot" in self.query:
                                        speak("sir, please tell me the name for screenshot file")
                                        name = self.take_command().lower()
                                        speak("please hold on for few seconds, i am taking screenshot")
                                        # time.sleep(3)
                                        img = pyautogui.screenshot()
                                        img.save(f"{name}.png")
                                        speak("the screenshot has been saved in main folder. now i am ready for next task")



                                elif "read pdf" in self.query:
                                        pdf_reader()



                                elif 'time ' in self.query:
                                        time = datetime.datetime.now().strf.time('%I:%M %p')
                                        print(time)
                                        speak('Current time is ' + time)   




                                # elif "open camera" in self.query:
                                #         cap = cv2.VedioCapture(0)
                                #         int k
                                #         while True:
                                #                 ret, img = cap.read()
                                #                 cv2.waitKey(50)
                                #                 if k ==27:
                                #                         break;
                                #                 cap.release()
                                #                 cv2.destroyAllWindows




                                elif "open" in self.query:
                                        from Dictapp import openappweb
                                        openappweb(self.query)



                                elif "close" in self.query:
                                        from Dictapp import closeappweb
                                        closeappweb(self.query)



                                elif "pause" in self.query:
                                        pyautogui.press("k")
                                        speak("video paused")

                                        
                                elif "stop playing " in self.query:
                                        pyautogui.press("k")
                                        speak("video paused")


                                elif "stop" in self.query:
                                        pyautogui.press("k")
                                        speak("video paused")


                                elif "play" in self.query:
                                        pyautogui.press("k")
                                        speak("video played")


                                elif "mute" in self.query:
                                        pyautogui.press("m")
                                        speak("video muted")


                                elif "volume up" in self.query:
                                        from keyboard import volumeup
                                        speak("Turning volume up,sir")
                                        volumeup()


                                elif "volume down" in self.query:
                                        from keyboard import volumedown
                                        speak("Turning volume down, sir")
                                        volumedown()





                                elif "open" in self.query:
                                        from Dictapp import openappweb
                                        openappweb(self.query)

                                elif "close" in self.query:
                                        from Dictapp import closeappweb
                                        closeappweb(self.query)




                                elif "shut down" in self.query:
                                        speak("ok sir , shutdowning your computer")
                                        os.system("shutdown /s /t 5")                        



                                elif  "turn pc into sleep mode" in self.query:
                                        os.system("rundl132.exe powrprof.d;;,SetSuspendState 0,1,0")
                                        


                                
                                elif "restart" in self.query:
                                        speak("restarting your computer")
                                        os.system("shutdown /s /t 5")





                                elif"thanks nova" in self.query : 
                                        speak("Thank you sir , have a good day.") 
                                        sys.exit() 


                                elif "Thank you nova" in self.query : 
                                        speak("Thank you sir , have a good day.") 
                                        sys.exit() 




                                elif "exit" in self.query: 
                                        speak("Thank you sir , have a good day.") 
                                        sys.exit() 



                                elif "you can sleep" in self.query : 
                                        speak("okay sir , ") 
                                        break

                                



# TaskExcecution()        
#         if __name__=="__main__":
#                 while True:
#                         permission = take_command()  
#                         if "wake up" in permission:
#                                 TaskExecution()

#                         elif "bye"   in permission:
#                                      speak("thanks for using me sir , have a good day")
#                                      sys.exit()

#                         elif"thanks nova" in permission : 
#                                         speak("Thank you sir , have a good day.") 
#                                         sys.exit() 


#                         elif "Thank you nova" in permission : 
#                                         speak("Thank you sir , have a good day.") 
#                                         sys.exit() 


#                         elif "exit" in permission: 
#                                         speak("Thank you sir , have a good day.") 
#                                         sys.exit() 







startExecution = MainThread()


class Main(QMainWindow):
        def __init__(self)  :
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)


        def  startTask(self):
            self.ui.movie = QtGui.QMovie("../../Pictures/GUI/UI-data visualize project.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            startExecution.start()




app = QApplication(sys.argv)
QApplication.setApplicationName('NOVA')
Nova = Main()
Nova.show()
exit(app.exec_())

input()
