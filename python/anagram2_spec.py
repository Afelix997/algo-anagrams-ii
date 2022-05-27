# Can you translate this driver code to unit tests?

from anagram2 import anagrams_for 

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
print(anagrams_for("apple", list_of_words) == [])
