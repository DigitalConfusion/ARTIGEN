import numpy as np

def modify_gcode(scale_factor):
    min_x = np.Infinity
    min_y = np.Infinity
    max_y = -np.Infinity
    translated_gcode = []

    with open("./ARTIGEN/graph2.gcode", "r") as file:
        gcode = file.readlines()

    # Find min_x
    for line in gcode:
        if line.startswith(('G0', 'G1')):
            components = line.split()
            for component in components:
                if component.startswith('X'):
                    x_value = float(component[1:])
                    if x_value < min_x:
                        min_x = x_value
                if component.startswith('Y'):
                    y_value = float(component[1:])
                    if y_value < min_y:
                        min_y = y_value
                    if y_value > max_y:
                        max_y = y_value

    # Translate and scale x and y coordinates
    for line in gcode:
        if line.startswith(('G0', 'G1')):
            components = line.split()
            for i, component in enumerate(components):
                if component.startswith('X'):
                    x_value = float(component[1:])
                    translated_x = round((x_value - min_x) * scale_factor, 2)
                    components[i] = 'X' + str(translated_x)
                elif component.startswith('Y'):
                    y_value = float(component[1:])
                    scaled_y = round((y_value) * scale_factor - min_y * scale_factor, 2)
                    components[i] = 'Y' + str(scaled_y)
            translated_gcode.append(' '.join(components))
        else:
            translated_gcode.append(line)

    # Write to a new file
    with open("./ARTIGEN/translated_graph2.gcode", "w") as file:
        for line in translated_gcode:
            # Write line to file with a newline character
            file.write(line + "\n")


def append_feed_rate():
    modified_gcode = []

    with open("./ARTIGEN/translated_graph2.gcode", "r") as file:
        gcode = file.readlines()

    # Append F1000 after G0 or G1
    for line in gcode:
        if line.startswith(('G0', 'G1')):
            components = line.split()
            components.insert(1, 'F2000')
            modified_gcode.append(' '.join(components))
        else:
            modified_gcode.append(line)

    # Write to a new file
    with open("./ARTIGEN/modified_graph2.gcode", "w") as file:
        for line in modified_gcode:
            # Write line to file with a newline character
            file.write(line + "\n")
            
def remove_small_movements():
    filtered_gcode = []
    last_x = None
    last_y = None

    with open("./ARTIGEN/modified_graph2.gcode", "r") as file:
        gcode = file.readlines()

    # Remove lines with small movements
    for line in gcode:
        if line.startswith(('G0', 'G1')):
            components = line.split()
            x_value = None
            y_value = None
            for component in components:
                if component.startswith('X'):
                    x_value = float(component[1:])
                elif component.startswith('Y'):
                    y_value = float(component[1:])
            
            if last_x is not None and last_y is not None:
                if abs(x_value - last_x) < 0.5 and abs(y_value - last_y) < 0.5:
                    continue
            
            last_x = x_value
            last_y = y_value

            filtered_gcode.append(line)
        else:
            filtered_gcode.append(line)

    # Write to a new file
    with open("./ARTIGEN/modified_graph2.gcode", "w") as file:
        for line in filtered_gcode:
            # Write line to file with a newline character
            file.write(line)



modify_gcode(0.35)  # Example usage: scale by a factor of 2
append_feed_rate()  # Run the function
remove_small_movements()  # Run the function