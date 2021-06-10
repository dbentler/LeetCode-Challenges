"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

def reverseWords(s: str) -> str:
    tmp = s.split()
    reversed_in_place = []
    for words in tmp:
        reversed_in_place.append(words[::-1])
    return " ".join(reversed_in_place)

if __name__ == "__main__":
    sentence = "Let's take LeetCode contest"
    reversed_sentence = reverseWords(sentence)
    print(reversed_sentence)