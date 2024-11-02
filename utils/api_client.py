
import requests

class APIClient:
    BASE_URL = "https://petstore.swagger.io/v2"

    @staticmethod
    def post(endpoint, data):
        response = requests.post(f"{APIClient.BASE_URL}{endpoint}", json=data)
        return response

    @staticmethod
    def get(endpoint):
        response = requests.get(f"{APIClient.BASE_URL}{endpoint}")
        return response

    @staticmethod
    def put(endpoint, data):
        response = requests.put(f"{APIClient.BASE_URL}{endpoint}", json=data)
        return response

    @staticmethod
    def delete(endpoint):
        response = requests.delete(f"{APIClient.BASE_URL}{endpoint}")
        return response