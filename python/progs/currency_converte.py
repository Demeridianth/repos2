import json
import requests

# from json file

# def load_rates(json_file: str) -> dict[str, dict]:
#     with open(json_file, 'r') as file:
#         return json.load(file)
    

def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base = base.upper() 
    to = to.upper()

    from_rates = rates.get(base, {"rate": 1.0}) if base == 'eur' else rates.get(base)
    to_rates = rates.get(to, {'rate': 1.0}) if to == 'eur' else rates.get(to)
    all_rates = [rate for rate in rates]
        


    if from_rates is not None and to_rates is not None:
        if base == 'eur':
            return amount * to_rates 
        else:
            return amount * (to_rates / from_rates)
    else: 
        print(f'Rate is invalid, here are all available rates:\n  {", ".join(all_rates)}')
        return None

    
        
    
def main():
    # rates taken from API
    response = requests.get('https://v6.exchangerate-api.com/v6/29f44fa576d5ee3a585ef2f6/latest/EUR')
    response_json = response.json()
    rates = response_json['conversion_rates']
    result = convert(amount=10, base='eur', to='usd', rates=rates)
    if result is not None:
        print(result)
    

if __name__ == '__main__':
    main()


"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""