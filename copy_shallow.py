import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)

shallow_copied[0][0] = 100

print("original", original)
print("Shallow Copy", shallow_copied)

print()


class Car:
    def __init__(self, name, colors):
        self.name = name
        self.colors = colors


# Create a Honda car object
honda_colors = ["Red", "Blue"]
honda = Car("Honda", honda_colors)

shallow_copy = copy.copy(honda)
shallow_copy.colors.append('White')
print(shallow_copy.colors)
print(honda.colors)