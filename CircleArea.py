PI = 3.14


def circlearea():
    introca()
    radius_needed = float(input("Enter the radius:"))
    radius_to_area(radius_needed)


def introca():
    print("This is to get the area of a circle, all you need is the radius")


def radius_to_area(radius):
    area = PI * (radius**2)
    print(f'That makes the area {area}')


circlearea()
