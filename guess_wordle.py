import sys

if __name__ == "__main__":
	print("Processing guess results...")
	
	# Read words and all possible guess results
	words_file = open("words.csv", 'r')
	words = []
	for line in words_file:
		guess_results = line.rstrip(' ,\n').split(',')
		solution = guess_results.pop(0)
		words.append((solution, guess_results))
	
	# Read others' guess results
	guesses_file = open(sys.argv[1], 'r')
	guesses = []
	for line in guesses_file:
		guesses.extend(line.rstrip(' ,\n').replace(' ','').split(','))
	guesses = set(guesses)
	
	# Get and return candidates
	candidates = []
	for word, guess_results in words:
		if guesses.issubset(guess_results):
			candidates.append(word)
	
	print("Candidates found:")
	for candidate in candidates:
	  print(candidate)