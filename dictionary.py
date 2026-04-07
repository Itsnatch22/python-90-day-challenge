words = ['apple', 'banana', 'cherry', 'date', 'elderberry'
         , 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

def word_dict(word_list):
    word_dictionary = {}
    for word in word_list:
        word_dictionary[word] = len(word)
    return word_dictionary
if __name__ == "__main__":
    result = word_dict(words)
    print(result)