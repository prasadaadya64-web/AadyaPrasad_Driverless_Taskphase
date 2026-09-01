import csv
import os


# Function to calculate distance squared
def distance_squared(x1, y1, x2, y2):

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


# Find the folder where this Python file is located
folder = os.path.dirname(__file__)


# --------------------------------
# STEP 1: Read cones.csv
# --------------------------------

file_path = os.path.join(folder, "cones.csv")

cones = []

with open(file_path, "r", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cone = {
            "id": row["id"],
            "x": float(row["x"]),
            "y": float(row["y"]),
            "colour": row["colour"].lower()
        }

        cones.append(cone)


# --------------------------------
# STEP 2: Calculate distance
# from origin
# --------------------------------

for cone in cones:

    cone["distance"] = distance_squared(
        cone["x"],
        cone["y"],
        0,
        0
    )


# --------------------------------
# STEP 3: Sort cones
# --------------------------------

cones.sort(key=lambda cone: cone["distance"])


# --------------------------------
# STEP 4: Separate colours
# --------------------------------

blue_cones = []
yellow_cones = []

for cone in cones:

    if cone["colour"] == "blue":

        blue_cones.append(cone)

    elif cone["colour"] == "yellow":

        yellow_cones.append(cone)


# --------------------------------
# STEP 5: Create blue.csv
# --------------------------------

blue_file = os.path.join(folder, "blue.csv")

with open(blue_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "x", "y", "colour"])

    for cone in blue_cones:

        writer.writerow([
            cone["id"],
            cone["x"],
            cone["y"],
            cone["colour"]
        ])


# --------------------------------
# STEP 6: Create yellow.csv
# --------------------------------

yellow_file = os.path.join(folder, "yellow.csv")

with open(yellow_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "x", "y", "colour"])

    for cone in yellow_cones:

        writer.writerow([
            cone["id"],
            cone["x"],
            cone["y"],
            cone["colour"]
        ])


# --------------------------------
# STEP 7: Find nearest yellow
# for every blue cone
# --------------------------------

centreline_file = os.path.join(folder, "centreline.csv")

with open(centreline_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["x", "y"])

    for blue in blue_cones:

        nearest_yellow = None

        smallest_distance = float("inf")

        for yellow in yellow_cones:

            distance = distance_squared(
                blue["x"],
                blue["y"],
                yellow["x"],
                yellow["y"]
            )

            if distance < smallest_distance:

                smallest_distance = distance

                nearest_yellow = yellow


        # --------------------------------
        # STEP 8: Find midpoint
        # --------------------------------

        if nearest_yellow is not None:

            midpoint_x = (
                blue["x"] + nearest_yellow["x"]
            ) / 2

            midpoint_y = (
                blue["y"] + nearest_yellow["y"]
            ) / 2

            writer.writerow([
                midpoint_x,
                midpoint_y
            ])


print("Done!")
print("blue.csv created")
print("yellow.csv created")
print("centreline.csv created")