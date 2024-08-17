from graphics import *
import math
import time

def draw_rectangles(win):
    rect = Rectangle(Point(50, 60), Point(80, 90))
    rect.setFill("green")
    rect.setOutline("black")
    rect.draw(win)
    c = rect.getCenter()

    for i in range(10):
        p = win.getMouse()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newrect = Rectangle(Point(50 + dx, 60 + dy), Point(80 + dx, 90 + dy))
        newrect.setFill("green")
        newrect.setOutline("black")
        newrect.draw(win)

    text = Text(Point(100, 20), "Click again to proceed.")
    text.draw(win)
    win.getMouse()
    text.undraw()

def draw_triangle(win):
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    pt3 = win.getMouse()

    Polygon(pt1, pt2, pt3).draw(win)

    dx1 = abs(pt1.getX() - pt2.getX())
    dy1 = abs(pt1.getY() - pt2.getY())
    a = math.sqrt((dx1 ** 2) + (dy1 ** 2))

    dx2 = abs(pt2.getX() - pt3.getX())
    dy2 = abs(pt2.getY() - pt3.getY())
    b = math.sqrt((dx2 ** 2) + (dy2 ** 2))

    dx3 = abs(pt1.getX() - pt3.getX())
    dy3 = abs(pt1.getY() - pt3.getY())
    c = math.sqrt((dx3 ** 2) + (dy3 ** 2))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    Text(Point(350, 600), f'Area: {area:.2f} sq. units').draw(win)
    time.sleep(2)

def draw_house(win):
    pt1 = win.getMouse()
    pt2 = win.getMouse()
    Rectangle(pt1, pt2).draw(win)

    pt3 = win.getMouse()
    width = abs(pt1.getX() - pt2.getX())
    door_width = width / 5

    door_x1 = pt3.getX() - door_width / 2
    door_y1 = pt3.getY()
    door_x2 = pt3.getX() + door_width / 2
    door_y2 = pt1.getY()
    Rectangle(Point(door_x1, door_y1), Point(door_x2, door_y2)).draw(win)

    pt4 = win.getMouse()
    window_width = door_width / 2
    window_x1 = pt4.getX() - window_width / 2
    window_y1 = pt4.getY() - window_width / 2
    window_x2 = pt4.getX() + window_width / 2
    window_y2 = pt4.getY() + window_width / 2
    Rectangle(Point(window_x1, window_y1), Point(window_x2, window_y2)).draw(win)

    pt5 = win.getMouse()
    pt_temp = Point(pt1.getX(), pt2.getY())
    Polygon(pt5, pt2, pt_temp).draw(win)
    time.sleep(2)

def draw_archery(win):
    circle4 = Circle(Point(300, 300), 120)
    circle4.setFill("white")
    circle4.draw(win)
    update(30)
    time.sleep(2)

    circle3 = Circle(Point(300, 300), 90)
    circle3.setFill("blue")
    circle3.draw(win)
    update(30)
    time.sleep(2)

    circle2 = Circle(Point(300, 300), 60)
    circle2.setFill("red")
    circle2.draw(win)
    update(30)
    time.sleep(2)

    circle1 = Circle(Point(300, 300), 30)
    circle1.setFill("yellow")
    circle1.draw(win)
    update(30)
    time.sleep(0.1)

def draw_face(win):
    oval = Oval(Point(125, 50), Point(375, 450))
    oval.draw(win)

    left_eye = Circle(Point(190, 180), 10)
    left_eye.draw(win)

    right_eye = Circle(Point(300, 180), 10)
    right_eye.draw(win)

    nose = Rectangle(Point(248, 240), Point(255, 247))
    nose.draw(win)

    mouth = Rectangle(Point(185, 320), Point(330, 300))
    mouth.draw(win)
    time.sleep(2)

