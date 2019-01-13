# Given a string of opening and closing parentheses, check whether it’s balanced.
# We have 3 types of parentheses: round brackets: (), square brackets: [], 
# and curly brackets: {}. Assume that the string doesn’t contain any other 
# character than these, no spaces words or numbers. As a reminder, 
# balanced parentheses require every opening parenthesis to be closed in the 
# reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
def balance_check(s):
 
 # Check is even number of brackets
 if len(s) % 2 != 0:
     return False
 
 # Set of opening brackets
 opening = set('([{') 
 
 # Matching Pairs
 matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
 
 # Use a list as a "Stack"
 stack = []
 
 # Check every parenthesis in string
 for paren in s:
    # If its an opening, append it to list
    if paren in opening:
        stack.append(paren)
 
    else:
        # Check that there are parentheses in Stack
        if len(stack) == 0:
            return False
            # Check the last open parenthesis
        last_open = stack.pop()
        # Check if it has a closing match
        if (last_open,paren) not in matches:
            return False
 
 return len(stack) == 0

print(balance_check('[](){([[[]]])}')) # True