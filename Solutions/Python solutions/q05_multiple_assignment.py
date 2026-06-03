def display_coordinates(coords):
    if len(coords) != 2:
        print("Invalid coordinates")
        return
    x, y = coords
    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")
display_coordinates((10, 20))