import copy

original = [[1, 2, 3], [4, 5, 6]]
deep_copied = copy.deepcopy(original)

deep_copied[0][1] = 200

print("original", original)
print("Deep Copy", deep_copied)

print()

class Car:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors


# Create a Honda car object
honda_colors = ["Red", "Blue"]
honda = Car("Honda", honda_colors)


deep_copy = copy.deepcopy(honda)
deep_copy.colors.append('Black')
print(deep_copy.colors)
print(honda.colors)