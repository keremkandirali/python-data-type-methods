

# String Methods (45)
#
# .capitalize(), .casefold(), .center(), .count(), .endswith(), .find(), .index(), .isalnum(), .isalpha(), .isascii(), .isdecimal(), .isdigit(), .isidentifier(), .islower(), .isnumeric(), .isprintable(), .isspace(), .istitle(), .isupper(), .join(), .ljust(), .lower(), .lstrip(), .maketrans(), .partition(), .replace(), .rfind(), .rindex(), .rjust(), .rpartition(), .rsplit(), .rstrip(), .split(), .splitlines(), .startswith(), .strip(), .swapcase(), .title(), .translate(), .upper(), .format(), .format_map(), .encode(), .expandtabs() and .zfill()
#
# by Kerem Kandıralı
# https://twitter.com/keremkandirali
# https://github.com/keremkandirali


my_string = 'fAr far away.'


my_string.capitalize()
# Capitalizes the first letter of the string. Lowercases the rest.
# Far far away.


my_special_string = 'fArß far away.'
my_special_string.casefold()
# Aggresive lowercase for some special characters in caseless matching.
# farss far away.
# e.g. For 'ß' character, .lower() returns 'ß'; .casefold() returns 'ss'.


my_string.center(21)  # my_string.center(width*)
# Centers the string in the given width of characters.
#     fAr far away.
my_string.center(21, '-')  # my_string.center(width*, fillchar)
# Centers the string in the given width of characters, between the given character.
# ----fAr far away.----


my_string.count('a')  # my_string.count(sub*)
# Counts a substring in the string.
# 3
my_string.count('a', 2, 6)  # my_string.count(sub*, start, end)
# Counts a substring in the string in the given slice.
# 1


my_string.endswith('fa')  # my_string.(suffix*)
# Checks if the string ends with a suffix.
# False
my_string.endswith(('fa', '.'))  # my_string.(suffix*)
# Checks if the string ends with any of the suffixes as a tuple.
# True
my_string.endswith('fa', 2, 6)  # my_string.(suffix*, start, end)
# Checks if the given slice ends with the suffix.
# True


my_string.find('a')  # my_string.find(sub*)
# Returns the lowest index of a substring. Returns -1 if not found.
# 5
my_string.find('a', 2, 6)  # my_string.find(sub*, start, end)
# Returns the lowest index of a substring in the given slice. Returns -1 if not found.
# 5


my_string.index('a')  # my_string.index(sub*)
# Returns the lowest index of a substring. Raises ValueError if not found.
# 5
my_string.index('a', 2, 6)  # my_string.index(sub*, start, end)
# Returns the lowest index of a substring in the given slice. Raises ValueError if not found.
# 5


my_string.isalnum()
# Checks if all characters are alphabetic, decimals, digits or numerics. Which means alphanumeric.
# False (Because of the spaces and the dot.)


my_string.isalpha()
# Checks if all characters are alphabetic. (a-z)
# False (Because of the spaces and the dot.)


my_string.isascii()
# Checks if all characters are ASCII.
# True


my_string.isdecimal()
# Checks if all characters are decimals. (0-9)
# False (Because of the spaces, alphabetic characters and the dot.)


my_string.isdigit()
# Checks if all characters are decimals or digits including superscripts etc. (e.g ²)
# False (Because of the spaces, alphabetic characters and the dot.)


my_string.isidentifier()
# Checks if the string is a valid Python identifier.
# False
# P.S. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).


my_string.islower()
# Checks if all characters are lowercase.
# False (Because of the 'A' character.)


my_string.isnumeric()
# Checks if all characters are decimals, digits or numerics including Chinese etc. (e.g 四)
# False (Because of the spaces, alphabetic characters and the dot.)


my_string.isprintable()
# Checks if all characters are digits, ASCII, punctuation or whitespace.
# True


my_string.isspace()
# Checks if all characters are whitespace. ( \t\n\r\x0b\f)
# False (Because of the alphabetic characters and the dot.)


my_string.istitle()
# Checks if all words starts with an uppercase character.
# False


my_string.isupper()
# Checks if all characters are uppercase.
# False


'-'.join(my_string)  # ''.join(str*)
# Adds the given character after each index of the string, except the last one.
# f-A-r- -f-a-r- -a-w-a-y-.


my_string.ljust(17)  # my_string.ljust(width*)
# Adds spaces to the right of the string until the given width of characters are complete.
# fAr far away.
my_string.ljust(17, '-')  # my_string.ljust(width*, fillchar)
# Adds the given character to the right of the string until the given width of characters are complete.
# fAr far away.----


my_string.lower()
# Lowercases the string.
# far far away.


my_string.lstrip()
# Removes the spaces from the left side of the string.
# fAr far away.
my_string.lstrip('fy.')  # my_string.lstrip(chars)
# Removes the given characters from the left side of the string.
# Ar far away.


# my_string.maketrans()
#
#


my_string.partition('a')  # my_string.partition(sep*)
# Returns a 3-item tuple including the part before the first occurrence of the separator, the separator itself and the part after the separator.
# ('fAr f', 'a', 'r away.')


my_string.replace('a', 'x')  # my_string.replace(old*, new*)
# Replace a character or a substring with a new character or substring.
# fAr fxr xwxy.
my_string.replace('a', 'x', 2)  # my_string.replace(old*, new*, count)
# Replace a character or a substring with a new character or substring until the given number is complete.
# fAr fxr xway.


