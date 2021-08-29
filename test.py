import speech_recognition as sr
import time
# Library home: https://pypi.org/project/SpeechRecognition/
# testing out SpeachRecognition functions https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
# also referto: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# valuable further examples:https://github.com/Uberi/speech_recognition/blob/master/examples/background_listening.py

TALKER_CADENCE_PAUSE_THRESHOLD_SECONDS = 1

file_path = "C:/temp/audio_dump/test"

#This is our microphone
mic = sr.Microphone()
print("Microphone identified")
#This is the recognizer class
r = sr.Recognizer()
print("Recognizer initiated")

with mic as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    r.pause_threshold = TALKER_CADENCE_PAUSE_THRESHOLD_SECONDS
with mic as source:
    #We are trying to clean the ambient noise
    for i in range(5):
        print("Recording-0"+str(i))
        try:
            audio_data = r.listen(source) #, phrase_time_limit=1
            #audio_data = r.record(source, duration=3)
            text = r.recognize_google(audio_data)
            file1 = open(file_path+"-"+str(i)+".txt","w")
            file1.write(text)
            file1.close()
        except sr.WaitTimeoutError:
            print("No more speach, I assume")
        except sr.UnknownValueError:
            print("Cannot interpret input")
