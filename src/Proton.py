import pyttsx3
import speech_recognition as sr
from datetime import date
import time
import webbrowser
import datetime
from pynput.keyboard import Key, Controller
import pyautogui
import sys
import os
from os import listdir
from os.path import isfile, join
import smtplib
import wikipedia
import Gesture_Controller
#import Gesture_Controller_Gloved as Gesture_Controller
import Function
import app
import threading 


# -------------Object Initialization---------------
today = date.today()
r = sr.Recognizer()
keyboard = Controller()
engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# ----------------Variables------------------------
file_exp_status = False
files =[]
path = ''
is_awake = True  #Bot status

# ------------------Functions----------------------
def reply(audio):
    app.ChatBot.addAppMsg(audio)
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        reply("Good Morning!")
    elif hour>=12 and hour<18:
        reply("Good Afternoon!")   
    else:
        reply("Good Evening!")  
        
    reply("I am Exlaw, how may I help you?")

# Set Microphone parameters
with sr.Microphone() as source:
        r.energy_threshold = 500 
        r.dynamic_energy_threshold = False

# Audio to String
def record_audio():
    print("Here in record audio")
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        voice_data = ''
        audio = r.listen(source, phrase_time_limit=5)

        try:
            voice_data = r.recognize_google(audio)
        except sr.RequestError:
            reply('Sorry my Service is down. Plz check your Internet connection')
        except sr.UnknownValueError:
            print('cant recognize')
            pass
        return voice_data.lower()


