import sys
from stats import (
    count_words_in_text,
    count_characters_in_text,
    sorted_character_list
)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    raw_text = (get_book_text(book_text_file))
    word_count = count_words_in_text(raw_text)
    character_count = count_characters_in_text(raw_text)
    character_count_sorted = sorted_character_list(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_text_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in character_count_sorted:
        character = c["char"]
        count = c["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

try:
    book_text_file = sys.argv[1]
    main()
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    