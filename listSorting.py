
### function that cleans and characterizes a string: find whether a a string is an integer 
## and remove all non-intger, non-letter characters

def cleanIsWord(string):
	clean = ''.join(character for character in string if character.isalnum() or character == '-') # get rid of all non aplhanumeric expressions
	if clean:
		trueOrFalse = False
		minuses = 0
		for character in clean:
# if any of the characters in clean is not a digit but a letter form alphabet, the string is considered to be a word
			if not (character.isdigit() or (character == '-' and minuses == 0)):
				trueOrFalse = True
			if character == '-':
				minuses += 1
		return(clean, trueOrFalse) # returns false, if not word
	else :
		return('', True) # returns '' and true if clean is empty

## reads the file and returns the array with strings
def readLineParse(filename):
	with open(filename) as f:
		content = f.readlines()
	if content:
		content = content[0]
		stringArray = content.split()
		return(stringArray)
	else:
		return([])

## splits an array into two subarrays and the indicator array to indicate integers in the
## original string array

## returns list of words, integers and integer indicator list
def splitArrayIndicateIntegers(stringArray):
	indicateIntegers = []
	words = []
	integers = []
    
	if stringArray:
		for item in stringArray:
			cleanString, isWord = cleanIsWord(item)
            
			if isWord: ## checking if word 
				if cleanString: ## check if the string is empty after cleaning
					words.append(cleanString)
					indicateIntegers.append(0)
			else:
				indicateIntegers.append(1)
				integers.append(int(cleanString))

		return(words, integers, indicateIntegers)        
	else :
		return([],[],[])

## sorting the arrays and return the sorted merged array of words and integers

def sortWordsIntegers(words, integers, indicateIntegers):

	def lowerWords(words):
		newWords = []
		for word in words:
			newWords.append(word.lower())
		return(newWords)

	sorted(words, reverse = True, key = lowerWords)
	integers.sort(reverse = True)

	stringArray = indicateIntegers
    
	for ind in range(len(stringArray)):
		if stringArray[ind]:
			stringArray[ind] = str(integers.pop())
		else:
			stringArray[ind] = words.pop()
	return(stringArray)
## output the file

def outputArrayToFile(stringArray, outputFile):
	outputFile = open(outputFile, 'w')
	line = " ".join(word for word in stringArray)
	outputFile.write(line)

import sys

def main():
	if len(sys.argv) != 3:
		print ('usage: ./listSorting.py <path-to-input-file>/list.txt <path-to-output-file>/result.txt')
		sys.exit(1)
# load the file
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	stringArray = readLineParse(inputFile)

## split the array into array of words, integers and indicate integer positions
	words, integers, indicateIntegers = splitArrayIndicateIntegers(stringArray)

## sort words and output into the file
	stringArray = sortWordsIntegers(words, integers, indicateIntegers)
	outputArrayToFile(stringArray, outputFile)

if __name__ == '__main__':
  main()

