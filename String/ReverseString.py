# In order to reverse a string using recursion we need to consider what a base
# and recursive case would look like. Here we've set a base case to be when
# the length of the string we are passing through the function is length less
# than or equal to 1. During the recursive case we grab the first letter and
# add it on to the recursive call.
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Hello World")) #dlroW olleH