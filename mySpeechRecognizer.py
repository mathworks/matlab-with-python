# Python speech recognition code using CMU PocketSphinx
# Source: https://pypi.python.org/pypi/SpeechRecognition/

import speech_recognition as sr


# Takes an audio signal (in uint8 format), along with its sampling frequency and channel width, and outputs detected text and success flag.
def audioToText(audio,freq,width):

    # Create an AudioData object from the input signal
    audioData = sr.AudioData(bytes(audio),freq,width)
    
    # Create a recognizer instance and attempt to recognize text
    myRec = sr.Recognizer()
    try:
        recText = myRec.recognize_sphinx(audioData)
        successFlag = True
    except:
        recText = ""
        successFlag = False

    # Return recognized text and success flag
    return [recText,successFlag]


# Directly listens to the microphone and returns detected text.
def speechToText():

    # First, get the audio data from the microphone
    myRec = sr.Recognizer()
    myRec.energy_threshold = 1000 # Increase to reduce noise
    
    with sr.Microphone() as source:
        audioData = myRec.listen(source)

    try:
        # Call speech recognizer
        return myRec.recognize_sphinx(audioData)

    except:
        return ""
    