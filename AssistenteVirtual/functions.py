import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer
from shared import language, tld  # Importar variáveis compartilhadas


    
def get_audio(language):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            if language == "pt":
                lang = "pt-br"
            else:
                lang = "en-US"
            said = r.recognize_google(audio, language=lang)
            print(said)
        except sr.UnknownValueError:
            print("Repita")
        except sr.RequestError:
            print("Repita, serviço não disponivel")
    return said.lower()
#speak converted audio to text
def speak(text, idioma):
    tts = gTTS(text=text, lang=idioma, tld=tld)
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)
#function to respond to commands
def respond(text, idioma):
    language = idioma
    print("Texto do audio captado: " + text)
    if 'youtube' in text:
        speak("What do you want to search for", idioma) if language == "en"  else  speak("O que você quer procurar?", idioma)
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"This is what I found about {keyword} on youtube", idioma) if language == "en" else speak(f"Aqui está o que eu encontrei para {keyword} no youtube", idioma)
    elif ('search' if language == "en" else 'pesquise') in text:
        speak("What do you want to search for?", idioma) if language == "en" else speak("O que você quer pesquisar?", idioma)
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia", idioma) if language == "en" else speak("De acordo com a wikipedia", idioma)
            print(result)
            speak(result, idioma)
    elif 'joke' in text:
        speak(pyjokes.get_joke(), idioma)
    elif ('empty recycle bin' if language == "en" else 'esvaziar lixeira') in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle bin emptied", idioma) if language == "en" else speak("Lixeira esvaziada", idioma)
    elif ('what time' if language == "en" else 'que horas') in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime, idioma)
    elif ('play music' if language == "en" else 'tocar música') in text or 'play song' in text:
        speak("Now playing...", idioma) if language == "en" else speak("Agora tocando música...", idioma)
        music_dir = "C:\\Users\\unico\\Music\\baladag4.com.br_64719" #add your music directory here..
        songs = os.listdir(music_dir)
        print(songs)
        playmusic(music_dir + "\\" + songs[0])
    elif ('stop music' if language == "en" else 'parar música') in text:
        speak("Stopping playback.", idioma) if language == "en" else speak("Parando música", idioma)
        stopmusic()
    elif ('quit' if language == "en" else 'desconectar') in text:
        speak("Goodbye, till next time", idioma) if language == "en" else speak("Tchau, até a proxima", idioma)
        exit()
#Tocar musica
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
#Parar musica
def stopmusic():
    mixer.music.stop()
