import contextlib

import gradio as gr
from modules import scripts
from modules import script_callbacks
from translate_functions import translate_text
def send_text_to_prompt(text,box):
    return translate_text(text)

class ExampleScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "Athos extension"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("Athos extension", open=False):
                text_to_be_sent = gr.TextArea(placeholder='Escribe tu texto en español', variant='primary')
                send_text_button = gr.Button(value='Enviar', variant='primary')

        with contextlib.suppress(AttributeError):  # Ignore the error if the attribute is not present
            if is_img2img:
                # Bind the click event of the button to the send_text_to_prompt function
                # Inputs: text_to_be_sent (textbox), self.boxxIMG (textbox)
                # Outputs: self.boxxIMG (textbox)

                send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxxIMG], outputs=[self.boxxIMG])
            else:
                # Bind the click event of the button to the send_text_to_prompt function
                # Inputs: text_to_be_sent (textbox), self.boxx (textbox)
                # Outputs: self.boxx (textbox)
                send_text_button.click(fn=send_text_to_prompt, inputs=[text_to_be_sent, self.boxx], outputs=[self.boxx])

        return [text_to_be_sent, send_text_button]

    def after_component(self, component, **kwargs):
        #https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/7456#issuecomment-1414465888 helpfull link
        # Find the text2img textbox component
        if kwargs.get("elem_id") == "txt2img_prompt": #postive prompt textbox
            self.boxx = component
        # Find the img2img textbox component
        if kwargs.get("elem_id") == "img2img_prompt":  #postive prompt textbox
            self.boxxIMG = component

        #this code below  works aswell, you can send negative prompt text box,provided you change the code a little
        #switch  self.boxx with  self.neg_prompt_boxTXT  and self.boxxIMG with self.neg_prompt_boxIMG

        #if kwargs.get("elem_id") == "txt2img_neg_prompt":
            #self.neg_prompt_boxTXT = component
        #if kwargs.get("elem_id") == "img2img_neg_prompt":
            #self.neg_prompt_boxIMG = component







