import sys
from stats import sort_on, get_book_text, count_words, get_character_record


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============\n\nAnalyzing book found at books...\n")
    word_number = get_book_text(book_path)
    char_number = get_character_record(book_path)
    print("============= END ===============")


main()
