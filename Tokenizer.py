import sys
import os

def tokenize(text: str) -> list:

	allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
	uppercase_dict = {
    	'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
		'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
		'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
	}

	tokens = []

	current_token = ""
	
	for char in text:
		if char in allowed_characters:
			current_token += char
		elif char in uppercase_dict:
			current_token += uppercase_dict[char]
		else:
			if current_token:
				tokens.append(current_token)
				current_token = ""
    
	if current_token:
		tokens.append(current_token)
	
	return tokens
					

def compute_word_frequencies(tokens: list) -> dict:
	"""
	Runtime Complexity: Runs in linear time (O(n)) relative to the size of the input. The method iterates
	through every token in the list and performs a constant time (O(1)) search to check if the token is
	already present in the frequency dictionary (searching dictionary takes constant time in Python since
	it uses a hash table). Then it performs another constant time operation depending on the search result,
	either adding 1 to a retrieved value or adding a new dictionary entry. Therefore, the entire method
	runs in linear time relative to the size of the input.
	"""
	frequencies = {}
	for token in tokens:
		if token in frequencies:
			frequencies[token] += 1
		else:
			frequencies[token] = 1
	
	return frequencies

def print_frequencies(frequencies: dict) -> None:
	"""
	Runtime Complexity: Runs in linear time (O(n)) relative to the size of the input. The method iterates
	through every entry in the dictionary and performs a constant time (O(1)) operation of printing the
	entry. Therefore, the entire method runs in linear time relative to the size of the input.
	"""
	for token, frequency in frequencies.items():
		print(f"{token} - {frequency}")

if __name__ == '__main__':
	tokens = tokenize(sys.argv[1])
	freqs = compute_word_frequencies(tokens)
	print_frequencies(freqs)
