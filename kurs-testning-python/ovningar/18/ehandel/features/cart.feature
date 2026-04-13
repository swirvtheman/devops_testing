Feature: Kundvagn

  Background:
    Given att kundvagnen är tom

  Scenario: Lägg till en vara
    When jag lägger till "T-shirt" med pris 299.00 kr
    Then ska kundvagnen innehålla 1 vara
    And totalsumman ska vara 299.00 kr

  Scenario: Lägg till flera varor
    When jag lägger till "T-shirt" med pris 299.00 kr
    And jag lägger till "Jeans" med pris 599.00 kr
    Then ska kundvagnen innehålla 2 varor
    And totalsumman ska vara 898.00 kr

  Scenario: Ta bort en vara
    Given att kundvagnen innehåller "T-shirt" med pris 299.00 kr
    When jag tar bort "T-shirt"
    Then ska kundvagnen innehålla 0 varor
    And totalsumman ska vara 0.00 kr

  Scenario Outline: Tillämpa rabattkod
    Given att kundvagnen innehåller "T-shirt" med pris 500.00 kr
    When jag tillämpar rabattkoden "<kod>"
    Then ska totalsumman vara <förväntat> kr

    Examples:
      | kod       | förväntat |
      | RABATT10  | 450.00    |
      | RABATT20  | 400.00    |
      | OGILTIGT  | 500.00    |

  Scenario: Rabattkod på tom vagn
    When jag tillämpar rabattkoden "RABATT10"
    Then ska totalsumman vara 0.00 kr

