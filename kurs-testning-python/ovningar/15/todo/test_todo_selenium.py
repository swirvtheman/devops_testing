# test_todo_selenium.py
import pytest
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app_todo import app, todos


@pytest.fixture(scope="module")
def live_server():
    """Starta Flask i en bakgrundstråd."""
    todos.clear()
    thread = threading.Thread(
        target=lambda: app.run(port=5000, use_reloader=False)
    )
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Vänta på att servern startar
    yield "http://localhost:5000"


@pytest.fixture
def driver():
    """Starta en headless Chrome-instans."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(5)
    yield d
    d.quit()


@pytest.fixture(autouse=True)
def clean_todos():
    """Rensa todos före varje test."""
    todos.clear()

def test_page_loads(driver, live_server):
    """Startsidan laddas med rätt rubrik."""
    driver.get(live_server)
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert h1.text == "Mina uppgifter"