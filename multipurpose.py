import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'The download speed is {download_speed}')
print(f'The uplaod speed is {upload_speed}')                                          



import pyautogui
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")                                                 



import pyttsx3
engine = pyttsx3.init()
engine.say('This is a python example in MEDIUM')
engine.runAndWait()                                                             
