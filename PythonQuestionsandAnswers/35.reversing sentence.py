#Create a function that takes a sentence as input and returns the sentence in reverese order.
Sentence='Bengaluru is a beautyful city'
list1=list(map(str, Sentence.split()))
list_reversal=list1[::-1]
result=' '.join(list_reversal)
print(result)