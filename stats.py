def sort_on(dict_list):
    return dict_list["char"]


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        num_words = file_content.split()
        i = 0
        for word in num_words:
            i += 1
        print("----------- Word Count ----------\n", f"\nFound {i} total words\n")
        return 


def count_words(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        count_dict = {}
        for old_char in file_content:
            char = old_char.lower()
            char_count = 0
            if char not in count_dict:
                char_count += 1
                count_dict[char] = char_count
            elif char in count_dict:
                current_char_count = count_dict[char]
                new_current_char_count = current_char_count + 1
                count_dict[char] = new_current_char_count
        return count_dict


def get_character_record(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        num_words = file_content.split()
        count_dict = {}
        temp_list = []
        number_of_words = 0

        for word in num_words:
            number_of_words += 1

        for old_char in file_content:
            char = old_char.lower()
            char_count = 0
            if char not in count_dict:
                count_dict[char] = char_count
                current_dict = {}
                char_count += 1
                current_dict["name"] = char
                current_dict["char"] = char_count
                temp_list.append(current_dict)    
            elif char in count_dict:
                for i in range (len(temp_list)):
                    indexing_list = temp_list[i]
                    if indexing_list["name"] == char:
                        indexing_list["char"] += 1
        temp_list.sort(reverse=True, key=sort_on)
        print("--------- Character Count -------\n")
        for i in temp_list:
            if i["name"].isalpha():
                print(f"{i["name"]}:",i["char"])
        return