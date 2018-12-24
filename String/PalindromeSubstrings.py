# Given a string find all substrings that are palindromes.
# A palindrome is a word, phrase, number, or other sequence
# of characters which reads the same backwards as it reads
# forwards.

# input -> aabbbbaa
# output -> aa, bb, bbb, abbba, aabbbbaa, bb, aa
# O(n^3), and memory o(1)

# A naive solution of this problem is to find all substrings of
# a given string and check whether each substring is a palindrome 
# or not
def is_palindrome(input, i, j):
  while j > i:
    if input[i] != input[j]:
      return False
    i += 1
    j -= 1

  return True

def find_all_palindrome_substrings(input):
  count = 0

  for i in range(0, len(input)):
    for j in range(i + 1, len(input)):
      if is_palindrome(input, i, j):
        print(input[i:j + 1]),
        count += 1

  print("\n")
  return count

find_all_palindrome_substrings("aabbbaa")
# aa, aabbbaa, abbba bb, bbb, bb, aa

# Solution 2 O(n^2) and O(1)
# For each letter in the input string, start expanding to left
# and right while checking for even and odd length palindromes.
# Move to the next letter if we know a palindrome doesn't exist.

# We expand one character to the left and right and compare
# them. If both of them are equal, we print out the palindrome
# substring.

def find_palindromes_in_sub_string(input, j, k):
  count = 0
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    print(input[j: k + 1]) 
    count += 1

    j -= 1
    k += 1

  return count


def find_all_palindrome_substrings2(input):
  count = 0
  for i in range(0, len(input)):
    count += find_palindromes_in_sub_string(input, i - 1, i + 1)
    count += find_palindromes_in_sub_string(input, i, i + 1)

  print("\n")
  return count
find_all_palindrome_substrings2("aabbbaa")
# aa, bb, bbb, abbba, aabbbbaa, bb, aa