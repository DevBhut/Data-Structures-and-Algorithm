'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

# def checkValidString(s: str) -> bool:
#     left = 0
#     right = 0
#     star = 0
#     for x in s:
#         if x == '(':
#             left += -1
#         elif x == ')':
#             right += 1
#         elif x == '*':
#             star += 1
#     if left+right == 0:
#         return True
#     elif abs(left+right) <= abs(star):
#         return True
#     else: 
#         return False
# Does not work, cause does not check validness ie for every left bracket we have a right bracket 

def checkValidString(s: str):
    left, right = 0, 0
    for x in s:
        if x == '(':
            left, right = left + 1, right + 1
        elif x == ')':
            left, right = left - 1, right - 1
        elif x == '*':
            left, right = left - 1, right + 1
        if right < 0:
            return False
        if left < 0:
            left = 0
    return left == 0
    

s = "(((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)"
t = "                    "
l = 27 
r = 14
st = 15

print(checkValidString(s))