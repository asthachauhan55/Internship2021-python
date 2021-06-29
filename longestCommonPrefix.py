'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        shortest_elem = strs[0]

        for elem in strs:
            elem_len = len(elem)
            if elem_len == 0:
                return ""

            if elem_len <= len(shortest_elem):
                shortest_elem = elem

        prefix = ""

        for (i, c) in enumerate(shortest_elem):
            for elem in strs:
                if elem[i] != c:
                    return prefix

            prefix += c

        return prefix
