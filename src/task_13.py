class Solution:
    def romanToInt(self, s):
        encoding = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

        result = 0
        previous_value = max(encoding.values())  # SET START VALUE TO THE LARGEST VALUE IN OUR ENCODING

        for letter in s:
            value = encoding[letter]

            # IF THE PREVIOUS VALUE WAS SMALLER THEN THE CURRENT WE FIX THE SUMMATION BY DEDUCTING TWICE
            # e.g. IX -> [1,10] -> add 1, then add 10 and deduct the previous 1 twice -> 9
            if previous_value < value:
                result -= 2 * previous_value

            result += value
            previous_value = value

        return result


if __name__ == "__main__":
    from src.task_12 import Solution as intToRomanSolution

    solution_int_to_roman = intToRomanSolution()

    this_solution = Solution()
    for i in range(1, 3999):
        roman = solution_int_to_roman.intToRoman(i)
        arabic = this_solution.romanToInt(roman)
        assert arabic == i
