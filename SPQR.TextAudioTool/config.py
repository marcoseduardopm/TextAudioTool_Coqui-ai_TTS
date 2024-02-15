##======= CUDA_SUPPORT =======##
#Leave as "-1" if you want to use your CPU, "0" if you want to use your first GPU, and "1" if you want to use your second GPU (in case you have 2 GPUs)
USE_GPU = "-1"
#If using GPU, which version to install?  See https://pytorch.org/. Change only if it doesn't work after a few attempts.
TORCH_GPU_INSTALL = "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118"

#having problems with cuda (to use GPU) not being available? Try to force reinstall once.
TORCH_FORCE_REINSTALL = False

##======= COQUI_SUPPORT =======##
USE_COQUI_TTS = True

##======= SPEECH TO TEXT =======##

# The model used to process the speech into text. Larger models are better at detecting what the voice is saying, however they are considerably slower. The first time running after changing this the script will download the new whisper model if it's not already downloaded. Default is "tiny". Values: tiny, base, small, medium, large (https://github.com/openai/whisper#available-models-and-languages)
STT_MODEL = "tiny"
# The language used to detect words that are spoken. Default is "english". Other languages available and how good the model is at detecting them can be found here: https://github.com/openai/whisper#available-models-and-languages. E.g. "spanish", "japanese", etc
STT_LANGUAGE = "english"
# The time limit in seconds after which the speech recording ends even if there's still voice commands being sent. Default is 15. After 15 seconds the recording stops and the voice is processed to text.
STT_TIME_LIMIT = 15




##======= TEXT TO SPEECH  =======##
# the speech rate for the offline local voices in words per minute. Default value is 170
TTS_LOCAL_SPEECH_RATE = 170




##======= OTHER=======##

# used to print more log info
DEBUG = False
