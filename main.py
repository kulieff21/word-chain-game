import threading

WORDS_USED = []

def input_with_timeout(prompt, timeout):
    print(prompt, end="", flush=True)
    user_input = [None]

    def get_input():
        user_input[0] = input()

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    return user_input[0]

def is_valid_word(word, last_word):
    if not word:
        return False, "You must enter a word!"

    if not word.isalpha():
        return False, "Word must contain only letters!"

    if len(word) < 2:
        return False, "Word must be at least 2 letters long!"

    if word in WORDS_USED:
        return False, f"{word} was already used!"

    if last_word and word[0].lower() != last_word[-1].lower():
        return False, f"Word must start with {last_word[-1]}"

    return True, ""

def play_game():
    print("=== Word Chain Game ===")
    print("Rule: Your word must start with the last letter of the previous word.")
    print("You have 10 seconds per turn!\n")

    last_word = ""
    current_player = 1
    TIME_LIMIT = 10

    while True:
        word = input_with_timeout(f"Player {current_player}, enter a word: ", TIME_LIMIT)

        if word is None:
            print(f"\nTime's up! Player {current_player} loses.")
            break

        word = word.strip()

        is_valid, error_message = is_valid_word(word, last_word)

        if not is_valid:
            print(f"Invalid word! {error_message}")
            print(f"Game over. Player {current_player} loses.")
            break

        WORDS_USED.append(word)
        last_word = word
        current_player = 2 if current_player == 1 else 1

    show_summary(current_player)

def show_summary(losing_player):
    winner = 2 if losing_player == 1 else 1

    print("\n=== Game Summary ===")
    print(f"Winner: Player {winner}")
    print(f"Total words played: {len(WORDS_USED)}")

    if WORDS_USED:
        print("Word chain:")
        print(" -> ".join(WORDS_USED))

if __name__ == "__main__":
    play_game()