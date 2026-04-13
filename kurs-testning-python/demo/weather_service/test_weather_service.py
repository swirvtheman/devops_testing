from unittest.mock import patch, Mock
from weather_service import WeatherService

@patch("weather_service.requests.get")    # ← Patchar requests.get
def test_get_temperature(mock_get):       #    i weather_service-modulen
    # Konfigurera mock-svaret
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 22.5}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    service = WeatherService("fake-key")
    temp = service.get_temperature("Göteborg")

    assert temp == 22.5
    mock_get.assert_called_once()
