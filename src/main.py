from utils.request_engine import RequestEngine
from utils.response_handler import ResponseHandler
from utils.parser import Parser
import requests

def main():


    url = "https://www.daad.de/en/studying-in-germany/universities/all-degree-programmes/"

    request_engine = RequestEngine()
    response_handler = ResponseHandler()
    parser = Parser(url)

    try:
        response = request_engine.make_request(url)

        if isinstance(response , str):
            print(f"Error making request: {response}")
            return

        print(f"Request successfull...")
        print(f"Request status : {response}")

    finally:
        request_engine.close()


    validated_response = response_handler.response_validator(response)

    if not isinstance(validated_response , requests.Response):
        print(f"Error : {validated_response}")
        return

    print(f"Html structure successfully recieved.")
    print("\n")

    parsed_data = parser.parse(validated_response.text)

    for data in parsed_data:

        print(data)


if __name__ == "__main__":

    main()