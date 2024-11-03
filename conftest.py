import os
import pytest
import requests
from pages.pet_page import PetPage
import os


# Slack Webhook URL'sini ortam değişkeninden alın
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
print("SLACK_WEBHOOK_URL mevcut:", SLACK_WEBHOOK_URL is not None)
@pytest.fixture(scope="module")
def pet_page():
    return PetPage()

@pytest.fixture(scope="function", autouse=True)
def setup_pet(pet_page):
    pet_data = {
        "id": 1,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "status": "available"
    }
    # Her testten önce pet yarat
    pet_page.create_pet(pet_data)

def pytest_runtest_makereport(item, call):
    """Her bir test sonucu için Slack bildirim gönderir."""
    if call.when == "call":
        if call.excinfo is not None:  # Test başarısız ise
            send_slack_notification(item.nodeid, f"Başarısız: {call.excinfo}")
        else:  # Test başarılı ise
            send_slack_notification(item.nodeid, "Başarılı")

def pytest_sessionfinish(session, exitstatus):
    """Tüm testler tamamlandıktan sonra genel bir sonuç bildirimi gönderir."""
    message = f"Test oturumu tamamlandı. Çıkış durumu: {exitstatus}."
    if exitstatus == 0:
        message += "\nTüm testler başarıyla geçti."
    else:
        message += "\nBazı testler başarısız oldu."

    send_slack_notification("Toplu Test Sonucu", message)

def send_slack_notification(test_name, message_text):
    """Slack'e bildirim gönderir."""
    if SLACK_WEBHOOK_URL:
        message = {
            "text": f"{test_name}\nDurum: {message_text}"
        }
        response = requests.post(SLACK_WEBHOOK_URL, json=message)
        if response.status_code != 200:
            print("Slack bildirimi gönderilemedi.")
        else:
            print("Slack bildirimi başarıyla gönderildi.")
    else:
        print("Slack Webhook URL tanımlı değil.")