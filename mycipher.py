import sys

def cipher(text, key):
	text = text.upper()
	start = 65
	new_text = ""
	for char in text:
		asc = (ord(char)-start + key) % 26
		new_text += chr(asc)
	return new_text



all_lines_ciphered = []
key = int(sys.argv[1])
for lines in sys.stdin:
	all_lines_ciphered.append(cipher(lines, key))

for lines in all_lines_ciphered:
	blocks = []
	i = 0
	while i < len(lines):
		blocks.append(lines[i:i+5])
		i += 5
	new_str = " ".join(blocks)
	sys.stdout.write(new_str)

## FINISHED!!
