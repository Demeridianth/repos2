def calculate_split(total_amount: float, percentages: list[float], currency: str) -> None:
    # Validate if the sum of percentages equals 100%
    if sum(percentages) != 100:
        raise ValueError('Percentages must add up to 100')

    print(f'Total expenses: {currency}{total_amount:,.2f}')
    print(f'Number of people: {len(percentages)}')
    
    # Calculate and display the amount each person should pay based on their percentage
    for i, percentage in enumerate(percentages, start=1):
        share = (percentage / 100) * total_amount
        print(f'Person {i} should pay: {currency}{share:,.2f} ({percentage}%)')

def get_input(prompt, converter=str):
    while True:
        try:
            return converter(input(prompt))
        except ValueError:
            print('Please enter a valid value.')

def get_percentages(number_of_people: int) -> list[float]:
    percentages = []
    for i in range(1, number_of_people + 1):
        percentage = get_input(f'Enter the percentage for person {i}: ', float)
        percentages.append(percentage)
    return percentages

def main() -> None:
    total_amount = get_input('Enter the total amount: ', float)
    number_of_people = get_input('Enter the number of people: ', int)
    currency = get_input('Enter currency: ', int)
    
    if number_of_people < 1:
        raise ValueError('Number of people must be more than one')
    
    # Ask if user wants uneven split
    uneven = get_input('Do you want to enter uneven splits? (yes/no): ').strip().lower()

    if uneven == 'yes':
        percentages = get_percentages(number_of_people)
        calculate_split(total_amount, percentages, currency='eur')
    else:
        # Even split case
        share_per_person = total_amount / number_of_people
        print(f'Total expenses: {currency}{total_amount:,.2f}')
        print(f'Number of people: {number_of_people}')
        print(f'Each person should pay: {currency}{share_per_person:,.2f}')

if __name__ == '__main__':
    main()
