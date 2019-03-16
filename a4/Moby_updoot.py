string_1 = "Julian"
string_2 = "Moke"
string_3 = "Wow {} is really cool!"
string_4 = "{} != {}"

print(string_1)
print(string_2 + string_1)
print(string_3.format(string_1))
print(string_4.format(3, 4))
print(string_4.format(string_1, string_2))

print(string_4.format(string_3.format(string_2), string_2))
