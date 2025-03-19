def get_num_words(text):
    all_words = text.split()
    return len(all_words)

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()

        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_count(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        char_list.append(char_info)
    def sort_on(dict_item):
        return dict_item["count"]
    char_list.sort(reverse=True, key=sort_on)

    return char_list