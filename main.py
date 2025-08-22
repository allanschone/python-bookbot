from stats import count_words_in_text
from stats import count_characters_in_text

book_text_file = "books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    raw_text = (get_book_text(book_text_file))
    word_count = count_words_in_text(raw_text)
    print(f"{word_count} words found in the document")
    character_count = count_characters_in_text(raw_text)
    print(character_count)

main()