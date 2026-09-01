def distance_squared(point, reference):

#it assings first value to x1 n then second value to y1#

    x1, y1 = point
    x2, y2 = reference

# Calculates and returns the squared Euclidean distance square root is not needed as we r comparing distances#

    return (x1 - x2) ** 2 + (y1 - y2) ** 2

#Accepts a list of coordinate tuples (points) and a single coordinate tuple (reference)#

def sort_by_distance(points, reference):

    n = len(points)

#It tracks the boundary of the sorted portion of the list, moving from index 0 to n-1

    for i in range(n):

        #assumes the current position is closest#

        min_index = i

        for j in range(i + 1, n):

            if distance_squared(points[j], reference) < distance_squared(points[min_index], reference):
                min_index = j

        points[i], points[min_index] = points[min_index], points[i]

    return points


# Take number of points
n = int(input("Enter number of points: "))

#created an empty list to store users input#

points = []

# Take coordinates of each point

for i in range(n):

    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    points.append((x, y))


# Take reference point

rx = int(input("Enter reference x: "))
ry = int(input("Enter reference y: "))

reference = (rx, ry)


# Sort points

result = sort_by_distance(points, reference)


# Print result

print("Sorted points:")
print(result)