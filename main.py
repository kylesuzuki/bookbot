import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # Check if there are enough arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the path from command line arguments
    path = sys.argv[1]
    
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_count = get_char_count(text)
    sorted_chars = sort_char_count(char_count)  # Pass char_count as an argument
    
    # Now print the report with proper formatting
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through sorted characters and print them
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
