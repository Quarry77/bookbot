def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text:
        if char.lower() not in characters:
            characters[char.lower()] = 0
        characters[char.lower()] += 1
    return characters

def sort_characters(characters):
    sorted_list = []
    for char in characters:
        sorted_list.append({"char": char, "num": characters[char]})
    sorted_list.sort(reverse=True, key=sort_key_num)
    return sorted_list

def sort_key_num(items):
    return items["num"]