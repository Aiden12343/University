# is_palindrome_two_pointers

is_palindrome_two_pointers(text) FUNCTION
Return True if text reads the same both ways (ignoring case/punctuation).
REMEMBER Two pointers walk toward each other, skipping non-letters/digits; any mismatch → False.
TIME O(n). SPACE O(1).
def is_palindrome_two_pointers(text):
left_index = 0
right_index = len(text) - 1
while left_index < right_index:
while left_index < right_index and not text[left_index].isalnum():
left_index += 1
while left_index < right_index and not text[right_index].isalnum():
right_index -= 1
if text[left_index].lower() != text[right_index].lower():
return False
left_index += 1
right_index -= 1
return True
INPUT is_palindrome_two_pointers('A man, a plan, a canal: Panama')
OUTPUT True
IN PRODUCTION — the call you would actually write
BUILT-IN slicing (Python idiom) no install needed
Not a library, but the idiomatic form: clean the text, then compare it with its reverse. Uses O(n) extra memory where two pointers use
O(1).
CODE text = 'A man, a plan, a canal: Panama'
letters = [character.lower() for character in text if character.isalnum()]
letters == letters[::-1]
OUTPUT True
CS Algorithms Toolkit Array & linked-list techniques
74
