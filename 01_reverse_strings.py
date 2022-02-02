# text = input()
# print(text[::-1])
#
# text = list(input())
# for index in range(len(text) - 1, -1, -1):
#     print(text[index], end="")
#
# print(text)  # not Stack, the list still remains

text = list(input())
print(text)
while text:
    print(text.pop(), end="")
print(text)
