import requests
import os

API_KEY = "nope!"
OWS_CALL_PARAMETERS = {
        "lat": 35.689487,
        "lon": 139.691711,
        "appid": API_KEY,
        "cnt": 4
}


def is_rain_on_forecast(forecast: dict) -> bool:
    for partial_forecast in forecast["list"]:
        if partial_forecast["weather"][0]["id"] < 700:
            return True
    return False


def main():
    result = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                          params=OWS_CALL_PARAMETERS)
    result.raise_for_status()

    forecast = result.json()
    if is_rain_on_forecast(forecast):
        print("Bring an umbrella!")

    # Not gonna use SMS, here is an env variable test instead:
    print(os.environ.get("XDG_SESSION_TYPE"))


if __name__ == "__main__":
    main()
