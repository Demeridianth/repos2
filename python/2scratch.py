from difflib import SequenceMatcher
from datetime import datetime


class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:
        sequence = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()
    
    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity = 0.0
        best_match = 'Sorry, I didn\'t understand that'
        for response in self.responses:
            similarity = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = self.responses[response] 

        return best_match, highest_similarity
    
    def run(self) -> None:
        print(f'Hello, my name is {self.name}')

        while True:
            user_input = input('You: ')
            response, similarity = self.get_best_response(user_input)

            

            if response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            print(f'{self.name}: {response} (Simliraty: {similarity:.2%})')


def main() -> None:
    responses = {
        'hello': 'Hello! How are you today?',
        'how are you:': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day'
    }

    chat_bot = ChatBot('Responsive Bot', responses)
    chat_bot.run()

if __name__ == '__main__':
    main()


"""
Homework:
1. Add more responses.
2. Add a way to exit the program through the chat.
3. Add some cool features, like checking for the weather forecast.
4. Send an email adress !
5. Make it so that if the accuracy falls below 50%, it returns a default response.

!!! Make it would respond only to close inputs !!!

"""