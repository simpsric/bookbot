
def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(filePath):
    text_list = get_book_text(filePath).split()
    
    return f"Found {len(text_list)} total words"
    
def get_num_char_appears(filePath):
    text_list = get_book_text(filePath).split()
    char_dict = {}
    for word in text_list:
        for char in word:
            tmp_char = char.lower()
            if tmp_char in char_dict:
                char_dict[tmp_char] += 1
            else:
                char_dict[tmp_char] = 1
    char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return char_dict