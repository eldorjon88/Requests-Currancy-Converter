import requests

API_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

def get_rates():
    response = requests.get(API_URL)
    data = response.json()

    rates = {"USD": 1.0, "EUR": None, "UZS": 1.0}
    date = ""

    for item in data:
        if item["Ccy"] == "USD":
            rates["USD"] = float(item["Rate"])
            date = item["Date"]
        elif item["Ccy"] == "EUR":
            rates["EUR"] = float(item["Rate"])

    return rates, date


def convert(amount, from_currency, to_currency, rates):
    if from_currency == "UZS":
        if to_currency == "USD":
            return amount / rates["USD"]
        elif to_currency == "EUR":
            return amount / rates["EUR"]
        else:
            return amount

    if to_currency == "UZS":
        if from_currency == "USD":
            return amount * rates["USD"]
        elif from_currency == "EUR":
            return amount * rates["EUR"]
        else:
            return amount

    if from_currency == "USD" and to_currency == "EUR":
        return (amount * rates["USD"]) / rates["EUR"]
    if from_currency == "EUR" and to_currency == "USD":
        return (amount * rates["EUR"]) / rates["USD"]

    return amount


def main():
    rates, date = get_rates()

    print("Valyuta konvertori (CBU API asosida)")
    print(f"Kurslar sanasi: {date}")

    amount = float(input("Summani kiriting: "))
    from_currency = input("Qaysi valyutadan (USD, UZS, EUR): ").upper()
    to_currency = input("Qaysi valyutaga (USD, UZS, EUR): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print(" Noto'g'ri valyuta kiritildi!")
        return

    result = convert(amount, from_currency, to_currency, rates)
    print(f" {amount:,.2f} {from_currency} = {result:,.2f} {to_currency} ({date})")


if __name__ == "__main__":
    main()
