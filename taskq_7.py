def distance_squared(point, reference):
    x1, y1 = point
    x2, y2 = reference

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def sort_by_distance(points, reference):

    n = len(points)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if distance_squared(points[j], reference) < distance_squared(points[min_index], reference):
                min_index = j

        points[i], points[min_index] = points[min_index], points[i]

    return points


# Take number of points
n = int(input("Enter number of points: "))

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