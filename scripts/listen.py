import time
import speech_recognition as sr
import sys
import os
import json

ruta_al_archivo_dict = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

ruta_al_archivo_dict = os.path.normpath(ruta_al_archivo_dict)

with open(ruta_al_archivo_dict, 'r') as archivo:
    diccionario_cargado = json.load(archivo)


class SpeechListener:
    def __init__(self):
        self.result = None
        self.stop_listening = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def callback(self, recognizer, audio):
        try:
            self.result = recognizer.recognize_google(
                audio, language=diccionario_cargado["voice_detector"])
            print("Has dicho: " + self.result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print(e)

    def start(self):
        print("Start listening")
        self.stop_listening = self.recognizer.listen_in_background(
            self.microphone, self.callback)

    def stop(self):
        print("Stop function")
        if self.stop_listening is not None:
            self.stop_listening()
            self.stop_listening = None

    def get_result(self):
        return self.result
