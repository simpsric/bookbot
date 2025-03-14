from stats import get_num_words, get_num_char_appears
import sys

def main(filePath):
    return get_num_words(filePath)
    
    
    
    
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filePath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(main(filePath))
    print("--------- Character Count -------")
    for key, value in get_num_char_appears(filePath).items():
        print(f"{key}: {value}")
    print("============= END ===============")