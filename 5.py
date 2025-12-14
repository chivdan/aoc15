import re

three_vowels = "(.*[aeiou].*){3,}"
two_letters = ".*([a-z])\\1+.*"
bad_pairs = ["ab", "cd", "pq", "xy"] 

two_pairs = ".*([a-z]{2}).*\\1.*"
two_letters_with_one_in_between = ".*([a-z]).\\1.*"

def solve(part1: bool):
    result = 0
    for line in open("input.txt"):
        if part1:
            if any(p in line for p in bad_pairs):
                continue
            if all(re.match(pattern, line) for pattern in [three_vowels, two_letters]):
                result += 1
        else:
            if all(re.match(pattern, line) for pattern in [two_pairs, two_letters_with_one_in_between]):
                result += 1

    print(result)



if __name__ == '__main__':
    solve(True)
    solve(False)
