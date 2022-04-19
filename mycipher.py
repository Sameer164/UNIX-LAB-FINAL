import sys

def cipher(text, key):
	text = text.upper()
	start = 65
	new_text = ""
	for char in text:
		if 65 <= ord(char) <= 90:
			asc = (ord(char)-start + key) % 26
			new_text += chr(asc+start)
	return new_text



all_lines_ciphered = []
key = int(sys.argv[1])
for lines in sys.stdin:
	all_lines_ciphered.append(cipher(lines, key))


lines = "".join(all_lines_ciphered)
i = 0
new = ""
count= 0
while i < len(lines):
	if count == 10:
		count = 0
		new += "\n"
	blc = lines[i:i + 5]
	new += blc + " "
	count += 1
	i += 5

print(new)



## FINISHED!!
