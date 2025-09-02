def count_words(content):
    words = content.split()
    letters_number = len(words)
    return letters_number

def count_characters(content):
    dictionary = {}
    formated = content.lower()
    for word in formated:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    #print(dictionary)
    return dictionary

def sort(dictionary):
    list_dictionary = []
    for key in dictionary:
        value = dictionary[key]
        dictionary_pair = {"char":key, "num":value}
        list_dictionary.append(dictionary_pair)
        list_dictionary.sort(reverse=True, key=sort_on)
    #print(list_dictionary)
    return list_dictionary

def sort_on(dictionary):
    return dictionary["num"]



