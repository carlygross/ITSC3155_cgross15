# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  d = dict()
  for m in n:
    if m not in d:
      d[m] = 1
    else:
      d[m] = d[m] + 1

  return int(max(d, key=d.get))

  #count = 0
  #for i in range(1, n+1):
  #  if i % 3 == 0:
  #    count += 1

  #return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  letters = dict()
  count = 0

  for i in range(len(s)):
    new_count = 1

    for j in range(i + 1, len(s)):
      if s[i] != s[j]:
        break
      else:
        new_count += 1

      if new_count > count:
        count = new_count

      letters[s[i]] = count

  list_letters = []
  for key, value in letters.items():
    list_letters.append(letters[key])

  list_letters.sort(reverse=True)
  #print(list_letters)
  #print(letters)

  highest = list_letters[0]
  highest_list = []

  for value in letters:
    if highest == letters[value]:
      highest_list.append(value)

  #print(highest_list)

  return highest_list












  #count = 0
  #letter = s[0]
  #for i in range(len(s)):
  #  counts = 1
  #  for j in range(i + 1, len(s)):
   #   if s[i] != s[j]:
   #     break
   #   counts += 1

   #   if counts > count:
    #    count = counts
    #    letter = s[i]
  #return letter



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  s = s.lower()
  s = s.replace(" ", "")

  for i in range(len(s) - 1):
    if s[i] == s[len(s) - 1 - i]:
      continue
    else:
      return False
  return True