def draw_winter_scene(win):
    head = Circle(Point(650, 150), 50)
    head.draw(win)

    leye = Circle(Point(625, 125), 5)
    leye.draw(win)

    reye = Circle(Point(670, 125), 5)
    reye.draw(win)

    nose = Polygon(Point(650, 145), Point(645, 150), Point(655, 160))
    nose.draw(win)

    mouth = Rectangle(Point(625, 175), Point(675, 180))
    mouth.draw(win)

    s_circle = Circle(Point(650, 260), 60)
    s_circle.draw(win)

    l_circle = Circle(Point(650, 420), 100)
    l_circle.draw(win)

    l_hand = Line(Point(590, 260), Point(500, 200))
    l_hand.draw(win)

    r_hand = Line(Point(710, 260), Point(800, 200))
    r_hand.draw(win)

    f_triangle = Polygon(Point(180, 400), Point(70, 500), Point(300, 500))
    f_triangle.draw(win)

    s_triangle = Polygon(Point(180, 300), Point(100, 400), Point(270, 400))
    s_triangle.draw(win)

    t_triangle = Polygon(Point(180, 200), Point(120, 300), Point(250, 300))
    t_triangle.draw(win)

    f_triangle = Polygon(Point(180, 100), Point(125, 200), Point(230, 200))
    f_triangle.draw(win)

    base = Rectangle(Point(170, 500), Point(200, 510))
    base.draw(win)

    snow_circles = []
    points = [(100, 108), (120, 229), (110, 326), (130, 409), (300, 101), (320, 222), (300, 330),
              (325, 430), (510, 100), (530, 200), (525, 300), (522, 400), (723, 110), (734, 230),
              (740, 340), (750, 450)]
    for point in points:
        c = Circle(Point(point[0], point[1]), 5)
        c.draw(win)
        snow_circles.append(c)

    for _ in range(58):
        for c in snow_circles:
            c.move(10, 10)
            update(60)
    time.sleep(2)

def draw_dices(win):
    dice_points = [(33, 233), (266, 466), (499, 699), (732, 932), (965, 1165)]
    for pt1, pt2 in dice_points:
        Rectangle(Point(pt1, 200), Point(pt2, 400)).draw(win)

    dice5_points = [(1009, 231), (1121, 231), (1009, 300), (1121, 300), (1009, 369), (1121, 369)]
    for pt in dice5_points:
        Circle(Point(pt[0], pt[1]), 12.5).draw(win)

    dice4_points = [(775.5, 231), (888.5, 231), (832, 300), (775.5, 369), (888.5, 369)]
    for pt in dice4_points:
        Circle(Point(pt[0], pt[1]), 12.5).draw(win)

    dice3_points = [(542.5, 231), (655.5, 231), (542.5, 369), (655.5, 369)]
    for pt in dice3_points:
        Circle(Point(pt[0], pt[1]), 12.5).draw(win)

    dice2_points = [(423, 231), (366, 300), (309.5, 369)]
    for pt in dice2_points:
        Circle(Point(pt[0], pt[1]), 12.5).draw(win)

    dice1_points = [(76.5, 231), (189.5, 369)]
    for pt in dice1_points:
        Circle(Point(pt[0], pt[1]), 12.5).draw(win)
    time.sleep(2)

def draw_future_value(win):
    win.setBackground("white")

    prin = Text(Point(65, 50), 'Principal amount: ')
    int_text = Text(Point(55, 75), 'Interest rate:')
    prin.draw(win)
    int_text.draw(win)
    princ = Entry(Point(200, 50), 10)
    princ.setText("0.0")
    princ.draw(win)

    annual_rate = Entry(Point(200, 75), 10)
    annual_rate.setText("0.0")
    annual_rate.draw(win)

    year_text = Text(Point(110, 100), 'No of years: ')
    years = Entry(Point(200, 100), 5)
    years.setText("0")
    year_text.draw(win)
    years.draw(win)

    output = Text(Point(115, 150), 'Future Value: ')
    output.draw(win)
    result = Text(Point(200, 150), "")
    result.draw(win)

    calc_button = Rectangle(Point(150, 200), Point(250, 225))
    calc_button.draw(win)
    button_label = Text(Point(200, 212.5), "Calculate")
    button_label.draw(win)

    win.getMouse()

    principal = float(princ.getText())
    annual_rate_value = float(annual_rate.getText())
    time_years = float(years.getText())
    future_value = principal * (1 + annual_rate_value / 100) ** time_years
    result.setText(f'${future_value:.2f}')

    win.getMouse()

def main():
    win = GraphWin("Graphics Program", 1200, 800)
    draw_rectangles(win)
    draw_triangle(win)
    draw_house(win)
    draw_archery(win)
    draw_face(win)
    draw_winter_scene(win)
    draw_dices(win)
    draw_future_value(win)
    win.close()

if __name__ == "__main__":
    main()
