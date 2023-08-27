#Implement a program that reads a text file and counts the number of words and lines in it.
try:
    with open('Python_FH','r') as file1:
        lines_count=0
        words_count=0
        content=file1.read()
        lines=content.split('\n')
        words=content.split()
        for line in lines:
                 lines_count+=1
        print('Total lines are:',lines_count)
        for word in words:
             words_count+=1
        print('Total words are:',words_count)
except FileNotFoundError:
        print('file not found')