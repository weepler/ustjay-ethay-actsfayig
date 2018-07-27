import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()
    piglatinize_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'

    # Send a request to https://hidden-journey-62459.herokuapp.com/
    # should be a POST request, and it should have form data with 'input_test'
    # of the fact that we scraped and use the keyword argument 'follow_redirects=FALSE'
    # when making your request so that you can capture and analyse the redirect respose

    response = requests.post(
               piglatinize_url,
               data = {'input_text': fact},
               allow_redirects = False,
               )

    # if response.status_code != 302:
    #     raise Exception
    # then get the 'location' header from the response.
    # looks like:
    # location_header = response ....response

    print(response.status_code)
    print(response.headers)


    location_header = response.headers['Location']

    return "<a href='{}'>{}</a>".format(location_header,location_header)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

