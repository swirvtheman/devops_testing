# Övning 16 - Page Object Model

Page Object Model är det viktigaste design pattern för Selenium-tester. Konceptet är enkelt: skapa en klass per sida. Klassen innehåller alla selektorer och erbjuder metoder för de handlingar en användare kan göra.

Testet anropar `page.add_todo("Köp mjölk")` istället för att pilla med `find_element` och `send_keys`. Testet beskriver *vad* som skall hända, och Page Object hanterar *hur*.

Om UI ändras uppdaterar vi Page Object-klassen, testerna förblir orörda.

## Todo

Filen `todo_page.py` innehåller Page Object-klassen.

Längst upp har vi alla selektorer som klasskonstanter: `HEADING`, `TAST_INPUT`, `ADD_BUTTON` och så vidare. Om en selektor ändras uppdaterar vi den *här* och ingenstans annars.

Sen har vi metoder för varje handling: `add_todo`, `toggle_todo`, `delete_todo` och `get_todo_items`. Metoderna returnerar `self` med method chaining - vilket gör testerna mer flytande.

Märk att Page Object INTE innehåller assertions. Det är testets jobb. Page Object vet *hur* man interagerar med sidan, testet vet *vad* som skall verifieras.

I filen `test_todo_pom.py` hittar du tester, jämför de med de du skrev i övning 15. Ser du skillnaden? Inga selektorer, inget `find_element` och inget `send_keys`. Testerna blir som en berättelse: "Navigera, lägg till en uppgift och verifiera att den syns".

Om frontend-teamet byter `id="task-input"` till `id="new-task-field"` ändrar du *en rad* i `TodoPage`-klassen och alla tester fortsätter att fungera.

Det här är professionell testkod. Den är den här nivån man förväntar sig i arbetslivet.

## Uppgiften

> OBS! Detta fungerar inte på macOS (med M1/M2/M3/M4/M5 cpu) eller andra ARM-baserade operativsystem så som Raspberry PI. Det finns en fix: att installera Chromium och Chromium Driver och ändra så testet kör Chromium istället. Det gör dock containern mycket större.

I katalogen `pages/` hittar du filerna `todo_page.py` och `test_todo_pom.py`. Här skall du portera dina tester från övning 15 till POM. Du skall också lägga till två helt nya, valfria, testfall.

1. Portera dina tester från övning 15 till POM.
2. Lägg till två valfria tester.
3. Lägg till metoden `wait_for_todo_count(n)` med explicit wait.
4. Testa method chaining med: `page.nagivate().add_todo("X").add_todo("Y")

