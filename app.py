import random

class SimpleChatBot:
    """
    A simple chatbot that can respond to user inputs with predefined answers.

    Attributes:
    - responses: dict
        A dictionary containing various user inputs as keys and corresponding responses as values.
    """

    def __init__(self):
        """
        Initializes the SimpleChatBot with a set of predefined responses.

        The responses are designed to cover a range of common questions and statements.
        """
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Greetings!", "How can I assist you today?"],
            "how are you?": ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?", "I'm here to help you!"],
            "what is your name?": ["I'm a simple chatbot created to assist you.", "You can call me ChatBot.", "I don't have a name, but I'm here to chat!"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "default": ["I'm sorry, I don't understand that.", "Can you please rephrase?", "Let's talk about something else!"]
        }

    def get_response(self, user_input: str) -> str:
        """
        Retrieves a response based on the user's input.

        Parameters:
        - user_input: str
            The input provided by the user.

        Returns:
        - str:
            A response string that corresponds to the user's input. If the input is not recognized,
            a default response is provided.
        """
        # Normalize the user input to lower case for easier matching
        normalized_input = user_input.lower()

        # Check if the input matches any predefined responses
        if normalized_input in self.responses:
            return random.choice(self.responses[normalized_input])
        else:
            return random.choice(self.responses["default"])

    def chat(self):
        """
        Starts a chat session with the user.

        The user can type messages, and the chatbot will respond until the user types 'bye'.
        """
        print("Welcome to the Simple ChatBot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("ChatBot: Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"ChatBot: {response}")

# Example of using the SimpleChatBot class
if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.chat()
