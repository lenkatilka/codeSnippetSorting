import unittest
from  listSorting import sortWordsIntegers, splitArrayIndicateIntegers, cleanIsWord

class stringTests(unittest.TestCase):
	"""The test function here tests for the code in listSorting.py"""
	def testTheEmptyString(self):
		"""See whether the empty string correctly returns the empty string"""
		words, integers,  indicateIntegers = splitArrayIndicateIntegers('')
		self.assertFalse(sortWordsIntegers(words, integers, indicateIntegers ))


	"""See whether the non-alphanumeric string correctly returns the empty string"""
	def testNonAplhaNumeric(self):
		words, integers,  indicateIntegers = splitArrayIndicateIntegers('#^&*&')
		self.assertFalse(sortWordsIntegers(words, integers, indicateIntegers ))

	def testNumeric(self):
		"""See whether the numeric string correctly returns the numeric string"""
		words, integers,  indicateIntegers = splitArrayIndicateIntegers('1')
		words = sortWordsIntegers(words, integers, indicateIntegers)
		self.assertTrue(words[0].isdigit())
		
	def testAlphabetic(self):
		"""See whether the numeric string correctly returns the numeric string"""
		words, integers,  indicateIntegers = splitArrayIndicateIntegers('ajd')
		words = sortWordsIntegers(words, integers, indicateIntegers)
		self.assertFalse(words[0].isdigit())


	def testNegative(self):
		""" Check the negative numbers """
		number, word = cleanIsWord('-123')
		self.assertFalse(word)

	def testTwoNegativeSigns(self):
		""" Check the double negative sign occurence in the string, if yes, then its a word"""
		number, word1 = cleanIsWord('--123')
		number, word2 = cleanIsWord('-1-23')
		self.assertTrue(word1 and word2)

class checkSorting(unittest.TestCase):
	"""Check the sorting"""
	
	def testTwoNumbersSort(self):
		"""Check the positive and negative number sorting"""
		words, integers,  indicateIntegers = splitArrayIndicateIntegers(['23', '-23'])
		array = sortWordsIntegers(words, integers, indicateIntegers )
		self.assertTrue( array[0] < array[1] )
		
	def testUpperLowerSort(self):
		"""Check the upper and lower case character sorting"""
		words, integers,  indicateIntegers = splitArrayIndicateIntegers(['B', 'a'])
		array = sortWordsIntegers(words, integers, indicateIntegers )
		self.assertTrue( array[0].lower() < array[1].lower() )

		

if __name__ == '__main__':
        unittest.main()

