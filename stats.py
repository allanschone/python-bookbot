def count_words_in_text(text):
    split_text = text.split()
    return len(split_text)

def count_characters_in_text(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count