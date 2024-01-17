import os
file=open("product_descriptions.txt",mode='r')
#Reading the contents of the file
file_contents=(file.read())
print(file_contents)


#capitalizing first word of each sentence
capitalized_lines = []
for line in file_contents.splitlines():
    capitalized_words = ' '.join(word.capitalize() for word in line.split())
    capitalized_lines.append(capitalized_words)
    capitalized_content = '\n'.join(capitalized_lines)
    
print("The capitalized description is \n")
print(capitalized_content)

#saving capitalized content into the file
file2=open("formatted_descriptions.txt",mode='w')
file2.write(capitalized_content)