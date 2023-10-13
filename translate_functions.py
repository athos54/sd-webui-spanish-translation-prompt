from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

def translate_text(text):
    print("text to translate: " + text)
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    # translate to French
    tokenizer.src_lang = "es_XX"
    encoded_text = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_text,
        forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
    )
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    print("translation: " + translation[0])
    return translation[0]
def translate2(text):
    print("hola2 " + text)
# Ejemplo de uso
# article_hi = "me voy a ir a un lago con un barco, el lago está un poco pasado las montañas, ¿te gustaría venir conmigo?"
# translation_hi = translate_text(article_hi)
# print(translation_hi)
