def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    
    return book_contents