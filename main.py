import sys
from stats import get_book_text,word_count, per_cha_count, book_report

def main():
    #book_path = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text("./"+book_path)
    book_word_count = word_count(book_text)
    book_per_cha_count = per_cha_count(book_text)
    #print (f"{book_word_count} words found in the document")
    #print (book_per_cha_count)

    #============ BOOKBOT ============
    title = " BOOKBOT "
    print("Analyzing book found at " + book_path + "...")
    sub_title = " Word Count "
    print(f"{title:=^33}")
    print(f"{sub_title:-^33}")
    print("Found",book_word_count,"total words")
    sub_title = " Character Count "
    print(f"{sub_title:-^33}")
    report = book_report(book_per_cha_count)
    for letter in report:
        if letter["cha"].isalpha():
            print(f"{letter["cha"]}:",letter["num"])
main()

