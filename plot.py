import matplotlib.pyplot as plt

# Turn on interactive mode
plt.ion()

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Plot of G-code Coordinates')
ax.grid(True)
x = 0
# Parse the G-code and extract X and Y coorcddinates
with open("graph14.gcode", "r") as file:
    for line in file:
        x += 1
        print("line " + str(x))
      
        if line.startswith("G0") or line.startswith("G1"):
            parts = line.split()
            x_coord = None
            y_coord = None
            for part in parts:
                if part.startswith("X"):
                    x_coord = float(part[1:])  # Extract X coordinate
                elif part.startswith("Y"):
                    y_coord = float(part[1:])  # Extract Y coordinate
            if x_coord is not None and y_coord is not None:
                # ax.plot(x_coord, y_coord, 'b')
                ax.scatter(x_coord, y_coord, color='b')
                # ax.scatter(x_coord, y_coord, color='b')  # Plot a dot for each coordinate
                plt.draw()
                # plt.pause(0.000000000000000000000000000000001)

# Keep the plot window open
plt.ioff()
plt.show()