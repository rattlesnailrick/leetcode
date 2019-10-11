class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        results = []

        if len(digits) == 0:
            return []

        if len(digits) <= 1:
            return [char for char in mapping.get(digits, "")]

        for char in mapping[digits[0]]:
            for combination in self.letterCombinations(digits[1:]):
                results.append("".join([char, *combination]))
        return results


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("232"))
