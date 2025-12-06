class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, word_list):
        matches = []
        
        for candidate in word_list:
            candidate_lower = candidate.lower()
            
            # Skip if it's the same word
            if candidate_lower == self.word:
                continue
            
            # Check if they have the same sorted letters
            if sorted(candidate_lower) == sorted(self.word):
                matches.append(candidate)
        
        return matches