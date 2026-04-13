# Övning 15 - Automatisera med Selenium

Vi har en enkel TODO-app som är skriven med Flask. Denna skall vi testa med Selenium.

TODO-appen har:

- En startsida med en lista av uppgifter
- Ett formulär för att lägga till nya uppgifter
- Möjlighet att markera uppgifter som klara
- Möjlighet att radera uppgifter

Din uppgift är att automatisera tester som navigerar appen, lägger till uppgifter, markerar uppgifter som klara och verifierar att allt fungerar.

## TODO-appen

Filen `app_todo.py` innehåller TODO-appen. Notera `data-testid`-attributen i HTML-koden. Det är en best practice för testbarhet. Istället för att söka efter CSS-klasser eller test (som kan ändras) har vi stabila testidentifierare. Det gör testerna mer robusta.

Appen startas automatiskt av testet, så du behöver inte ha två fönster öppnade.

## Testerna

> OBS! Detta fungerar inte på macOS (med M1/M2/M3/M4/M5 cpu) eller andra ARM-baserade operativsystem så som Raspberry PI. Det finns en fix: att installera Chromium och Chromium Driver och ändra så testet kör Chromium istället. Det gör dock containern mycket större.

Filen `test_todo_selenium.py` innehåller test-setupen och det är också här du skall skriva dina tester. Här finns tre delar:

- `live_server` startar Flask i en bakgrundstråd - vi behöver en körande server som Selenium kan prata med. Den här fixturen har `scope="module"` så servern startas bara en gång per testfil.
- `driver` skapar en headless Chrome-instans. Headless innebär att ingen synlig webbläsare öppnas - den kör i bakgrunden. Det är standardsättet för att köra Selenium i CI/CD.
- `clean_todos` rensar data efter vare test, precis som vi gjorde med böckerna i övning 13.
- `implicitly_wait(5)` säger åt Selenium att vänta upp till fem sekunder om ett element inte hittas direkt. Det hjälper med timing-problem.

Här är två färdiga tester som visar hur du skall göra:

```python
def test_page_loads(driver, live_server):
    """Startsidan laddas med rätt rubrik."""
    driver.get(live_server)
    h1 = driver.find_element(By.TAG_NAME, "h1")
    assert h1.text == "Mina uppgifter"


def test_add_todo(driver, live_server):
    """Lägg till en uppgift och verifiera att den syns."""
    driver.get(live_server)
    input_field = driver.find_element(By.ID, "task-input")
    input_field.send_keys("Köp mjölk")
    driver.find_element(By.ID, "add-btn").click()

    # Verifiera att uppgiften syns i listan
    items = driver.find_elements(By.CSS_SELECTOR, "#todo-list li")
    assert len(items) == 1
    assert "Köp mjölk" in items[0].text
```

`test_page_loads` är det enklaste - vi navigerar och verifierar att rubriken finns. `test_add_todo` visar hela flödet: navigera, hitta input, skriv text, klicka och verifiera.

Nu skall du skriva resten själv. Använd `data-testid`-attributen för att hitta rätt element. Till exempel `By.CSS_SELECTOR, "[data-testid='toggle-1']"` för att toggla första uppgiften.

Kör dina tester med kommandot: `pytest test_todo_selenium.py -v`

Skriv tester för:

1. Lägg till 3 uppgifter, alla tre skall visas
2. Markera en uppgift som klar, den skall få CSS-klassen `done`
3. Radera en uppgift, den skall försvinna
4. Räknaren uppdateras efter att du lagt till 2 uppgifter, "2 uppgifter" skall synas
5. Om du postar ett tomt formulär skall inget läggas till

