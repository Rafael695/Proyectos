from time import strftime
from types import new_class
from typing import Text, TextIO
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
import time
import pywhatkit


from urllib.request import urlopen
from wikipedia.wikipedia import languages, search


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Hora_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak('La hora actual es')
    speak(Time)

def Fecha_():
    año = datetime.datetime.now().year
    mes = datetime.datetime.now().month
    dia = datetime.datetime.now().day
    speak('El día de hoy es')
    speak(dia)
    speak(mes)
    speak(año)

def wishme():
    speak("Bienvenido de vuelta Amo Rafael")
    Hora_()
    Fecha_()

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("¡Buenos días señor!")
    elif hour>=12 and hour<18:
        speak("¡Buenas tardes señor!")
    elif hour>=18 and hour<=24:
        speak("¡Buenas noches señor!")
    else:
        speak("Que descance señor")

    speak("Antonela está a sus servicios. Porfavor digame, ¿cómo puedo ayudarle?")   
 

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Lo escucho.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    

    try:
        print("Reconociendo.....")
        query = r.recognize_google(audio,language='es-MX')
        print(query)
    except Exception as e:
        print(e)
        print("Me lo podría repetir una vez más por favor")
        return "None"
    return query

def enviesuncorreo(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #para esta funcion, debes tener desactivada la seguridad in tu gmail el cual vas a usar como el enviador
    server.login('zmdlmend@gmail.com','fglyvgbefnrgwsbr')
    server.sendmail('zmdlmend@gmail.com',to,content)
    server.close()

def captura():
    img = pyautogui.screenshot()
    img.save(r'C:/Users/Zmade/Downloads/screenshot.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('El CPU está en'+usage)

    battery = psutil.sensors_battery()
    speak('La bateria está en')
    speak(battery.percent)
    speak('porciento')

def joke():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        if 'dime la hora' in query:
            Hora_()

        elif 'dime la fecha' in query:
            Fecha_()

        elif 'modo de reposo' in query:
            speak('Esta bien, en ese caso señor creo que tomaré una siesta.')
            quit()
        
        elif 'wikipedia' in query:
            speak("Buscando.....")
            query=query.replace('wikipedia','')
            resultado=wikipedia.summary(query,sentece=3)
            speak('segun wikipedia')
            print(resultado)
            speak(resultado)
        
        elif 'envíes un correo' in query:
            try:
                speak("¿Qué deberia decir?")
                content=TakeCommand()
                #provide reciever email address
                #speak("¿Señor,a que correo envio esta informacion?")
                #reciever=TakeCommand()
                speak("Señor, ingrese por favor el correo electronico al que enviaré la información.")
                print('A continuación ingrese el correo electronico')              
                reciever=input()
                #reciever ="ciindy.zf97@gmail.com" 
                to = reciever
                print(reciever)
                enviesuncorreo(to,content)
                speak(content)
                speak('El correo a sido enviado señor.')
            
            except Exception as e:
                print(e)
                speak("No se pudo enviar el correo electronico.")
        
        elif 'una página' in query:
            speak('¿Qué página debo buscar señor?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        

        elif 'en youtube' in query:
            speak('¿Qué debo de buscar señor?')
            search_Term = TakeCommand().lower() 
            speak('Muy bien me dirijo a youtube')
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'en google' in query:
            speak('¿Qué debo de buscar señor?')
            search_Term = TakeCommand().lower()
            speak('Buscando...')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' in query:
            cpu()
        
        elif 'broma' in query:
            joke()

        elif 'word' in query:
            speak('Abriendo el word.....')
            ms_word  = r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE'
            os.startfile(ms_word)

        elif 'powerpoint' in query:
            speak('Abriendo el powerpoint.....')
            ms_powerpoint = r'C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE'
            os.startfile(ms_powerpoint)
        
        elif 'visual studio code' in query:
            speak('Abriendo el visual studio code.....')
            ms_code = r'C:\Users\Zmade\AppData\Local\Programs\Microsoft VS Code\Code.exe'
            os.startfile(ms_code)   

        elif 'escribe una nota' in query:
            speak('¿Qué deberia de escribir, señor?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("señor, ¿quiere que incluya la fecha?")
            ans = TakeCommand()
            if 'sí' in ans or 'seguro' in ans or 'si' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Ya agregé la fecha y terminé de tomar nota, señor')
            else:
                speak('Muy bien ya anote lo que me pidió señor')
                file.write(notes)
        
        elif 'muéstrame las notas' in query:
            speak('mostrando notas....')
            file = open('notes.txt','r')
            speak("La nota que me pidio escribir señor dice..."+ file.read())
            #print(file.read())

        elif 'captura de pantalla' in query:
            captura()
            speak('La captura de pantalla ya a sido tomada señor')

        elif 'música' in query:
            songs_dir = r'C:\Users\Zmade\OneDrive\Escritorio\Música'
            music = os.listdir(songs_dir)
            speak('Cuál reprodusco señor?')
            speak('seleccione un número...')
            ans = TakeCommand().lower()
            while('la número' not in ans and ans != 'aleatorio' and ans != 'tu elige' and ans != 'tú elige' and ans != 'tú eliges' and ans != 'tu eliges'):
                speak('No entendí. ¿Lo puede repetir una vez más?')
                ans = TakeCommand().lower()
            if 'la número' in ans:
                nom = int(ans.replace('la número',''))
            elif 'aleatorio' or 'tu elige' or 'tú elige' or 'tú eliges' or 'tu eliges' in ans:
                nom = random.randint(1,111)

            os.startfile(os.path.join(songs_dir,music[nom]))

        elif 'recuerdes esto' in query:
            speak('¿Qué debó de recordar?')
            memory = TakeCommand()
            speak('Me pediste que recordara esto.....'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'recuerdas algo' in query:
            remember = open('memory.txt','r')
            speak('me pediste que recordara esto.....'+remember.read())

        elif 'noticias' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=881c726423404be9b9f5c8f310956e8b")
                data = json.load(jsonObj)
                i = 1

                speak('Aquí están algunos de los principales titulares de la industria del entretenimiento')
                print('==================TOP HEADLINES================='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1
                
            except Exception as e:
                    print(str(e))

        elif 'dónde está' in query:
            query = query.replace("dónde está","")
            location = query
            speak("Muy bien señor ahora le diré donde esta"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'descansa' in query:
            try:
                speak('¿Por cuantos segundos quiere que descanse y no escuche lo que ordenes señor?')
                ans = int(TakeCommand())
                time.sleep(ans)
                print(ans)

            except Exception as e:
                print(e)
                speak('No se pudo efectuar el comando intentelo de nuevo')    

        elif 'whatsapp' in query:
            try:
                speak('¿A que numero debo de mandar el mensaje señor?')
                ans = TakeCommand()
                speak('¿Que quiere que le escriba señor?')
                mess = TakeCommand()
                speak('digame la hora del envio')
                re1 = int(TakeCommand())
                speak('digame los minutos del envio')
                re2 = int(TakeCommand())
                pywhatkit.sendwhatmsg("+52"+ans,mess,re1,re2)
                speak('Mensaje enviado')
            
            
            except:
                speak('Ocurrio un error')

        elif 'cerrar sesión' in query:
            os.system("shutdown -l")
        elif 'reiniciar' in query:
            os.system("shutdown /r /t 1")
        elif 'apagar' in query:
            os.system("shutdown /s /t 1")