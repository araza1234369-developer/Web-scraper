import requests

class ResponseHandler():

    def response_validator(self , response : requests.Response) -> requests.Response | str:

        if not isinstance(response , requests.Response):
            return f"Invalid response object recieved."

        html_content = response.text.lstrip().lower()

        if html_content.startswith("<!doctype html>") or html_content.startswith("<html>"):
            return response

        return f"Invalid html structure recieved."