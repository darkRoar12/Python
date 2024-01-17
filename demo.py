import os
file=open("product_descriptions.txt",mode='r')
#Reading the contents of the file
file_contents=(file.read())
# print(file_contents)


#capitalizing first word of each sentence
capitalized_lines = []
for line in file_contents.splitlines():
    for word in line.split():
        capitalized_words=' '.join(word.capitalize())
        capitalized_lines.append(capitalized_words)
capitalized_content = '\n'.join(capitalized_lines)
    
print("The capitalized description is \n")
print(capitalized_content)