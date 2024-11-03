# tests/test_01_create_pet.py

def test_create_pet(pet_page):
    pet_data = {
        "id": 2,
        "category": {"id": 2, "name": "Cats"},
        "name": "Whiskers",
        "status": "available"
    }
    response = pet_page.create_pet(pet_data)
    assert response.json()["name"] == "Whiskers"