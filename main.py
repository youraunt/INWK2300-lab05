import string

# from collections import Counter
#
# def main(s):
#     l = s.split()
#     c = Counter(l)
#     for k,v in c.items():
#         print(k,v)
#
# if __name__ == "__main__": main("When I find myself in times of trouble Mother Mary comes to me Speaking words of
# wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be
# Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living
# in the world agree There will be an answer let it be For though they may be parted there is still a chance that
# they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let
# it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let
# it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine
# until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be
# Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah
# let it be Whisper words of wisdom let it be")
#
# """""
#    The with statement replaces try finally blocks
#    the form is
#    with expression [as variable]:
#    followed by the with block
#    this is a encapsulation technique
#    which makes the code more reusable
#    and closes the file automatically!!
#  """
# with open('input.txt') as input_data:
#     # read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
#
#     # strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
#     #     characters (space is the default leading character to remove)
#
#     # strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
#     #  characters (space is the default leading character to remove)
#     #  You can specify the separator, I used the default separator, whitespace.
#
#     words = input_data.read().strip().split()
# # the dict() constructor creates an empty dictionary
# # A dictionary is a data structure which is unordered, changeable and indexed.
# word_count_dict = dict()
# # for loop to iterate over the list 'words' word by word converting
# for word in words:
#     # if the current word is already in the dictionary word_count_dict
#     # add one to the current count
#     if word in word_count_dict:
#         word_count_dict[word] += 1
#     #     else this must be the first time encountering a word
#     #     add it to the dictionary with a count of 1
#     else:
#         word_count_dict[word] = 1
#         # map(<function>, <iterable>)
#         # The map function executes a specified function for each item in an iterable.
#         # The item is sent to the function as a parameter.
#         # map() passes each item of the iterable to this function.
#         # @param string is a call to the string() function
#         # which converts the specified value into a string.
#         # @param count is a call to the count() function
#         # which counts how many times a given object occurs in a tuple(tuples are immutable).
# word_count = [map(str, count) for count in word_count_dict.items()]
# # open outfile stream to write data
# # join word and word count separated by whitespace
# with open('output.txt', "w") as output_data:
#     # this is to ignore the newline character for the first write
#     output_data.write(' '.join(word_count[0]))
#     # iterate over word_count
#     for count in word_count[1:]:
#         output_data.write('\n' + ' '.join(count))


# ###################### version 0.3


# The with statement replaces try finally blocks
# the form is:
# with expression [as variable]:
# followed by the with block
# this is a encapsulation technique
# which makes the code more reusable
# and closes the file automatically!
# open defaults to 'rt' so a second param is unnecessary here
# read() method returns the specified number of bytes from the file.
#   Default is -1 which means the whole file.
with open('input.txt') as input_data:
    text = input_data.read()
# This uses the three param version of str.maketrans
# the syntax is <a,b,c>
# where a and be need to be equal length strings
# chars in a are replaced by chars in b
# c needs to be a string in our case it's string.punctuation
# string.punctuation contains < !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ >
# every time one of the symbols above occurs it maps to None
# this eliminates the punctuation from the file and returns conditioned text
conditioned_text = text.translate(str.maketrans('', '', string.punctuation))
# strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
#   characters (space is the default leading character to remove)
# strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
#   characters (space is the default leading character to remove)
#   You can specify the separator, I used the default separator, whitespace.
conditioned_text = conditioned_text.strip().split()
# A lambda is an inline function I am using it here to condition the text to all lowercase
# this is necessary to sort correctly because
# capital 'A' starts at ascii 65d and lowercase 'a' starts at ascii 97d
# sort sorts in ascii value so A-Z then a-z
# comment out for rosalind
conditioned_text.sort(key=lambda x: x.lower())
# create dict
word_count_dict = dict()
# for loop over pre-conditioned data
# if word in word dict is already in word_count_dict add one to the count
# else store original value as 1
for word in conditioned_text:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1
# Syntax = map(<function>, <iterable>)
# The map function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# map() passes each item of the iterable to this function.
# @param string is a call to the string() function
# which converts the specified value into a string.
# @param count is a call to the count() function
# which counts how many times a given object occurs in a tuple(tuples are immutable).
word_count = [map(str, count) for count in word_count_dict.items()]
# open outfile stream to write data
# join word and word count separated by whitespace
with open('output.txt', 'w') as output_data:
    output_data.write(' '.join(word_count[0]))
    for count in word_count[:]:
        output_data.write(' '.join(count) + '\n')
