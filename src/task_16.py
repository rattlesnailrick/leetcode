class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        max_idx = len(nums) - 1

        best_val = None
        best_diff = None

        for idx_a, value_a in enumerate(nums[:-2]):
            idx_b, idx_c = idx_a + 1, max_idx

            while idx_b < idx_c:
                summation = value_a + nums[idx_b] + nums[idx_c]

                diff = summation - target

                if diff < 0:
                    if not best_diff or abs(diff) < best_diff:
                        best_val = summation
                        best_diff = abs(diff)
                    idx_b += 1
                elif diff > 0:
                    if not best_diff or abs(diff) < best_diff:
                        best_val = summation
                        best_diff = abs(diff)
                    idx_c -= 1
                else:
                    return summation
        return best_val


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest([-1, 2, 1, -4, 17, 23, -2], 0))
    print(solution.threeSumClosest([0, 2, 1, -3], 1))
    print(solution.threeSumClosest([0, 0, 0], 1))
