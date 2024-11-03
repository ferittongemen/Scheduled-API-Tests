# tests/test_03_update_pet.py

def test_update_pet(pet_page):
    pet_data = {
        "id": 1,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "status": "sold"
    }
    response = pet_page.update_pet(pet_data)
    assert response.json()["status"] == "sold"