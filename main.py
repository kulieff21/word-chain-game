WORDS_USED = []

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
    print("Rule: Your word must start with the last letter of the previous word.\n")

    last_word = ""
    current_player = 1

    while True:
        word = input(f"Player {current_player}, enter a word: ").strip()

        is_valid, error_message = is_valid_word(word, last_word)

        if not is_valid:
            print(f"Invalid word! {error_message}")
            print(f"Game over. Player {current_player} loses.")
            break

        WORDS_USED.append(word)
        last_word = word
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()