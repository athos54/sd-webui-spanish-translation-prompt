import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("SpeechRecognition"):
    launch.run_pip("install SpeechRecognition", "sd-webui-spanish-translation-prompt requirement")
if not launch.is_installed("keyboard"):
    launch.run_pip("install keyboard", "sd-webui-spanish-translation-prompt requirement")
if not launch.is_installed("PyAudio"):
    launch.run_pip("install PyAudio", "sd-webui-spanish-translation-prompt requirement")