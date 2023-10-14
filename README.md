# Spanish to English Prompt Translation

Simply open the Translation Extension accordion, type your text, and wait until the prompt box is updated.

This extension uses LibreTranslate: [LibreTranslate GitHub](https://github.com/LibreTranslate/LibreTranslate)

## How to Use

This extension has two features:

### Native Text to English

You can type text in your native language and press "Send to Prompt." It will **replace** your current prompt with the translated text to English.

### Speech to Text

Click the "Listen" button, speak, and then press the "Stop" button. In a few seconds, what you said will be written in the native language textbox. After that, you can click "Send to Prompt" to translate it to English.

## How It Works

The translation API used for this extension is from this project: [LibreTranslate Locales](https://github.com/LibreTranslate/LibreTranslate/tree/main/libretranslate/locales). You can deploy your own instance and change the URL in the config file. The key in the config file is `translate_api_url`.

## Configuration

The configuration of this extension is under the `scripts/config.json` file. You can modify this file according to your language.

To see translation language options, look at [LibreTranslate Locales](https://github.com/LibreTranslate/LibreTranslate/tree/main/libretranslate/locales).

To see voice recognition options, refer to [Google Cloud Speech-to-Text Supported Languages](https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages?hl=es-419).

## Others

Feel free to make a pull request if you want to improve the extension.
