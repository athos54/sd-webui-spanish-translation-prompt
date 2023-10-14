import gradio as gr
from modules import scripts
from scripts.translate_functions import translate_text_api
from scripts.listen import SpeechListener
import os
import json
import contextlib

config_file_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.json').replace("\\", "/")

config_file_path = os.path.normpath(config_file_path)

with open(config_file_path, 'r') as file:
    loaded_dictionary = json.load(file)

listener = SpeechListener()
is_listening = False


def send_text_to_prompt(text, box):
    return translate_text_api(text)


def start_listen():
    global is_listening
    if not is_listening:
        is_listening = True
        listener.start()
    return "Listening..."


def stop_listen():
    global is_listening
    if is_listening:
        is_listening = False
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
            with gr.Accordion("Translation extension", open=loaded_dictionary["is_accordion_auto_opened"]):
                with gr.Row():
                    with gr.Column(scale=2):
                        start_listen_btn = gr.Button(
                            "Listen", variant='primary')
                    with gr.Column(scale=2):
                        stop_listen_btn = gr.Button("Stop")
                with gr.Row():
                    status_label = gr.Label(
                        value='Stopped', label="Listen status")
                with gr.Row():
                    text_to_be_sent = gr.TextArea(
                        label="Prompt on native language",
                        placeholder='Write your text according to your configuration language', variant='primary')
                with gr.Row():
                    send_text_button = gr.Button(
                        value='Send to prompt', variant='primary')

                start_listen_btn.click(start_listen, outputs=[status_label])
                stop_listen_btn.click(stop_listen, outputs=[
                                      status_label, text_to_be_sent])

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
