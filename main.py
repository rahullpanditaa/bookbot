from stats import get_number_of_words

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(f"{get_number_of_words(frankenstein)} words found in the document")


def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()    
    return book_contents


if __name__ == "__main__":
    main()