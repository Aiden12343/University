# edit_distance

edit_distance(first_text, second_text) FUNCTION
Return the minimum inserts/deletes/substitutions to turn one into the other.
REMEMBER cell = cheapest way to convert first a chars into first b chars. Equal chars: copy the diagonal. Otherwise 1 +
min(delete = up, insert = left, substitute = diagonal). Only the previous row is needed.
WHEN TO USE Spell-check suggestions, fuzzy matching, DNA comparison.
REQUIRES Two strings (Levenshtein distance, all edits cost 1).
TIME O(m × n). SPACE O(n) with the two-row trick used here.
USED FOR "Did you mean...?", autocorrect, record linkage.
def edit_distance(first_text, second_text):
previous_row = list(range(len(second_text) + 1)) # turning "" into prefix
for first_position in range(1, len(first_text) + 1):
current_row = [first_position] # turning prefix into ""
for second_position in range(1, len(second_text) + 1):
substitution_cost = 0 if first_text[first_position - 1] == second_text[second_position - 1]
↳ else 1
current_row.append(min(
previous_row[second_position] + 1, # delete
current_row[second_position - 1] + 1, # insert
previous_row[second_position - 1] + substitution_cost)) # substitute
previous_row = current_row
return previous_row[-1]
INPUT edit_distance('kitten', 'sitting')
OUTPUT 3
IN PRODUCTION — the call you would actually write
THIRD-PARTY rapidfuzz.distance.Levenshtein pip install rapidfuzz
The standard library has no edit distance (difflib.get_close_matches is fuzzy but not Levenshtein). RapidFuzz is the fast, maintained choice;
it also offers process.extractOne for 'did you mean?' lookups.
CODE from rapidfuzz.distance import Levenshtein
Levenshtein.distance('kitten', 'sitting')
OUTPUT 3
CS Algorithms Toolkit Dynamic programming
54
