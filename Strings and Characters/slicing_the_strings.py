#general rule :- str[start:stop:stepsize] 

word="Ashwin"
# only start
substring=word[2:]
print(substring)
# only stop
substring=word[:6]
print(substring)
# only stepsize (note that if the start is from default then the first character is also considered)
substring=word[0::2]
print(substring)
