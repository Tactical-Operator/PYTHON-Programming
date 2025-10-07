file =open('myfile.txt','r+')

print_contents=file.read()

print(print_contents)

input_string=input('Enter new text: ')

file.write(input_string)

file=open('myfile.txt','r')

new_contents=file.read()

print(new_contents)

file.close()
