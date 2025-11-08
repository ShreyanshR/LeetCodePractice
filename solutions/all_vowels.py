from typing import List

class Solution:
    def __init__(self, list_of_words: List[str]):
        self.list_of_words = list_of_words

    def words_with_all_vowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = []
        

        for word in self.list_of_words:
            vow = []
            print(word)
            for char in word:
                if char.lower() in vowels:
                    print(char)
                    vow.append(char)

            if set(vow) == set(vowels) : 
                res.append(True) 
            else: 
                res.append(False)

        print(res)
        return res


if __name__ == "__main__":
   words = ['car', 'multidirectional', 'hello', 'overqualified', 'university']

   sol = Solution(['car', 'multidirectional', 'hello', 'overqualified', 'university'])

   sol.words_with_all_vowels()