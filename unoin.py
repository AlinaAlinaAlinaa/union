file1={
    1,
    3,
    5,
    7,
    9,
    10,
    12,
    15,
    20
}

file2={
    2,
    3,
    6,
    7,
    10,
    14,
    15,
    18,
    20,
    25
 }
# weather_f ={day:temp * 9/5 + 32 for day,temp in weather_c.items()}

duplicates={numbers for numbers in file1  if numbers in file2}
print(duplicates)

