# tests/test_02_get_pet.py

def test_get_pet(pet_page):
    pet_id = 1
    response = pet_page.get_pet(pet_id)
    print(response.json())  # Yanıt içeriğini yazdırın
    pet_page._verify_status_code(response, 200)  # Status doğrulama metodu kullanımı
    assert response.json()["name"] == "Buddy"
    assert response.json()["id"] == pet_id