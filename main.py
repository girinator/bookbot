import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as file:
        content = file.read()
        return content

from stats import count_words
from stats import count_characters
from stats import sort
def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    dictionary = count_characters(text)
    #print(f"{count_words(text)} words found in the document")
    #print(count_characters(text))
    #print(sort(dictionary))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print(f"--------- Character Count -------")
    for key in dictionary:
        value = dictionary[key]
        if key.isalpha():
            print(f"{key}: {value}")
    print(f"============= END ===============")

main()

    

