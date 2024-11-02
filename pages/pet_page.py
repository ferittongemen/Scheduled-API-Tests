# pages/pet_page.py

from utils.api_client import APIClient

class PetPage:
    def __init__(self):
        self.endpoint = "/pet"

    def create_pet(self, pet_data):
        """Yeni bir pet yaratır ve yanıtı döner."""
        response = APIClient.post(self.endpoint, pet_data)
        self._verify_status_code(response, 200)
        return response

    def get_pet(self, pet_id):
        """Belirli bir pet'i ID ile alır."""
        response = APIClient.get(f"{self.endpoint}/{pet_id}")
        return response

    def update_pet(self, pet_data):
        """Var olan bir pet'i günceller."""
        response = APIClient.put(self.endpoint, pet_data)
        self._verify_status_code(response, 200)
        return response

    def delete_pet(self, pet_id):
        """Belirli bir pet'i ID ile siler."""
        response = APIClient.delete(f"{self.endpoint}/{pet_id}")
        self._verify_status_code(response, 200)
        return response

    def _verify_status_code(self, response, expected_status):
        """Yanıt durum kodunu doğrular."""
        assert response.status_code == expected_status, (
            f"Beklenen durum kodu {expected_status}, ancak {response.status_code} alındı."
        )