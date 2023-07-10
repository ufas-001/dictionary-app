import sys
import signal


def display_menu():
    print("=== Python Dictionary App ===")
    print("1. Look up a word")
    print("2. Exit")


def lookup_word(dictionary):
    word = input("Enter a word to look up: ")
    if word in dictionary:
        definitions = dictionary[word]
        print(f"\nDefinitions for '{word}':")
        for i, definition in enumerate(definitions):
            print(f"{i+1}. {definition}")
    else:
        print(f"\n'{word}' not found in the dictionary.")


def load_dictionary():
    return {
        "apple": ["A fruit that grows on trees.", "A green Plant", "A class of fruit"],
        "car": ["A four-wheeled vehicle used for transportation."],
        "computer": ["An electronic device that can perform various tasks."],
    }


def main():
    dictionary = load_dictionary()

    def signal_handler(signal, frame):
        print("\nExiting the app. Goodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            lookup_word(dictionary)
        elif choice == "2" or choice.lower() == "exit" or choice.lower() == "quit":
            print("\nExiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
