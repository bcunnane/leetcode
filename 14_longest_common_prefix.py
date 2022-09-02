"""
Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix(strs):
    # deal with empty list or empty strings
    if len(strs) == 0 or strs.count("") >= 1:
        return ""

    # get shortest string length
    strs_lens = [len(s) for s in strs]
    min_len = min(strs_lens)

    # count longest shared prefix
    num = len(strs)
    max_match = 0
    for i in range(min_len):
        char = [s[i] for s in strs]
        if char.count(strs[0][i]) == num:
            max_match += 1
        else:
            break
    result = strs[0][:max_match]
    return result


def test():
    test_strs = [["flower", "flow", "flight"],
                 ["dog", "racecar", "car"],
                 ["ride", "riding", "rider"],
                 ["", "riding", "rider"],
                 ["r", "riding", "rider"]]
    for ts in test_strs:
        result = longestCommonPrefix(ts)
        print(f'{str(ts).ljust(30)}     longest prefix: {result}')


test()
