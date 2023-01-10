def countWords(s): 
    if s.strip() == "":
		return 0
	words = s.split()
	return len(words)
if __name__ == "__main__":
	s = "One two	 three\n four\tfive "
	print("No of words : ", countWords(s))
