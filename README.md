# codeSnippetSorting
# Coding Challenge: Sorting Strings

## Lenka Kovalcinova


### Problem Statement:

 - Input:  list of strings containing integers and words 
 - Output: sorted version of the list: 
     - All words are in alphabetical order.
     - All integers are in numerical order.
     - If the nth element in the list is an integer it must remain an integer, and if it is a word it must remain a word. 
     - Only ascii symbols that belong to letter set nor digit set (i.e. "#", "%", ";", etc are not allowed). 
     
### Examples:
==========================================================

Input String:  "sym\*bo+l"    

Ouptut String: "symbol"

--

Input String: "12%3"

Output String: "123"

--

Input String Array:  20 cat bi?rd 12 do@g 

Output String Array: 12 bird cat 20 dog

==========================================================

### I/O instructions and format:

**Input:** file that includes a single, possibly empty, line containing a space-separated list of strings to be sorted. 
   - Words will not contain spaces, will contain upper-case, lower-case letters a-z and maybe non-letter-non-digit characters. 
   - Integers will be in the range -999999 to 999999, and might also contain non-letter-non-digit characters. 

**Output:** file named "result.txt"
   - The list of strings, sorted per the requirements above. 
   - Strings must be separated by a single space, with no leading space at the beginning of the line or trailing space at the end of the line. 

   - The program should take the input file name as the first argument, output file as the second argument:

	root:#  ./listSorting.py <path-to-input-file>/list.txt <path-to-output-file>/result.txt 


## Code Solution
