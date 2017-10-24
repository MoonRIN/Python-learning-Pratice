from math import sin, cos, radians
class projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0, 0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvell = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (yvell + self.yvel) / 2.0

    def getY(self):
        return self.ypos

    def method_name(self):
        ret0urn self.xpos

    def getX(self):

from projectil import *
def getInputs():
    a = eval(input("Enter lunch angle (in gegrees):"))
    v = eval(input("Enter initial velocity (in meters/sec):"))
    h = eval(input("Enter initial height (in meters):"))
    t = eval(input("Enter the time interval:"))
    return a, v, h, t
def main():
    angle, vel, h0, time = getInputs()
    shot = projectile(angle, vel, h0)
    while shot.getY()>=0:
        shot.update(time)
    print("\nDistance traveled:{0:0.1f}meters.".format(shot.getX()))

if __name__ == "__main__":
    main()
