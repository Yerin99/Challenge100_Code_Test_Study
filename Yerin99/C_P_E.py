hangul_str = []
hangul_substring = []
similarity_list = []

n = int(input())

for _ in range(n):
    line = input()
    new_line = ''
    for char in line:
        if ord('가') <= ord(char) <= ord('힣'):
            new_line += char
    hangul_str.append(new_line)

for entry in hangul_str:
    substring_set = set()
    for i in range(len(entry)-1):
        substring_set.add(entry[i:i+1])
    hangul_substring.append(substring_set)

for i in range(n):
    for j in range(i+1, n):
        numerator = len(hangul_substring[i] & hangul_substring[j])
        denominator = len(hangul_substring[i] | hangul_substring[j])
        similarity = numerator / denominator
        similarity_list.append([i+1, j+1, similarity])

similarity_list.sort(reverse=True, key=lambda x: x[-1])

print(similarity_list[0][0], similarity_list[0][1])
