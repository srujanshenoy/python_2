pi = 3.141592659


def area_square(a: float):
    return a**2


def peremeter_square(a: float):
    return a*4


def area_rectangle(l: float, b: float):
    return l*b


def peremeter_rectangle(l: float, b: float):
    return 2*(l+b)


def area_triangle(breadth: float, hight: float):
    breadth/2*hight


def peremeter_triangle(side_a: float, side_b: float, side_c: float):
    return side_a + side_b + side_c


def missing_angle(angle_a: float, angle_b: float):
    if angle_a + angle_b < 180:
        return 180-(angle_a + angle_b)
    else:
        return """innapropriate values:
                1. either you typed any other characters other than numbers.
                2. you typed two values that sum to more than 180, thus making it impossible to have a triangle.
              """


def peremeter_circle(value: float):
    r_or_d = int(input(
        "what have you typed? radius or the diameter? \n if it is the radius, type 1. if it is the denominator, type 2. \n"))
    # if r_or_d is 1, it has to be the radius: (2 * pi * r)
    if r_or_d == 1:
        return 2*pi*r_or_d
    # if r_or_d is 2, it has to be the diameter, in which case 2 pi r would be the
    # same as pi 2 r or pi d. so, we can directly say pi*r_or_d.
    if r_or_d == 2:
        return pi*r_or_d


def area_circle(value: float):
    r_or_d = int(input(
        "what have you typed? radius or the diameter? \n if it is the radius, type 1. if it is the denominator, type 2. \n"))
    # if r_or_d is 1, it has to be the radius: pi * r**2
    if r_or_d == 1:
        return pi * (r_or_d ** 2)
    # if r_or_d is 2, then it has to be the diameter: pi r**2.
    # but since it is the diameteter, we have to divide by two and substitute that for r in the formula
    # ending up with pi * ((r_or_d / 2) ** 2)
    if r_or_d == 2:
        return pi * ((r_or_d/2) ** 2)


def help_msg_1():

    x = input("""
    AREA AND PEREMETER AND ANGLES

    FOR AREA, TYPE 1
    FOR PEREMETER, TYPE 2
    FOR HELP, TYPE 3
    FOR MISSING ANGLE OF TRIANGLE, TYPE 4
    FOR EXIT, TYPE 5
    """)

    try:
        x = int(x)
    except:
        print("you did not type a valid number. Please type 3 to display this help & select again.")

    return x


def help_msg_area():
    #circle, triangle, rectangle, square
    shape_of_area = input("""
    1. circle
    2. triangle
    3. rectangle
    4.square
    5. exit

    Please type the reference index number for whichever shape you need
    """)

    # 1 - CIRCLE
    # 2 - TRIANGLE
    # 3 - RECTANGLE
    # 4 - SQUARE
    # 5 - EXIT

    return shape_of_area


def help_msg_peremeter():
    #circle, triangle, rectangle, square
    shape_of_area = input("""
    1. circle
    2. triangle
    3. rectangle
    4.square
    5. exit

    Please type the reference index number for whichever shape you need
    """)

    # 1 - CIRCLE
    # 2 - TRIANGLE
    # 3 - RECTANGLE
    # 4 - SQUARE
    # 5 - EXIT

    return shape_of_area


def prog():
    pass


prog()
