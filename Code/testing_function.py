def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + '' + last
    return full_name.title()

# Find Max in a list
arr = [1, 3, 5, 7, 9, -1, 100]
def max(arr):
    maxn=arr[0]
    for item in arr:
        if item > maxn:
            maxn = item
    return maxn
print(max(arr))

def min(arr):
    minn = arr[0]
    for item in arr:
        if item < minn:
            minn = item
    return minn

class Dish():
    def __init__(self, name, calories, vegan):
        self.name = name
        self.calories = calories
        self.vegan = vegan

dish_1 = Dish('A', 12, False)
dish_2 = Dish('B', 13, False)
dish_3 = Dish('C', 14, True)

Meny =[]
Meny.append(dish_2)
Meny.append(dish_1)
Meny.append(dish_3)

ListOfCal = []

for item in Meny:
    ListOfCal.append(item.calories)

print(ListOfCal)
print(min(ListOfCal))
mincal = min(ListOfCal)

index1 = ListOfCal.index(mincal)
print(index1)
print(Meny[index1].name)
print(max(ListOfCal))
print("The dish with lowest calory is dish " + Meny[index1].name)

