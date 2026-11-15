from utils.request_engine import RequestEngine
from utils.response_handler import response_validator
from utils.parser import parser
import requests

def main():

    url = "https://www.daad.de/en/studying-in-germany/universities/all-degree-programmes/"

    request_engine = RequestEngine()

    try:
        response = request_engine.make_request(url)

        if isinstance(response , str):
            print(f"Error making request: {response}")
            return

        print(f"Request successfull...")

    finally:
        request_engine.close()


    valid_html = response_validator(response)

    if valid_html is not None:
        print(f"Html structure recieved successfully.")

    else:
        print(f"Html structure is not valid.")



if __name__ == "__main__":

    main()