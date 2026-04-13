Feature: Inloggning

  Scenario: Lyckad inloggning
    Given att användaren "anna" finns med lösenord "hemligt123"
    When användaren loggar in med "anna" och "hemligt123"
    Then ska inloggningen lyckas

  Scenario: Felaktigt lösenord
    Given att användaren "anna" finns med lösenord "hemligt123"
    When användaren loggar in med "anna" och "fellösen"
    Then ska inloggningen misslyckas
    And felmeddelandet ska vara "Felaktigt lösenord"

  Scenario: Icke-existerande användare
    When användaren loggar in med "okänd" och "något"
    Then ska inloggningen misslyckas
    And felmeddelandet ska vara "Användaren finns inte"
