
def num_letters(num_rows, num_columns):
    return 2 * num_rows + 2 * num_columns - 4

# Check the function with assertions
assert num_letters(3, 4) == 10
assert num_letters(4, 4) == 12
assert num_letters(6, 4) == 16
assert num_letters(6, 7) == 22
assert num_letters(2, 5) == 10

print("Checking assertions.")

import numpy as np

data = np.loadtxt("loop4.csv", delimiter=",",
                  dtype=str, encoding="utf-8-sig")

words = []

rows, columns = data.shape

# Collect letters across the top row
r = 0
c = 0
while c < columns:
    words.append(data[r,c].strip())
    c = c + 1

# Collect letters across the bottom row
r = rows - 1
c = columns - 1
while c >= 0:
    words.append(data[r,c].strip())
    c = c - 1

# Collect letters down the right side
r = 1
c = columns - 1
while r < rows - 1:
    words.append(data[r,c].strip())
    r = r + 1

# Collect letters up the left side
r = rows - 2
c = 0
while r > 0:
    words.append(data[r,c].strip())
    r = r - 1

print(words)

assert len(words) == num_letters(rows, columns)
print("Part 3 passed!")

# PART 4: Collect two-letter words

two_letter_words = []

# Top row - move left to right
r = 0
c = 0
while c < columns - 1:
    word = data[r,c].strip() + data[r,c+1].strip()
    two_letter_words.append(word)
    c = c + 1

# Bottom row - move right to left
r = rows - 1
c = columns - 1
while c > 0:
    word = data[r,c].strip() + data[r,c-1].strip()
    two_letter_words.append(word)
    c = c - 1

# Right side - move downward
r = 0
c = columns - 1
while r < rows - 1:
    word = data[r,c].strip() + data[r+1,c].strip()
    two_letter_words.append(word)
    r = r + 1

# Left side - move upward
r = rows - 1
c = 0
while r > 0:
    word = data[r,c].strip() + data[r-1,c].strip()
    two_letter_words.append(word)
    r = r - 1

print("Two-letter words:")
print(two_letter_words)

assert len(two_letter_words) == num_letters(rows, columns)
print("Part 4 passed!")

