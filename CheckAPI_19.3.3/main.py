# Проверка работы основных методов API
import requests
import json


class CheckPetStoreAPI:
    """апи проверка статус-кода к веб приложению Pet Store"""

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.headers = {'accept': 'application/json',
                        'Content-Type': 'application/json'}

    def check_get_pets(self) -> json:
        status = 'available'
        res_get = requests.get(f'{self.base_url}/pet/findByStatus?status={status}',
                               headers=self.headers)
        return print(f'GET код: {res_get.status_code}\n')

    def check_post_pet(self) -> json:
        data = {"id": 9223366554433221111, "category": {"id": 0, "Cat": "string"},
                "name": "Barsik", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
                "status": "available"}
        data = json.dumps(data)
        res_post = requests.post(f'{self.base_url}/pet', headers=self.headers, data=data)
        return print(f'POST код: {res_post.status_code}\n')

    def check_put_pet(self) -> json:
        data = {"id": 9223366554433221111, "category": {"id": 0, "Cat": "string"},
                "name": "New_Barsik", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
                "status": "available"}
        res_put = requests.put(f'{self.base_url}/pet', headers=self.headers, json=data)
        return print(f'PUT код: {res_put.status_code}\n')

    def check_delete_pet(self) -> json:
        res_delete = requests.delete(f'{self.base_url}/pet/{9223366554433221111}',
                                     headers=self.headers)
        return print(f'DELETE код: {res_delete.status_code}\n')
