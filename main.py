from stats import get_number_of_words, count_every_character, sort_dict_of_characters

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    character_count = count_every_character(frankenstein)
    sorted_characters = sort_dict_of_characters(character_count)

    generate_report("books/frankenstein.txt", get_number_of_words(frankenstein), sorted_characters)

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()    
    return book_contents


def generate_report(filepath, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for ch in char_list:
        print(ch["character"], ch["num"], sep=": ")

if __name__ == "__main__":
    main()