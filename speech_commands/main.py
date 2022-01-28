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
        print("")
    except sr.RequestError as e:
        print("")

    sleep(1)
