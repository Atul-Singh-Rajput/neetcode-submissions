class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:

    
            sorted_word = sorted(word)

        
            key = "".join(sorted_word)

            if key not in d:
                d[key] = []

            d[key].append(word)

        return list(d.values())
