class Solution:
    def intToRoman(self, num):
        ones = ["I", "X", "C", "M"]
        fives = ["V", "L", "D", None]

        idx = 0

        output = []

        while num > 0:

            last_digit = num % 10
            if last_digit == 0:
                pass
            elif last_digit < 4:
                output = [ones[idx] * last_digit] + output
            elif last_digit == 4:
                output = [ones[idx], fives[idx]] + output
            elif last_digit == 9:
                output = [ones[idx], ones[idx + 1]] + output
            elif last_digit >= 5:
                output = [fives[idx], ones[idx] * (last_digit - 5)] + output

            num = int((num - last_digit) / 10)
            idx += 1

        return "".join(output)


if __name__ == "__main":
    solution = Solution()
    for i in range(100):
        print(i, solution.intToRoman(i))
