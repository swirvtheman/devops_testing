# pages/todo_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TodoPage:
    """Page Object för TODO-sidan."""

    # Selektorer — samlade på ett ställe
    HEADING = (By.TAG_NAME, "h1")
    TASK_INPUT = (By.ID, "task-input")
    ADD_BUTTON = (By.ID, "add-btn")
    TODO_LIST = (By.ID, "todo-list")
    TODO_ITEMS = (By.CSS_SELECTOR, "#todo-list li")
    COUNT_TEXT = (By.ID, "count")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def navigate(self):
        """Gå till startsidan."""
        self.driver.get(self.base_url)
        return self

    def get_heading(self):
        """Returnera sidans rubrik."""
        return self.driver.find_element(*self.HEADING).text

    def add_todo(self, task):
        """Lägg till en uppgift."""
        input_field = self.driver.find_element(*self.TASK_INPUT)
        input_field.clear()
        input_field.send_keys(task)
        self.driver.find_element(*self.ADD_BUTTON).click()
        return self

    def get_todo_items(self):
        """Returnera alla TODO-element."""
        return self.driver.find_elements(*self.TODO_ITEMS)

    def get_todo_texts(self):
        """Returnera texten för alla uppgifter."""
        items = self.get_todo_items()
        return [item.find_element(By.CLASS_NAME, "task-text").text
                for item in items]

    def toggle_todo(self, todo_id):
        """Toggla klar/ej klar för en uppgift."""
        selector = (By.CSS_SELECTOR, f"[data-testid='toggle-{todo_id}']")
        self.driver.find_element(*selector).click()
        return self

    def delete_todo(self, todo_id):
        """Radera en uppgift."""
        selector = (By.CSS_SELECTOR, f"[data-testid='delete-{todo_id}']")
        self.driver.find_element(*selector).click()
        return self

    def get_count_text(self):
        """Returnera räknartexten."""
        return self.driver.find_element(*self.COUNT_TEXT).text

    def is_todo_done(self, todo_id):
        """Kolla om en uppgift är markerad som klar."""
        selector = (By.CSS_SELECTOR,
                     f"[data-testid='todo-item-{todo_id}']")
        item = self.driver.find_element(*selector)
        return "done" in item.get_attribute("class")
