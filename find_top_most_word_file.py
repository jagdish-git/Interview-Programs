def find_top_ten_repeated_word():
    with open("large_text_file.txt", "r+") as file:
        f = file.readlines()
        
    store_word_dict = dict()
    translation_table = str.maketrans('', '', '.,!')
    for word in f[0].split():
        word_filter = word.translate(translation_table).lower()
        store_word_dict[word_filter] = store_word_dict.get(word_filter, 0) + 1

    sorted_word_dict = dict(sorted(store_word_dict.items(), key= lambda x:x[1], reverse=True))
    count = 0
    for rept_word in sorted_word_dict:
        yield rept_word
        count += 1
        if count >= 10:
            break


print(list(find_top_ten_repeated_word()))


# counter and regex
from collections import Counter
import re 

def find_top_repeated_words(file_path, top_n=10):
    word_counter = Counter()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                word_counter.update(words)
        top_ten_word = word_counter.most_common(top_n)
        return top_ten_word
    except FileNotFoundError as fe:
        print(fe)
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    file_path = "large_text_file.txt"
    top_n = 10
    result = find_top_repeated_words(file_path, top_n)
    all_ten_word = []
    if result:
        print(f"Top {top_n} most repeated words:")
        for word, count in result:
            all_ten_word.append(word)
            # print(f"{word}: {count}")
    print(all_ten_word)