class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        
        anagrams = []
    
        for i, v in enumerate(strs):
            elem = self.extractElements(v)

            found = False
            for j, anagram in enumerate(anagrams):
                if elem == anagram:
                    answer[j].append(v)
                    found = True
                    break
            
            if not found:
                anagrams.append(elem)
                answer.append([v])


        return answer

    def extractElements(self, s: str) -> dict:
        elements = {}
    
        for c in s:
            elements[c] = elements.get(c, 0) + 1

        return elements
