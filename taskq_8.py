import csv
import os

# Function to calculate distance squared

def distance_squared(x1, y1, x2, y2):

    return (x1 - x2) ** 2 + (y1 - y2) ** 2

# Find the folder where this Python file is located

folder = os.path.dirname(__file__)

# Read cones.csv

file_path = os.path.join(folder, "cones.csv")

cones = [] #empty list#

with open(file_path, "r", newline="") as file:

    reader = csv.DictReader(file)

    #starting a loop to iterate through every individula row in the csv file.#

    for row in reader:

        #creating of new dictionary named cone for the row#

        cone = {
            "id": row["id"], #for extracting the cone's text id#
            "x": float(row["x"]),
            "y": float(row["y"]),
            "colour": row["colour"].lower()
        }

        cones.append(cone)

# Calculate distance from origin
# calling the helper function to calculate the distance of the co ordinates of the cone to the origin

for cone in cones:

    cone["distance"] = distance_squared(
        cone["x"],
        cone["y"],
        0,
        0
    )

    def get_distance(cone):           #defining a function for single object(cone).#
        return cone["distance"]

#Sorting cones

cones.sort(key=get_distance) #sorts the cones list using get distance function as the key#

#Separate colours

blue_cones = []
yellow_cones = []

for cone in cones:

    if cone["colour"] == "blue":

        blue_cones.append(cone)

    elif cone["colour"] == "yellow":

        yellow_cones.append(cone)

#Create blue.csv

blue_file = os.path.join(folder, "blue.csv")

with open(blue_file, "w", newline="") as file:

    writer = csv.writer(file)  #creating csv writer object for file#

    writer.writerow(["id", "x", "y", "colour"]) #writing each cones data row by row , w is for writer mode#

    for cone in blue_cones:

        writer.writerow([
            cone["id"],
            cone["x"],
            cone["y"],
            cone["colour"]
        ])

#Create yellow.csv

yellow_file = os.path.join(folder, "yellow.csv")

with open(yellow_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["id", "x", "y", "colour"])

    for cone in yellow_cones: # creating loop for each cone in yellow category list#

        writer.writerow([
            cone["id"],
            cone["x"],
            cone["y"],
            cone["colour"]
        ])

# Find nearest yellow
# for every blue cone

centreline_file = os.path.join(folder, "centreline.csv")

with open(centreline_file, "w", newline="") as file: # we r using writer mode as it needs to completely create a new file n save the sorted data.#

    writer = csv.writer(file)

    writer.writerow(["x", "y"])

    for blue in blue_cones:

        nearest_yellow = None # finding closest yellow cone to blue cone , none acts as a baseline at the start of each search#

        smallest_distance = float("inf") # sets the initial minimum distance to infinity#

        for yellow in yellow_cones:

            distance = distance_squared(
                blue["x"],
                blue["y"],
                yellow["x"],
                yellow["y"]
            )

            if distance < smallest_distance: #checking if the calculated distance is less than the current distance

                smallest_distance = distance

                nearest_yellow = yellow


       
        #Find midpoint
        

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