import random

word_list = ["Космос", "Болото", "Векс", "Мышь", "Кружка"]


def got_word():
    return random.choice(word_list).upper()


word = got_word().upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Добро пожаловать в угадайку слов. ")
    print(display_hangman(tries))
    print(f"Загаданное слово : {word_completion}")
    print()
    while guessed == False and tries > 0:
        guess = input("Введите букву или слово : ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже называли эту букву.")
            elif guess not in word:
                print(f"Буквы {guess} нет в слове.")
                tries -= 1
            else:
                print(f"Буква {guess} есть в слове!")
                guessed_letters.append(guess)
                word_completion = "".join(
                    [
                        guess if letter == guess else word_completion[i]
                        for i, letter in enumerate(word)
                    ]
                )

                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha:
            if guess in guessed_words:
                print("Вы уже называли это слово")
            elif guess != word:
                print("Это не то слово.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Недопустимый ввод. Введите одну букву или слово целиком.")

        print(word_completion)
        print(display_hangman(tries))

    if guessed:
        print("Правильно! Вы угадали слово!")
    if not guessed:
        print(f"К сожалению, неверно. Загаданное слово - {word}")


def main():
    play(word)
    more = input('Хотите сыграть ещё?, "д" если да , "н" если нет : ')
    while True:
        if more.upper() == "Д":
            play(word)
        if more.upper() == "Н":
            print("Спасибо за игру, пока !")
            break
        else:
            more = input('Хотите сыграть ещё?, "д" если да , "н" если нет : ')
            continue


main()
