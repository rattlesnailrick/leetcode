class Solution:
    def longestCommonPrefix(self, strs):
        # Runtime: 36 ms, faster than 99.82% of Python3 online submissions for Longest Common Prefix.
        output = []

        for chars in zip(*strs):
            if len(set(chars)) == 1:
                output.append(chars[0])
            else:
                break
        return "".join(output)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["abc", "abd", "abe"]))
