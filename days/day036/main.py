import requests
import smtplib as smtp

SENDER_EMAIL = "dummysender@gmail.com"
RECIEVER_EMAIL = "dummyreciever@gmail.com"
SENDER_PWD = "dummypassword"

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

API_KEY_ALPHAVANTAGE = "dummyapikey1"
API_KEY_NEWS = "dummyapikey2"


def get_stock_variation() -> float:
    parameters = {
            "function": "GLOBAL_QUOTE",
            "symbol": STOCK,
            "apikey": API_KEY_ALPHAVANTAGE,
    }
    response = requests.get("https://www.alphavantage.co/query",
                            params=parameters)
    response.raise_for_status()
    variation_percent = response.json()["Global Quote"]["10. change percent"]
    return float(variation_percent.strip("%"))


def get_headlines(number: int) -> list:
    if number > 100:
        print("News must be requested at most 100 at a time!")
        return None

    parameters = {
            "q": COMPANY_NAME,
            "pageSize": 3,
            "apikey": API_KEY_NEWS,
    }
    response = requests.get("https://newsapi.org/v2/top-headlines",
                            params=parameters)
    response.raise_for_status()
    return response.json()["articles"]


def get_headlines_formatted(number: int, variation: float) -> str:
    if variation >= 0:
        icon = "⬆️"
    else:
        icon = "⬇️"

    result = f"{STOCK} ({COMPANY_NAME}): {variation} {icon}\n\n"

    news = get_headlines(number)
    for item in news:
        result += f"{item['title']}\n{item['description']}\n\n"

    result += "Brought to you by el wiwi!"
    return result


def send_email(body: str) -> None:
    email_message = f"Subject: {COMPANY_NAME} news!\n\n" + body
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PWD)
        connection.sendmail(to_addrs=RECIEVER_EMAIL,
                            from_addr=SENDER_EMAIL,
                            msg=email_message)


def main():
    variation = get_stock_variation()
    if abs(variation) > 5:
        print(get_headlines_formatted(3, variation))
        # send_email(get_headlines_formatted(3, variation))
