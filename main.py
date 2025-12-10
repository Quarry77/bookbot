from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        result = f.read()
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    characters = count_characters(book_text)
    sorted_chars = sort_characters(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()