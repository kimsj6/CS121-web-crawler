import sys
import os

def tokenize(text: str) -> list:

	allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789'-"
	uppercase_dict = {
    	'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i',
		'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
		'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
	}
	stop_words_list = [
    'about', 'above', 'after', 'again', 'against', 'all', 'and', 'any', 'are', "aren't", 'because', 'been', 'before',
    'being', 'below', 'between', 'both', 'but', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'does', 
    "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', 
    "hasn't", 'have', "haven't", 'having', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 
    'himself', 'his', 'how', "how's", "i'd", "i'll", "i'm", "i've", 'into', "isn't", "it's", 'its', 'itself', "let's", 
    'more', 'most', "mustn't", 'myself', 'nor', 'not', 'off', 'once', 'only', 'other', 'ought', 'our', 'ours', 
    'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 
    'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
    "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'too', 'under', 
    'until', 'very', 'was', "wasn't", "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', 
    "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', 
    "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

	tokens = []

	current_token = ""
	
	for char in text:
		if char in allowed_characters:
			current_token += char
		elif char in uppercase_dict:
			current_token += uppercase_dict[char]
		else:
			if current_token and len(current_token) > 3 and current_token not in stop_words_list:
				tokens.append(current_token)
			current_token = ""
    
	if current_token and len(current_token) > 3 and current_token not in stop_words_list:
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
