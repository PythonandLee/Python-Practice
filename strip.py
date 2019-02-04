# .rstrip() is a command to remove spaces in the end
# .lstrip() is a command to remove spaces at the beginning
# .strip() is a command to remove spaces from both beginning and end

favorite_language = '   Python       '
a = favorite_language.rstrip()
b = favorite_language.lstrip()
c = favorite_language.strip()

print(a)
print(b)
print(c)