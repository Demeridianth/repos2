from difflib import SequenceMatcher
from datetime import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import readline
import json

"""A responsive bot, try asking it some simple questions (it knows the weather, and can send a simple email)"""
# for email sending  Make sure 2-Step Verification and App Passwords are enabled for Gmail accounts.


class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses


    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()
    

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity = 0.5
        best_match = 'Sorry, I didn\'t understand that'
        for response in self.responses:
            similarity = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.responses[response] 
        return best_match, highest_similarity


    @staticmethod
    def get_user_input(prompt: str, converter=str) -> str:
        return converter(input(prompt)) 
    

    def get_weather(self) ->  str:
        country = self.get_user_input('Enter country you are located in: ')
        city = self.get_user_input('Enter city you are located in: ')
        response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}%2C%20{country}?unitGroup=metric&key=BTQTHAA84DKENYU4NLH4AM4FM&contentType=json')
        weather = response.json()
        location = weather['resolvedAddress']
        days = weather['days']
        temp_max = days[0].get('tempmax')
        temp_min = days[0].get('tempmin')
        date_time = days[0].get('datetime')
        description = days[0].get('description')

        print(f'On {date_time} in {location} the temperature will vary from {temp_min} to {temp_max}\n{description}')


    def send_email(self) -> None:
        sender_email = self.get_user_input('Enter your email address: ')
        sender_password = self.get_user_input('Enter you gmail App password: ')
        recipient_email = self.get_user_input('Enter recipient email address: ')
        subject = self.get_user_input('Enter subject: ')
        message = self.get_user_input('Enter message: ')
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print('email sent succesfully')
            
        except Exception as e:
            print(f'Failed to send email: {e}')


    def run(self) -> None:
        print(f'Hello, my name is {self.name}')

        while True:
            user_input = input('You: ')
            response, similarity = self.get_best_response(user_input)

            if user_input == 'q' or user_input == 'quit' or user_input == 'exit':
                break

            elif response == 'EXIT':
                print('Goodbye! Have a nice day.')
                break

            elif response == 'GET_WEATHER':
                self.get_weather()

            elif response == 'GET_YEAR':
                response = f'It is {datetime.now().year}'

            elif response == 'GET_DATE':
                response = f'It is {datetime.now().date()}'

            elif response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            elif response == 'SEND_EMAIL':
                self.send_email()

            print(f'{self.name}: {response} (Simliraty: {similarity:.2%})')


def main() -> None:
    with open('responses.json', 'r') as file:
        responses = json.loads(file.read())
        
    chat_bot = ChatBot('Responsive Bot', responses)
    chat_bot.run()


if __name__ == '__main__':
    main()


