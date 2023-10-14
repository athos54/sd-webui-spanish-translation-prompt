import os
import json
import speech_recognition as sr

config_file_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

config_file_path = os.path.normpath(config_file_path)

with open(config_file_path, 'r') as file:
    loaded_dictionary = json.load(file)


class SpeechListener:
    def __init__(self):
        self.result = None
        self.stop_listening = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def callback(self, recognizer, audio):
        try:
            self.result = recognizer.recognize_google(
                audio, language=loaded_dictionary["voice_detector"])
            print("You said: " + self.result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")
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
