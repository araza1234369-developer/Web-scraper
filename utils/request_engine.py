import requests

class RequestEngine():

    def __init__(self , timeout : int = 10):
        self.__session = requests.Session()
        self.__timeout = timeout


    def make_request(self , url) -> requests.Response | str: 

        try:
           response = self.__session.get(url , timeout = self.__timeout)
           response.raise_for_status()

           return response

        except requests.RequestException as error:
          error_message = str(error)
          return error_message


    def close(self):
       self.__session.close()