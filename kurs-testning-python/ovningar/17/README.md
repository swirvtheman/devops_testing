# Övning 17 - BDD med pytest-bdd

Vi ska bygga en inloggningsfunktion med BDD.

Vi har tre filer:
- login.feature - vi har har tre scenarion: lyckad inloggning, felaktigt lösenord och icke-existerande användare. Det här täcker happy path och två vanliga error paths.
- Filen auth.py är vår kod, en enkel AuthService-klass som lagrar användare i en dict. Inget fancy, vi vill fokusera på BDD-konceptet, inte på databaslogik.
- Filen test_login.py innehåller våra step definitions. Varje Given, When och Then i feature-filen måste matcha en decorator i python-filen. pytest-bdd använder strängmatchning så texten i decoratorn måste matcha feature-filen exakt.

Din uppgift är att skriva klart step definitions.

