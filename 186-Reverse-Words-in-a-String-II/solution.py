class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        reverse(s, 0, len(s) - 1)
        i = 0
        j = 0
        while i < len(s) - 1:
            while j < len(s) - 1 and s[j] != ' ':
                j += 1
            if j == len(s) - 1:
                reverse(s, i, j)
            else:
                reverse(s, i, j - 1)
            j += 1
            i = j