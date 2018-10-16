class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        result = []

        for idx_a in range(len(nums) - 2):

            if (nums[idx_a] > (nums[-2] + nums[-1])) or nums[idx_a] > 0:
                continue

            if idx_a > 0 and nums[idx_a] == nums[idx_a - 1]:
                continue

            idx_b, idx_c = idx_a + 1, len(nums) - 1

            while idx_c > idx_b:
                summation = nums[idx_a] + nums[idx_b] + nums[idx_c]
                if summation > 0:
                    idx_c -= 1
                elif summation < 0:
                    idx_b += 1
                else:
                    result.append([nums[idx_a], nums[idx_b], nums[idx_c]])

                    while idx_b < idx_c and nums[idx_b] == nums[idx_b + 1]:
                        idx_b += 1

                    while idx_c > idx_b and nums[idx_c] == nums[idx_c - 1]:
                        idx_c -= 1

                    idx_b += 1
                    idx_c -= 1

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([0, 0]))
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([0, 0, 0]))
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([3, -2, 1, 0]))
    print(solution.threeSum(
        [12, 5, -12, 4, -11, 11, 2, 7, 2, -5, -14, -3, -3, 3, 2, -10, 9, -15, 2, 14, -3, -15, -3, -14, -1, -7, 11, -4,
         -11, 12, -15, -14, 2, 10, -2, -1, 6, 7, 13, -15, -13, 6, -10, -9, -14, 7, -12, 3, -1, 5, 2, 11, 6, 14, 12, -10,
         14, 0, -7, 11, -10, -7, 4, -1, -12, -13, 13, 1, 9, 3, 1, 3, -5, 6, 9, -4, -2, 5, 14, 12, -5, -6, 1, 8, -15,
         -10, 5, -15, -2, 5, 3, 3, 13, -8, -13, 8, -5, 8, -6, 11, -12, 3, 0, -2, -6, -14, 2, 0, 6, 1, -11, 9, 2, -3, -6,
         3, 3, -15, -5, -14, 5, 13, -4, -4, -10, -10, 11]))

    print(solution.threeSum(
        [-3, 14, -10, -1, 12, 13, -3, 2, -6, 4, 13, 7, -8, 4, 0, -13, 11, -4, 7, 0, 4, -3, 12, 11, 5, -14, -8, 8, 3, -1,
         -8, -15, -2, -11, -9, -12, 9, 3, 5, -11, -8, 3, 3, -9, -15, -12, -15, 3, -9, 0, -12, 3, 12, -14, -1, -6, -13,
         -2, -13, -3, 12, -14, -3, -13, -9, 3, -10, -15, 13, 2, 11, 13, -9, -1, 11, 13, -6, 4, 1, 1, -11, 5, -11, 8, -2,
         -5, -12, -8, 8, -10, 4, -3, -8, -14, -1, -10, -4, -3, 12, -14, 14, 9, 6, 12, -15, 3, 10, -13, -8, -11, 3, -4,
         1, -1]))
