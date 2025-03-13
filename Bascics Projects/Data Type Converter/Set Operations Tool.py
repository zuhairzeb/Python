###  Set Operations Tool (DataTypes)

def set_operations():
    set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
    set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference: {set1 - set2}")

set_operations()