from hashlib import new


def anagrams_for(word, list_of_words):
	res_list=[]
	new_word= list(word.lower())
	new_word.sort()
	for checking in list_of_words:
		new_checking= list(checking.lower())
		new_checking.sort()
		if  "".join(new_word)== "".join(new_checking):
			res_list.append(checking)
	return res_list


