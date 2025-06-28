import requests
import datetime as dt
import smtplib as smtp
import time

MY_LAT = 35.689487
MY_LONG = 139.691711

SENDER_EMAIL = "dummyemail@gmail.com"
SENDER_PWD = "dummypassword"
RECIEVER_EMAIL = "dummyreciever@gmail.com"
MAIL_BODY = "Subject: ISS Notification\n\nLook up! The ISS is right above you!"


def get_iss_position() -> (float, float):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    return latitude, longitude


def is_iss_on_range(lat: float, long: float) -> bool:
    iss_latitude, iss_longitude = get_iss_position()
    return not (iss_latitude >= lat + 5 or iss_latitude <= lat - 5 or
                iss_longitude >= long + 5 or iss_longitude <= long - 5)


def get_sunset_sunrise_hours(lat: float, long: float) -> (int, int):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset


def is_nighttime(lat: float, long: float) -> bool:
    current_hour = dt.datetime.now().hour
    sunrise_hour, sunset_hour = get_sunset_sunrise_hours(lat, long)
    return not (current_hour >= sunrise_hour and current_hour <= sunset_hour)


def send_look_up_email(reciever: str) -> None:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PWD)
        connection.sendmail(to_addrs=reciever,
                            from_addr=SENDER_EMAIL,
                            msg=MAIL_BODY)


def main():
    while True:
        if is_iss_on_range(MY_LAT, MY_LONG) and is_nighttime(MY_LAT, MY_LONG):
            send_look_up_email(RECIEVER_EMAIL)
        time.sleep(60)


if __name__ == "__main__":
    main()
