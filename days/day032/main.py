import pandas as pd
import datetime as dt
import smtplib as smtp
import random


def read_text_file(file: str) -> str:
    with open(file) as text_file:
        return text_file.read()


def birthday_is_today(entry: pd.Series) -> bool:
    today = dt.datetime.now()
    return entry["month"] == today.month and entry["day"] == today.day


def get_birthday_letter(name: str) -> str:
    return random.choice(LETTERS).replace('[NAME]', name)


def send_email(reciever: str, subject: str, message: str) -> None:
    with smtp.SMTP(SMTP_PROVIDER) as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=EMAIL_SENDER_PWD)
        connection.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=reciever,
                message=f"Subject: {subject}\n\n{message}"
        )


# Data related constants
BIRTHDAYS = [entry for _, entry in pd.read_csv("birthdays.csv").iterrows()]
N_LETTERS = 3
LETTERS = [read_text_file(f"letter_templates/letter_{n}.txt") for n in range(1, N_LETTERS+1)]

# SMTP related constants
EMAIL_SENDER = "dummyemail@gmail.com"
EMAIL_SENDER_PWD = "notgonnaleakthis;)"
SMTP_PROVIDER = "smtp.gmail.com"


def main():
    for person in BIRTHDAYS:
        if birthday_is_today(person):
            letter = get_birthday_letter(person["name"])
            send_email(person["email"], "Happy Birthday!", letter)


if __name__ == "__main__":
    main()
