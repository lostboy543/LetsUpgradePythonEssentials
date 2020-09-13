input="fahar is a good boy"
str=input.split(" ")

lst_new = list(map(lambda s: s.capitalize(),str))
print(lst_new)