# Executes Commands (input: string)
def respond(voice_data):
    global file_exp_status, files, is_awake, path
    print(voice_data)
    voice_data.replace('exlaw','')
    app.eel.addUserMsg(voice_data)

    if is_awake==False:
        if 'wake up' in voice_data:
            is_awake = True
            wish()

    # STATIC CONTROLS
    elif 'hello' in voice_data:
        wish()

    elif 'what is your name' in voice_data:
        reply('My name is Exlaw!')

    elif 'date' in voice_data:
        reply(today.strftime("%B %d, %Y"))

    elif 'time' in voice_data:
        reply(str(datetime.datetime.now()).split(" ")[1].split('.')[0])

    elif 'search' in voice_data:
        reply('Searching for ' + voice_data.split('search')[1])
        url = 'https://google.com/search?q=' + voice_data.split('search')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')
            
    elif 'play spotify' in voice_data: 
        reply('Searching for ' + voice_data.split('play spotify')[1])
        url = 'https://open.spotify.com/' + voice_data.split('play spotify')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')
            
    elif 'w3 school' in voice_data:
        reply('Searching for ' + voice_data.split('w3 school')[1])
        url = 'https://www.w3schools.com/' + voice_data.split('w3school')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')
            
    elif 'learn python' in voice_data:
        reply('Searching for ' + voice_data.split('learn python')[1])
        url = 'https://www.learnpython.org/' + voice_data.split('learn python')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet') 
                    
    elif 'whatsapp' in voice_data: 
        reply('Searching for ' + voice_data.split('whatsapp')[1])
        url = 'https://web.whatsapp.com/' + voice_data.split('whatsapp')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')
            
    elif 'instagram' in voice_data:
        reply('Searching for ' + voice_data.split('instagram')[1])
        url = 'https://www.instagram.com/' + voice_data.split('instagram')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'twitter' in voice_data:
        reply('Searching for ' + voice_data.split('twitter')[1])
        url = 'https://twitter.com/i/flow/login' + voice_data.split('twitter')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'gmail' in voice_data:
        reply('Searching for ' + voice_data.split('gmail')[1])
        url = 'https://accounts.google.com/v3/' + voice_data.split('gmail')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'weather' in voice_data:
        reply('Searching for ' + voice_data.split('weather')[1])
        url = 'https://weather.com/en-IN' + voice_data.split('weather')[1]
        try:
                webbrowser.get().open(url)
                reply('This is what I found Sir')
        except:
                reply('Please check your Internet')
                
    elif 'kit' in voice_data:
        reply('Searching for ' + voice_data.split('kit')[1])
        url = 'https://kitcbe.com/' + voice_data.split('kit')[1]
        try:
                webbrowser.get().open(url)
                reply('This is what I found Sir')
        except:
                reply('Please check your Internet')

    elif 'swiggy' in voice_data:
        reply('Searching for ' + voice_data.split('swiggy')[1])
        url = 'https://www.swiggy.com/' + voice_data.split('swiggy')[1]
        try:
                webbrowser.get().open(url)
                reply('This is what I found Sir')
        except:
                reply('Please check your Internet')

    elif 'amazon' in voice_data:
        reply('Searching for ' + voice_data.split('amazon')[1])
        url = 'https://www.amazon.in/' + voice_data.split('amazon')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'netflix' in voice_data:
        reply('Searching for ' + voice_data.split('netflix')[1])
        url = 'https://www.netflix.com/in/' + voice_data.split('netflix')[1]
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif 'location' in voice_data:
        reply('Which place are you looking for ?')
        if app.ChatBot.userinputQueue.empty()==False:
            
            temp_audio =app.ChatBot.userinputQueue.get() 
            app.eel.addUserMsg(temp_audio)
        else:
            temp_audio = record_audio()
          
        reply('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            reply('This is what I found Sir')
        except:
            reply('Please check your Internet')

    elif ('bye' in voice_data) or ('by' in voice_data):
        reply("Good bye Sir! Have a nice day.")
        is_awake = False

    elif ('exit' in voice_data) or ('terminate' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
        app.ChatBot.close()
        #sys.exit() always raises SystemExit, Handle it in main loop
        sys.exit()
        
    
    # DYNAMIC CONTROLS
    elif 'launch gesture recognition' in voice_data:
        if Gesture_Controller.GestureController.gc_mode:
            reply('Gesture recognition is already active')
        else:
            gc = Gesture_Controller.GestureController()
            event =threading.Event()
            t =threading.Thread(target = gc.start)
            t.start()
            reply('Launched Successfully')
            event.set()

    elif ('stop gesture recognition' in voice_data) or ('top gesture recognition' in voice_data):
        if Gesture_Controller.GestureController.gc_mode:
            Gesture_Controller.GestureController.gc_mode = 0
            reply('Gesture recognition stopped')
        else:
            reply('Gesture recognition is already inactive')
        
    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied')
          
    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted')

    elif 'hand sign' in voice_data:
        import Main
        if Main.Function.gc_mode:
            reply('Hand sign is already active')
        else:
            gc = Main.Function()
            event = threading.Event()
            t =threading.Thread(target = gc.start)
            t.start()
            reply('Launched Successfully')
            event.set()

    elif ('stop hand sign' in voice_data) or ('top hand sign' in voice_data):
        if Main.Function.gc_mode:
           Main.Function.gc_mode = 0
           reply('Hand sign stopped')
        else:
            reply('Hand sign is already inactive')
        
    elif 'copy' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
        reply('Copied')
          
    elif 'page' in voice_data or 'pest'  in voice_data or 'paste' in voice_data:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
        reply('Pasted')    
        
    # File Navigation (Default Folder set to C://)
    elif 'list' in voice_data:
        counter = 0
        path = 'C://'
        files = listdir(path)
        filestr = ""
        for f in files:
            counter+=1
            print(str(counter) + ':  ' + f)
            filestr += str(counter) + ':  ' + f + '<br>'
        file_exp_status = True
        reply('These are the files in your root directory')
        app.ChatBot.addAppMsg(filestr)
        
    elif file_exp_status == True:
        counter = 0   
        if 'open' in voice_data:
            if isfile(join(path,files[int(voice_data.split(' ')[-1])-1])):
                os.startfile(path + files[int(voice_data.split(' ')[-1])-1])
                file_exp_status = False
            else:
                try:
                    path = path + files[int(voice_data.split(' ')[-1])-1] + '//'
                    files = listdir(path)
                    filestr = ""
                    for f in files:
                        counter+=1
                        filestr += str(counter) + ':  ' + f + '<br>'
                        print(str(counter) + ':  ' + f)
                    reply('Opened Successfully')
                    app.ChatBot.addAppMsg(filestr)
                    
                except:
                    reply('You do not have permission to access this folder')
                                    
        if 'back' in voice_data:
            filestr = ""
            if path == 'C://':
                reply('Sorry, this is the root directory')
            else:
                a = path.split('//')[:-2]
                path = '//'.join(a)
                path += '//'
                files = listdir(path)
                for f in files:
                    counter+=1
                    filestr += str(counter) + ':  ' + f + '<br>'
                    print(str(counter) + ':  ' + f)
                reply('ok')
                app.ChatBot.addAppMsg(filestr)
                   
    else: 
        reply('I am not functioned to do this !')

# ------------------Driver Code--------------------
event =threading.Event()
t1 = threading.Thread(target = app.ChatBot.start )
t1.start()

# Lock main thread until Chatbot has started
while not app.ChatBot.started:
    time.sleep(0.5)

wish()
voice_data = None
while True:

    if app.ChatBot.userinputQueue.empty() ==False:
        #take input from GUI
        voice_data = app.ChatBot.popUserInput()
        
        #reply(voice_data)
    else:
        #take input from Voice
        voice_data = record_audio()

        voice_data = record_audio()
    #process voice_data
    print("Comes here")
    if '' in voice_data:
        try:
            #Handle sys.exit()
            respond(voice_data)
        except SystemExit:
            reply("Exit Successfull")
            event.set()
            break
        except:
            #some other exception got raised
            print("EXCEPTION raised while closing.") 
            event.set()
            break 