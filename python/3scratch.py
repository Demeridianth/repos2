from difflib import SequenceMatcher
from datetime import datetime


class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    def calculate_similarity(self, input_sentence: str, response_sentence: str) -> float:
        similarity = SequenceMatcher(a=input_sentence, b=response_sentence)
        return similarity.ratio()
    
    def get_best_response(self, user_input: str) -> str:
        highest_similarity = 0.0
        best_choice = 'Sorry. Can\'t understand you'
        for response in self.responses:
            similarity = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_choice = self.responses[response]

        return best_choice, highest_similarity
    
    def run(self) -> None:
        print('Hello, my name is Responsive Bot')

        user_input = input('You: ')
        response, similarity = self.get_best_response(user_input)

        if response == 'GET TIME':
            response = f'The time is {datetime.now():%H:%M}'

        print(f'{self.name}: {response} (Similarity: {similarity:.2%})')


def main():
    responses = {
        'hello': 'Hello! How are you today?',
        'how are you:': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'bye': 'Goodbye! Have a great day'
    }

    chat_bot = ChatBot('BoT', responses=responses)
    chat_bot.run()


if __name__ == '__main__':
    main()
