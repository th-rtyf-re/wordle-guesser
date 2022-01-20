if __name__ == "__main__":
	print("Processing guess results...")
	
	words_file = open("words.csv", 'r')
	guesses_file = open("guesses.csv", 'r')
	
	words = []
	for line in words_file:
		guess_results = line.rstrip(' ,\n').split(',')
		solution = guess_results.pop(0)
		words.append([solution, guess_results])
	
	guesses = []
	for line in guesses_file:
		guesses.extend(line.rstrip(' ,\n').replace(' ','').split(','))
	guesses = set(guesses)
	
	candidates = []
	for word, guess_results in words:
		if guesses.issubset(guess_results):
			candidates.append(word)
	
	print("Candidates found:")
	for candidate in candidates:
	  print(candidate)