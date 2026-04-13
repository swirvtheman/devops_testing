    
# test_age_validator.py
import pytest
from age_validator import validate_age

class TestEkvivalensklasser:
    """Testar med ett representativt värde per klass."""
    
    def test_barn(self):
        assert validate_age(5) == "barn"
    
    def test_ungdom(self):
        assert validate_age(15) == "ungdom"
    
    def test_vuxen(self):
        assert validate_age(30) == "vuxen"
    
    def test_senior(self):
        assert validate_age(80) == "senior"
    
    def test_negativ_alder(self):
        with pytest.raises(ValueError):
            validate_age(-1)
    
    def test_for_hog_alder(self):
        with pytest.raises(ValueError):
            validate_age(151)


class TestGransvarden:
    """Testar värdena vid gränserna."""
    
    @pytest.mark.parametrize("age,expected", [
        (0, "barn"),       # Nedre gräns
        (12, "barn"),      # Övre gräns barn
        (13, "ungdom"),    # Nedre gräns ungdom
        (17, "ungdom"),    # Övre gräns ungdom
        (18, "vuxen"),     # Nedre gräns vuxen
        (64, "vuxen"),     # Övre gräns vuxen
        (65, "senior"),    # Nedre gräns senior
        (150, "senior"),   # Övre gräns senior
    ])
    def test_gransvarden(self, age, expected):
        assert validate_age(age) == expected

