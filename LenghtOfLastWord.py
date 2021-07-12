class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        for letter in s[::-1]:
            if letter == " ":
                if count >= 1:
                    return count
            else:
                count+=1
        return count
