# Challenge

Your challenge, should you choose to accept it, is to write a program that meets the requirements listed below. Feel free to implement the program in the language of your choice (Go, Ruby, or Python are preferred if you're choosing between languages).

1. The program accepts as arguments a list of one or more file paths (e.g. ./solution.rb file1.txt file2.txt ...). 
2. The program also accepts input on stdin (e.g. cat file1.txt | ./solution.rb). 
3. The program outputs a list of the 100 most common three word sequences in the text, along with a count of how many times each occurred in the text. For example: `231 - i will not, 116 - i do not, 105 - there is no, 54 - i know not, 37 - i am not …`
4. The program ignores punctuation, line endings, and is case insensitive (e.g. “I love\nsandwiches.” should be treated the same as "(I LOVE SANDWICHES!!)") 
5. The program is capable of processing large files and runs as fast as possible. 
6. The program should be tested. Provide a test file for your solution.

So, set your own pace. No rush. And just so you have some bounds, the challenge was designed to take somewhere between 2 and 3 hours. You could try it against "Origin Of Species" as a test: http://www.gutenberg.org/cache/epub/2009/pg2009.txt .
