import json


def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)
    

def convert(amount: float, base: str, someother: float, to: str, rates: dict[str, dict]) -> float:
    base: str = base.lower() 