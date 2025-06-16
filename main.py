def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(f"{number_of_words(frankenstein)} words found in the document")


def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    
    return book_contents

def number_of_words(text):
    return len(text.split())


if __name__ == "__main__":
    main()