class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}

        #Unlike last time where we had to compare if two are anagrams, instead of just comparing if the word has a certain amount of letters instead we sort the word and then compare it with the rest of the words and if they are the same then we add them to the same list if not we create a new one so we can seperate them

        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str not in counter:
                counter[sorted_str] = [i]
            else: 

                counter[sorted_str].append(i)

        return list(counter.values())