class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], "."}

        if len(pattern) >= 2 and pattern[1] == "*":
            return (
                self.isMatch(text, pattern[2:])
                or first_match
                and self.isMatch(text[1:], pattern)
            )
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatch3(self, s, p):
        p = self.collapse_patterns(p)

        if not s and self.empty_pattern(p):
            return True

        if s and not p:
            return False

        if not s and p:
            return False

        if self.lookahead_loop(s, p):
            return True

        if self.pattern_match(s[0], p[0]):
            return self.isMatch(s[1:], p[1:])

        return False

    def lookahead_loop(self, s, p):
        if not self.asterisk_lookahead(p):
            return False

        # EMPTY MATCH
        if self.isMatch(s, p[2:]):
            return True

        # SUBSTRING MATCH
        for substring in self.string_slicer(s):
            if self.pattern_match(substring, p[0]):
                reduced_string = s[len(substring) :]
                if self.isMatch(reduced_string, p[2:]):
                    return True
            else:
                break  # EARLY STOPPING BECAUSE PATTERN CANNOT MATCH ANY MORE.

        return False

    def collapse_patterns(self, p):
        idx = 0

        while idx < len(p) - 3:
            if p[idx + 1] == "*" and p[idx + 3] == "*":
                if [idx] == "." or p[idx] == p[idx + 2]:
                    p = "".join(
                        [
                            char
                            for i, char in enumerate(p)
                            if i not in [idx + 2, idx + 3]
                        ]
                    )
                    idx = 0
                    continue
                elif [idx + 2] == ".":
                    p = "".join(
                        [char for i, char in enumerate(p) if i not in [idx, idx + 1]]
                    )
                    idx = 0
                    continue
            idx += 1
        return p

    def string_slicer(self, s):
        """
        Slices a string into substrings ( -> generator of substrings )
        """
        for i in range(1, len(s) + 1):
            yield s[:i]

    def pattern_match(self, s, p):
        """
        Checks if a string matches a character (a-z or "." for any character)
        """
        if p[0] == ".":
            return True

        if len(set(s)) != 1:
            return False

        return s[0] == p[0]

        # for char in s:
        #     if not p[0] == char:
        #         return False
        # return True

    def asterisk_lookahead(self, p):
        """
        Checks if the next character is "*"
        """
        try:
            return p[1] == "*"
        except IndexError:
            return False

    def empty_pattern(self, p):
        if not p:
            return True
        if len(p) >= 2 and p[1] == "*":
            return self.empty_pattern(p[2:])
        return False

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not s or not p:
            return False

        if p[0] in [s[0], "."]:
            s_reduced = s[1:]
            p_reduced = p[1:]

            if not s_reduced and self.empty_pattern(p_reduced):
                return True
            if not s_reduced or not p_reduced:
                return False

            if p_reduced[0] == "*":
                p_reduced = p_reduced[1:]
                if self.isMatchRecurringChar(s_reduced, p_reduced, p[0]):
                    return True

            if self.isMatch(s_reduced, p_reduced):
                return True

        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:])

        return False

    def isMatchRecurringChar(self, s, p, recurring_char):

        if recurring_char in [s[0], "."]:
            s_reduced = s[1:]
            p_reduced = p

            if not s_reduced and self.empty_pattern(p_reduced):
                return True
            if not s_reduced:
                return False

            if self.isMatchRecurringChar(s_reduced, p_reduced, recurring_char):
                return True
            else:
                print(s, p, s_reduced, p_reduced)

            return self.isMatch(s_reduced, recurring_char + p_reduced)
        else:
            return self.isMatch(s, p)


if __name__ == "__main__":
    solution = Solution()
    print(solution.collapse_patterns("a*a*a*a*a*a*a*a*a*a*c"))

    assert solution.isMatch("aa", "a") == False
    assert solution.isMatch("aa", "a*") == True
    assert solution.isMatch("aab", "a*b") == True
    assert solution.isMatch("ab", ".*") == True
    assert solution.isMatch("aab", "c*a*b") == True
    assert solution.isMatch("mississippi", "mis*is*p*.") == False
    assert solution.isMatch("mississippi", "mis*is*ip*.") == True
    assert solution.isMatch("mississippi", "mis*is*a*ip*.") == True
    assert solution.isMatch("aaa", ".*") == True
    assert solution.isMatch("aaa", "ab*a*c*a") == True
    assert solution.isMatch("a", "ab*") == True
    assert solution.isMatch("bbbba", ".*a*a") == True

    print("all good")
