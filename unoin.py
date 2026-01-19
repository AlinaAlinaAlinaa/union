with open("file1.txt") as f1:
    element1 = [int(numbers) for numbers in f1]

with open("file2.txt") as f2:
    element2 = [int(numbers) for numbers in f2]
    
duplicates={numbers for numbers in element1  if numbers in element2}
print(duplicates)

