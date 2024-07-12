class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1:r]
        longest = ""

        for i in range(len(s)):
            palindromeOdd = findPalindrome(i, i)
            palindromeEven = findPalindrome(i, i + 1)

            longest = palindromeOdd if len(palindromeOdd) > len(longest) else longest
            longest = palindromeEven if len(palindromeEven) > len(longest) else longest

        return longest
