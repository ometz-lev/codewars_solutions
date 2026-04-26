#Function that takes a number as an argument and returns even or odd based on the number.
def even_or_odd(number):
    return ("Even") if number % 2 == 0 else ("Odd")

#Function that converts a number to string.
def number_to_string(num):
    return str(num)

#Function that removes all spaces from a string.
def no_space(x):
    return x.replace(' ' ,'')

#Function that that takes a sentence and count the number of vowels in the sentence.
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count +=1
    return count