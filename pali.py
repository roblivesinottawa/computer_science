# def is_palindrome(word):
#     for i in range(0, int(len(word) / 2)):
#         if word[i] != word[len(word) - i - 1]:
#             return False
#     return True


def is_palindrome(word):
    return word == word[::-1]

# user_input = input("enter a word to check if it's palindrome: ")
# print(is_palindrome(user_input))


def is_palindrome(string):

    def tochars(string):
        string = string.lower() #convert all to lowercase
        answer = "" # no spaces
        for char in string: #if it's a letter, add it to answer
            if char in "abcdefghijklmnopqrstuvwxyz":
                answer += char
        return answer

    def ispal(string):
        if len(string) <= 1: # a string of length 0 or 1 is a palindrome
            return True
        else:
            # if first character matches last character, it is a palindrome if middle also matches
            return string[0] == string[-1] and ispal(string[1:-1]) #checks the middle section
    return ispal(tochars(string))

print(is_palindrome("kayak"))
