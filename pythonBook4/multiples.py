multiple = [val for val in range(0,31) if val%3 == 0]
multiple2 = [*range(0,31,3)]#* operator force the range to became reallity
print(multiple)
print(multiple2)