import os
import requests
import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

NL_HOST_DOMAIN = os.environ.get("NL_HOST_DOMAIN")
NL_EXERCISE_ENDPOINT = os.environ.get("NL_EXERCISE_ENDPOINT")

SHEETY_HOST_DOMAIN = os.environ.get("SHEETY_HOST_DOMAIN")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
SHEETY_AUTHORIZATION_KEY = os.environ.get("SHEETY_AUTHORIZATION_KEY")

nl_authentication_headers = {
        "Content-Type": "application/json",
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
}

sheety_authentication_headers = {
        "Authorization": "Basic " + SHEETY_AUTHORIZATION_KEY
}


def get_current_datetime_entries() -> dict:
    current_datetime = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    current_datetime = current_datetime.split(' ')
    return {
            "date": current_datetime[0],
            "time": current_datetime[1],
    }


def get_exercise_list(natural_text: str) -> list:
    nl_exercise_parameters = {
            "query": natural_text
    }

    response = requests.post(url=NL_HOST_DOMAIN+NL_EXERCISE_ENDPOINT,
                             json=nl_exercise_parameters,
                             headers=nl_authentication_headers)
    response.raise_for_status()
    return response.json()["exercises"]


def get_exercise_entries(exercise: dict) -> dict:
    return {
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
    }


def add_row_to_spreadsheet(exercise: dict) -> None:
    sheety_row_parameters = {
            "workout": exercise
    }

    response = requests.post(url=SHEETY_HOST_DOMAIN+SHEET_ENDPOINT,
                             json=sheety_row_parameters,
                             headers=sheety_authentication_headers)
    response.raise_for_status()


def main():
    datetime_entries = get_current_datetime_entries()

    exercise_natural_desc = input("Describe your exercise: ")
    exercise_list = get_exercise_list(exercise_natural_desc)

    for exercise in exercise_list:
        exercise_entries = get_exercise_entries(exercise)

        row = datetime_entries | exercise_entries
        add_row_to_spreadsheet(row)


if __name__ == "__main__":
    main()
