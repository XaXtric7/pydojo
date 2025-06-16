def remove_word(word_list, word_to_remove):
    word_to_remove = word_to_remove.strip()
    # Create a new list excluding the stripped target word
    return [word.strip() for word in word_list if word.strip() != word_to_remove]


words = ["  apple", "banana  ", "  cherry ", "banana"]
cleaned_list = remove_word(words, " banana ")
print(cleaned_list)