my_string.rfind('a')  # my_string.rfind(sub*)
# Returns the highest index of a substring. Returns -1 if not found.
# 10
my_string.rfind('a', 2, 6)  # my_string.rfind(sub*, start, end)
# Returns the highest index of a substring in the given slice. Returns -1 if not found.
# 5


my_string.rindex('a')  # my_string.rindex(sub*)
# Returns the highest index of a substring. Raises ValueError if not found.
# 10
my_string.rindex('a', 2, 6)  # my_string.rindex(sub*, start, end)
# Returns the highest index of a substring in the given slice. Raises ValueError if not found.
# 5


my_string.rjust(17)  # my_string.rjust(width*)
# Adds spaces to the left of the string until the given width of characters are complete.
#     fAr far away.
my_string.rjust(17, '-')  # my_string.rjust(width*, fillchar)
# Adds the given character to the left of the string until the given width of characters are complete.
# ----fAr far away.


my_string.rpartition('a')  # my_string.rpartition(sep*)
# Returns a 3-item tuple including the part before the last occurrence of the separator, the separator itself and the part after the separator.
# ('fAr far aw', 'a', 'y.')


my_string.rsplit()
# Splits the words in the string and returns them as a list.
# ['fAr', 'far', 'away.']
my_string.rsplit(' ', 1)  # my_string.(sep, maxsplit)
# Starts from the right and splits the words in the string by the given substring until the given number is complete and returns them as a list.
# ['fAr far', 'away.']


my_string.rstrip()
# Removes the spaces from the right side of the string.
# fAr far away.
my_string.rstrip('fy.')  # my_string.rstrip(chars)
# Removes the given characters from the right side of the string.
# fAr far awa


my_string.split()
# Splits the words in the string and returns them as a list.
# ['fAr', 'far', 'away.']
my_string.split(' ', 1)  # my_string.(sep, maxsplit)
# Splits the words in the string by the given substring until the given number is complete and returns them as a list.
# ['fAr', 'far away.']


my_lined_string = 'Far\nfar\naway.'
my_lined_string.splitlines()
# Splits the string at line breaks and returns them as a list.
# ['Far', 'far', 'away.']
my_lined_string.splitlines(True)  # my_lined_string.splitlines(keepends)
# Splits the string at line breaks and returns them as a list, including the line breaks.
# ['Far\n', 'far\n' 'away.']


my_string.startswith('fA')  # my_string.(prefix*)
# Checks if the string starts with a prefix.
# True
my_string.startswith(('fa', '.'))  # my_string.(prefix*)
# Checks if the string starts with any of the prefixes as a tuple.
# False
my_string.startswith('r', 2, 6)  # my_string.(prefix*, start, end)
# Checks if the given slice starts with the prefix.
# True


my_string.strip()
# Removes the spaces from the left and the right side of the string.
# fAr far away.
my_string.strip('fy.')  # my_string.strip(chars)
# Removes the given characters from the left and the right side of the string.
# Ar far awa


my_string.swapcase()
# Uppercases the lowercase characters and lowercases the uppercase ones.
# FaR FAR AWAY.


my_string.title()
# Capitalizes the first letter of each word in the string. Lowercases the rest.
# Far Far Away.


# my_string.translate()
#
#


my_string.upper()
# Capitalizes all the characters in the string.
# FAR FAR AWAY.


my_formatted_string = 'My name is {}, my midname is {} and my last name is {}.'
my_formatted_string.format('John', 'Mike', 'Doe')
# My name is John, my midname is Mike and my last name is Doe.
my_formatted_string = 'My name is {0}, my midname is {2} and my last name is {1}.'
my_formatted_string.format('John', 'Doe', 'Mike')
# My name is John, my midname is Mike and my last name is Doe.
my_formatted_string = 'My name is {name}, my midname is {midname} and my last name is {lastname}.'
my_formatted_string.format(name='John', midname='Mike', lastname='Doe')
# My name is John, my midname is Mike and my last name is Doe.
# Formats the string allowing multiple substitions and value formatting.


my_formatted_string = 'My name is {name}, my midname is {midname} and my last name is {lastname}.'
my_formatted_string.format_map({'name': 'John', 'midname': 'Mike', 'lastname': 'Doe'})  # my_formatted_string.format_map(dict*)
# Formats the string with a dictionary allowing multiple substitions and value formatting.
# My name is John, my midname is Mike and my last name is Doe.


my_encoded_string = 'ç'
my_encoded_string.encode()
# Returns encoded version of the string.
# b'\xc3\xa7'
my_encoded_string.encode(encoding='UTF-8', errors='strict')
# Default encoding is UTF-8 and default errors is 'strict'. errors stands for the response when encoding fails.
# https://www.utf8-chartable.de/unicode-utf8-table.pl
# https://docs.python.org/3/library/codecs.html#standard-encodings


my_tabbed_string = '\tFar\tfar\taway\t.'
my_tabbed_string.expandtabs()
# Replaces the tabs (\t) in the string with 8 spaces. Characters until the next tab is included in tabsize.
#        Far     far     away    .
my_tabbed_string.expandtabs(12)  # my_tabbed_string.expandtabs(tabsize)
# Replaces the tabs (\t) in the string with the given number of spaces. Characters until the next tab is included in tabsize.
#            Far         far         away        .


my_number_string = '6'
my_number_string.zfill(3)  # my_string.zfill(width*)
# Adds 0 to the left of the string until the given width of characters are complete.
# '006'


# (*) required
