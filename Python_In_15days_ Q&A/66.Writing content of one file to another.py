#Create a function that takes a list of sentences and writes them to a new text file
#each on a new line.
import ast
def copy_content(file1,file2):
    try:
         with open(file1,'r') as f1:
             content=f1.read()
             list_strings=ast.literal_eval(content)   #Parse the list
         with open(file2,'w') as f2:
             for line in list_strings:
                   f2.write(line+'\n')
    except FileNotFoundError:
           print('file1 not found')

copy_content('Python_FH','abc')