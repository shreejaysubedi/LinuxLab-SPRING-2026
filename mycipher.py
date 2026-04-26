import sys

def encode(text, shift):
    result = []
    for ch in text.upper():
        if ch.isalpha():
            encoded = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result.append(encoded)
    return result

shift = int(sys.argv[1])
letters = []

for line in sys.stdin:
    letters.extend(encode(line, shift))

# Group into blocks of 5
blocks = [''.join(letters[i:i+5]) for i in range(0, len(letters), 5)]

# Print 10 blocks per line
for i in range(0, len(blocks), 10):
    print(' '.join(blocks[i:i+10]))
