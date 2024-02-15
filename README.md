# About TextAudioTool

This repository is a Fork of the (https://github.com/5PQR/TextAudioTool). The original TextAudioTool is a very quick & simple Python tool that creates local API endpoints for TTS &amp; STT. For more information, please see to original repository. 

The information present in this document is mostly related to the changes made in comparison with the original repository.

List of Changes:
- Allows the use of Coqui-AI TTS as the local speech generation. New voices can be easily added by putting an audio file at audio\voices. For more information about Coqui-AI TTS, please see (https://github.com/coqui-ai/TTS);
- Added Cuda support to allow the user to choose between CPU, or one of the installed graphic cards.
- Removed some application-specific files;
- Other minor code changes.

The Coqui-ai is select as default as the TTS engine. To change is SPQR.TextAudioTool/config.py, which has the following new options:
- USE_COQUI_TTS -> True or False, indicating if Coqui-AI should be used;
- USE_GPU -> "-1" means CPU, "0" means the first GPU, and "1" mean your second GPU;
- TORCH_GPU_INSTALL -> Changed only if necessary. The pip install command for  Torch to allow the use of GPU;
- TORCH_FORCE_REINSTALL -> If you are unable to make Cuda work, try setting this to True once.

Note that you should at least try to set USE_GPU as "0" (meaning first GPU) due to performance reasons. If your video card gets out of memory, then you should consider going back to "-1" (which means CPU).


Please note that you might need to run "SPQR.TextAudioTool - (standalone).bat" a few times during the installation and after changing the parameters at "SPQR.TextAudioTool/config.py". If you get an error, the first thing to do is try rerunning it.


# License
AGPL license because that script was based on an agpl licensed script.
The Coqui-AI TTS model has its own license terms related to its model. Please see https://github.com/coqui-ai/TTS.

# Credits
* To the main author of the original repository (https://github.com/5PQR/TextAudioTool)
* Coqui-AI TTS (https://github.com/coqui-ai/TTS)
* The installer script (SPQR.TextAudioTool.bat) that downloads and installs miniconda is based on oobabooga's install script made for https://github.com/oobabooga/one-click-installers , I only changed the python script it loads
