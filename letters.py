#Group Words Containing Same Letters Together
#Write a Python program to group words that contain the same letters.
#input_ an array/list as words
#output_list of groups, where each group contains words with sam latters
from collections import defaultdict

def group_words(words):
    groups = defaultdict(list)

    for w in words:
        key = ''.join(sorted(w))  # same letters create same key
        groups[key].append(w)

    return list(groups.values())


# Example
words = ["eat", "tea", "tan", "ate", "nat"]
print(group_words(words))
