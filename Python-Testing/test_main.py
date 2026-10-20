from main import get_weather

def test_get_weather():
    assert get_weather(21) == "Hot"
    assert get_weather(11) == "Cold"