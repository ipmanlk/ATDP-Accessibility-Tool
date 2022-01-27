import speech_recognition as sr
import pyautogui

from time import sleep

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        gvc_output = r.recognize_google(audio)
        text = gvc_output.strip()

        print("Recognized text {0}".format(text))

        if text == "click":
            pyautogui.click()

        if text == "double click":
            pyautogui.doubleClick()

        if text == "right click":
            pyautogui.rightClick()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    sleep(1)
