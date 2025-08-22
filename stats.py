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

def sort_on(items):
    return items["count"]

def sorted_character_list(character_count_dictionary):
    character_list = []
    for character in character_count_dictionary:
        character_dictionary = {}
        character_dictionary["char"] = character
        character_dictionary["count"] = character_count_dictionary[character]
        character_list.append(character_dictionary)
    character_list.sort(reverse=True, key=sort_on)
    return character_list