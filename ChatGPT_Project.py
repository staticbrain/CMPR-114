import re # Used for removing non-lowercase letters
import openai

openai.api_key = "copy and paste from document shared earlier in semester"

class Hangman:
    def __init__(self):
        self.secret_word = ""
        self.guesses_remaining = 6 # Head, body, and 4 limbs
        self.guessed_letters = []
        self.incorrect_letters = []

    def generate_secret_word(self, chatbot):
        while True:
            response = chatbot.generate_response(self.secret_word)

            # Removes spaces and tabs, and splits it into a list of words
            generated_words = response.strip().split()

            if generated_words:

                # If list is empty, assigns first word from the generated words list into the variable
                generated_word = generated_words[0]

                # Removes non-lowercase letters from any words that were generated
                generated_word = re.sub(r"[^a-z]", "", generated_word)

                # Makes sure secret words are more than 4 letters
                if len(generated_word) >= 4:
                    self.secret_word = generated_word
                    break

    # Checks if the game is over
    def game_over(self):
        if self.guesses_remaining == 0:
            return True
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    # Draws the hangman based on number of guesses left
    def draw_hangman(self):
        hangman_dict = {
            6: "_____\n|   |\n|\n|\n|\n|",
            5: "_____\n|   |\n|   O\n|\n|\n|",
            4: "_____\n|   |\n|   O\n|   |\n|\n|",
            3: "_____\n|   |\n|   O\n|  /|\n|\n|",
            2: "_____\n|   |\n|   O\n|  /|\\\n|\n|",
            1: "_____\n|   |\n|   O\n|  /|\\\n|  /\n|",
            0: "_____\n|   |\n|   O\n|  /|\\\n|  / \\\n|"
        }
        print(hangman_dict[self.guesses_remaining])
        print()

    # Main game loop
    def play(self, chatbot):

        # Generates the secret word
        self.generate_secret_word(chatbot)

        while not self.game_over():
            self.draw_hangman()

            # Displays letters guessed
            word_string = ""
            for letter in self.secret_word:
                if letter.lower() in self.guessed_letters:
                    word_string += letter + " "
                else:
                    word_string += "_ "

            print(word_string)
            print("Incorrect letters guessed:", " ".join(self.incorrect_letters))

            guess = input("Guess a letter: ").lower()

            try:

                # Ensures the user enters one letter, no more and no less
                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError("You must guess a single letter.\n")

            # Provides an error if the user does not enter a valid guess
            except ValueError as ve:
                print(f"Error: {ve}")
                continue

            # Tells the user they already guessed a letter
            if guess in self.guessed_letters:
                print("\nYou have already guessed that letter. Try again.\n\n")
                continue

            # Adds letters guessed to a list
            self.guessed_letters.append(guess)

            # Keeps track of guesses remaining based on incorrect letters
            if guess not in self.secret_word.lower():
                self.guesses_remaining -= 1
                self.incorrect_letters.append(guess)

        self.draw_hangman()

        if self.guesses_remaining == 0:
            print("\nYou lost!")
            print(f"The secret word was: {self.secret_word}\n")
        else:
            print("\nCongratulations! You won!\n")
            print(f"The secret word was: {self.secret_word}\n")

    # Resets game and words once user is done
    def reset_game(self):
        self.secret_word = ""
        self.guesses_remaining = 6
        self.guessed_letters = []
        self.incorrect_letters = []

class ChatGPT:
    def __init__(self):

        # Keeps track of past user inputs
        self.session_history = []

        # List of common words the AI uses as a reference - secret words are not limited to this list
        self.common_words = [
            "airplane",
            "bouillon",
            "canopy",
            "dealership",
            "entity",
            "fruitful",
            "giraffe",
            "hangman",
            "icicle",
            "jungle",
            "kangaroo",
            "lemonade",
            "manicure",
            "nightly",
            "orange",
            "parroted",
            "queen",
            "rainbow",
            "strawberry",
            "tiger",
            "umbrella",
            "vision",
            "watermelon",
            "xylophone",
            "yellow",
            "zebra"
        ]

    # Generates response from ChatGPT
    def generate_response(self, user_input):
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"user: {user_input}\nChatGPT:",
            max_tokens=60,
            temperature=0.7,
            n=1,
            stop=None
        )

        generated_text = response.choices[0].text.strip()
        generated_words = generated_text.split()

        # Filters words so they do not include special characters and are not more than 10 letters
        filtered_words = [word for word in generated_words if "-" not in word and not any(char.isdigit() for char in word) and not any(char.isupper() for char in word)]
        filtered_words = [word[:10] for word in filtered_words]
        filtered_response = " ".join(filtered_words)

        return filtered_response

    def chat(self):
        print("ChatGPT: Hello! I'm ChatGPT. Let's play a game of Hangman!")
        
        hangman = Hangman()

        while True:
            hangman.reset_game() # Resets the game
            user_input = input("You: ")
            self.session_history.append(user_input)
            hangman.play(self)

            if hangman.game_over():
                user_input = input("\nChatGPT: Play again? (yes/no): ")
                if user_input.lower()== "yes":
                    continue
                if user_input.lower() == "no":
                    print("\nChatGPT: Thanks for playing! Goodbye!\n")
                    break

            print()

# Starts the chat session
chatbot = ChatGPT()
chatbot.chat()
