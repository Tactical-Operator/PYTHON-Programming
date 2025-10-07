# create a text file to store individual characters


f=open('myfile.txt','w')

str=input('Enter text: ')

f.write(str)

f.close()