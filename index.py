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