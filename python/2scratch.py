import requests


def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base = base.lower()
    to = to.lower()

    from_rates = rates.get(base)
    to_rates = rates.get(to)
    all_rates = [rate for rate in rates]

    if from_rates is not None and to_rates is not None:
        result = amount * (to_rates['rate'] / from_rates['rate'])
    else:
        print(f'rate is invalid, please choose from these rates\n: {", ".join(all_rates)}')


def main():
    response = requests.get('http://currency_API_link_here...')
    response_json = response.json()
    rates = response_json['currency rates']
    result = convert(amount=10, base='eur', to='usd', rates=rates)
    print(result)


if __name__ == '__main__':
    main()