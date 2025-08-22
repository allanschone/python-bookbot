book_text_file = "books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words_from_text(text):
    split_text = text.split()
    return len(split_text)

def main():
    word_count = count_words_from_text((get_book_text(book_text_file)))
    print(f"{word_count} words found in the document")

main()