# tests/test_04_delete_pet.py

from pages.pet_page import PetPage

def test_delete_pet():
    pet_page = PetPage()
    pet_data = {
        "id": 1,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "status": "available"
    }
    # Test için pet yarat
    pet_page.create_pet(pet_data)

    # Silme işlemini gerçekleştir ve doğrula
    response = pet_page.delete_pet(1)
    assert response.status_code == 200

    # Silindikten sonra kontrol için tekrar GET isteği
    get_response = pet_page.get_pet(1)
    pet_page._verify_status_code(get_response, 404)  # Silinen pet'in 404 durumunu doğrula