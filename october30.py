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

try:
    print(x)
except NameError:
    print(None)
except IndentationError:
    print(False)