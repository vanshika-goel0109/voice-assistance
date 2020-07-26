
import speech_recognition as sr
import webbrowser as wb

r2 = sr.Recognizer()

with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source, duration=5)
    print('[search: google search: youtube ]')
    print('speak now...')
    audio = r2.listen(source)
    print(r2.recognize_google(audio))

def func():
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source, duration=5)
        print('search your query')
        audio = r2.listen(source)

    get = r2.recognize_google(audio)
    print(get)
    wb.get().open_new(url + get)

if 'Google' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.google.com/search?q='
    func()
elif 'Yahoo' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.yahoo.com/search?q='
    func()





















