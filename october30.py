# car = {
#   "brand": "Ford",
#   "year": 1964
# }

# print(car.setdefault("model", "ABC"))

# print(car)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def main(d, a=1,b=2,c=3):
#     print(a,b,c, d)

# main(j=213)

# def my_function(**kids):
#   print("The youngest child is " + kids["young"])
# my_function(young = "Emil", middle = "Tobias", elder = "Linus")

# def main2(x):
#     print(x)
#     main2(x+1)
# main2(3)

# try:
#     print(x)
# except NameError:
#     print(None)
# except IndentationError:
#     print(False)

# arr = [[11,123],[2,45342],[3,12],[4,432]]
# arr2 = sorted(arr, key = lambda x: sum(x), reverse=True)
# print(arr2)

# arr3 = [[3,10], [5,2], [66,4], [11,90]]
# print(max(arr3, key = lambda x: x[1]))

# arr = ["asd","asd"]
# d = {}
# for i in arr:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1 
# print(d)

d1 = {"name": "Sumaya", "phone": "550"}
d2 = {"name": "Nazima", "phone": "550"}

for j in d2:
    if j in d1:
        d1[j] += d2[j]

print(d1)