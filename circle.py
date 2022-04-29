from math import pi

def circle_area(r):
    if r<0:
        raise ValueError('Radius value cannot be less than 0')

    elif type(r) not in [int, float]:
        raise TypeError('Radius value can only be an integer or float')

    return pi*(r**2)

print(circle_area(5))

'''
radii = [2, -2, True, 2+5j, 'Radius']

message = 'Area of the circle with r = {radius} is {area}'

for i in radii:
    A = circle_area(i)
    print(message.format(radius = i, area = A))'''