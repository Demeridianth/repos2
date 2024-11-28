from difflib import SequenceMatcher
from datetime import datetime
import requests
import json


"""A responsive bot, try asking it some simple questions (it knows the weather)"""


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
            print(similarity)
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

            print(f'{self.name}: {response} (Simliraty: {similarity:.2%})')


def main() -> None:
    responses = {
        'hello': 'Hello! How are you today?',
        'hi': 'Hi there! How can I assist you today?',
        'hey': 'Hey! What can I help you with?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'what is the time': 'GET_TIME',
        'tell me the time': 'GET_TIME',
        'what is the weather today': 'GET_WEATHER',
        'what weather is like today': 'GET_WEATHER',
        'weather forecast': 'GET_WEATHER',
        'do you know the weather': 'GET_WEATHER',
        'Goodbye': 'EXIT',
        'Bye': 'EXIT',
        'See you later': 'EXIT',
        'So long': 'EXIT',
        'who are you': 'I am a Response Bot',
        'what is your name': 'My name is Responsive Bot!',
        'what are you': 'I am a chatbot designed to assist you.',
        'what can you do': 'I can chat with you, answer basic questions, and tell you the date and time.',
        'what coding language are you written in': 'I am written in Python',
        'do you know python': 'Yes, I am actually written in Python!',
        'what year is it': 'GET_YEAR',
        'what date is it': 'GET_DATE',
        'what is the date today': 'GET_DATE',
        'tell me the date': 'GET_DATE',
        'tell me a joke': 'Why did the programmer quit his job? Because he didn\'t get arrays!',
        'do you like python': 'Of course! Python is great for building chatbots like me.',
        'can you help me with programming': 'Sure! I can answer basic programming questions or guide you to resources.',
        'what is ai': 'AI, or artificial intelligence, is a field of computer science focused on building smart machines capable of performing tasks that typically require human intelligence.',
        'tell me about yourself': 'I am a chatbot here to help you with various questions and have a friendly chat!',
        'how does a chatbot work': 'Chatbots analyze user input, then find the best matching response or perform an action based on their programming.',
        'can you calculate something for me': 'I can answer questions, but for calculations, I suggest a calculator or programming tool.',
        'what is machine learning': 'Machine learning is a subset of AI that enables systems to learn from data and improve from experience without being explicitly programmed.',
        'what is deep learning': 'Deep learning is a type of machine learning that uses neural networks to analyze complex data.',
        'do you have feelings': 'I don\'t have feelings, but I\'m here to chat and hopefully make your day a little brighter!',
        'can you learn new things': 'I have a set range of responses, but developers can improve me over time.',
        'what is your purpose': 'My purpose is to assist you with information and make your day a little easier!',
        'what can you tell me about programming': 'Programming is the process of writing instructions for computers to perform tasks.',
        'do you know any programming languages': 'I\'m familiar with Python since I\'m written in it, but I can answer basic questions about other languages too!',
        'what is data science': 'Data science is a field that uses statistical and computational techniques to analyze data and gain insights.',
        'tell me a fun fact': 'Did you know that the first computer virus was created in 1983? It was called "Elk Cloner."',
        'how old are you': 'I am as old as my code! I don\'t age in the traditional sense.',
        'can you answer all questions': 'I try my best, but I may not know everything!',
    }


    chat_bot = ChatBot('Responsive Bot', responses)
    chat_bot.run()


if __name__ == '__main__':
    main()


"""
Homework:
3. Add some cool features, like checking for the weather forecast.
-- add location API -- to weather and to a question (where am i?)

4. Send an email adress !




"""