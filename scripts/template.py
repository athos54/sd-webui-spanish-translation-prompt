import contextlib
import gradio as gr
from modules import scripts
from modules import script_callbacks
from scripts.translate_functions import translate_text_api
from scripts.listen import SpeechListener
import os
import json

ruta_al_archivo_dict = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

ruta_al_archivo_dict = os.path.normpath(ruta_al_archivo_dict)

with open(ruta_al_archivo_dict, 'r') as archivo:
    diccionario_cargado = json.load(archivo)

listener = SpeechListener()
isListening = False


def send_text_to_prompt(text, box):
    return translate_text_api(text)


def startListen():
    global isListening
    if isListening == False:
        isListening = True
        listener.start()
    return "Listening..."


def stopListen():
    global isListening
    if isListening == True:
        isListening = False
        listener.stop()
        result = listener.get_result()

    return ["Stopped", result]


class ExampleScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "Translation extension"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("Translation extension", open=diccionario_cargado["is_accordion_auto_opened"]):
                with gr.Row():
                    with gr.Column(scale=2):
                        startListenBtn = gr.Button(
                            "Listen", variant='primary')
                    with gr.Column(scale=2):
                        stopListenBtn = gr.Button("Stop")
                with gr.Row():
                    statusLabel = gr.Label(
                        value='Stopped', label="Listen status")
                with gr.Row():
                    text_to_be_sent = gr.TextArea(
                        label="Prompt on native language",
                        placeholder='Write your text according to your configuration language', variant='primary')
                with gr.Row():
                    send_text_button = gr.Button(
                        value='Send to prompt', variant='primary')

                startListenBtn.click(startListen, outputs=[statusLabel])
                stopListenBtn.click(stopListen, outputs=[
                                    statusLabel, text_to_be_sent])

        with contextlib.suppress(AttributeError):
            if is_img2img:
                send_text_button.click(fn=send_text_to_prompt, inputs=[
                                       text_to_be_sent, self.boxxIMG], outputs=[self.boxxIMG])
            else:
                send_text_button.click(fn=send_text_to_prompt, inputs=[
                                       text_to_be_sent, self.boxx], outputs=[self.boxx])

        return [text_to_be_sent, send_text_button]

    def after_component(self, component, **kwargs):
        if kwargs.get("elem_id") == "txt2img_prompt":  # positive prompt textbox
            self.boxx = component
        if kwargs.get("elem_id") == "img2img_prompt":  # positive prompt textbox
            self.boxxIMG = component
