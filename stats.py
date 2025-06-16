def get_number_of_words(text):
    return len(text.split())

def count_every_character(text):
    num_of_characters = {}
    for ch in text.lower():
        if ch not in num_of_characters:
            num_of_characters[ch] = 1
        else:
            num_of_characters[ch] += 1
    return num_of_characters

def sort_dict_of_characters(dict_of_characters):
    sorted_list_of_characters = []

    for ch in dict_of_characters:
        if ch.isalpha():
            sorted_list_of_characters.append({"character" : ch, "num" : dict_of_characters[ch]})
        
    return sorted(sorted_list_of_characters, key=lambda char: char["num"], reverse=True)
