def freq_lyrics(lyrics):
    my_dict = {} #set up an empty dictionary
    for word in lyrics: #loop through all the words in lyrics
        if word in my_dict: #if the word is in the lyrics
            my_dict[word] += 1 #add word to my_dict
        else: #otherwise
            my_dict[word] = 1 #if it's not in the dictionary, just store it in the dictionary
    return my_dict

she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
                'she', 'loves', 'you', 'yeah', 'yeah',
                'she', 'loves', 'you', 'yeah', 'yeah', ]


print(freq_lyrics(she_loves_you))


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in words:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


