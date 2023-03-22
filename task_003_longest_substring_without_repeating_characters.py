def length_of_longest_substring(s: str) -> int:
    hash = set()
    result = 0
    left = 0
    for i in range(len(s)):
        while s[i] in hash:
            hash.remove(s[left])
            left += 1

        hash.add(s[i])
        result = max(result, i - left + 1)
    return result


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
