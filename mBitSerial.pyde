add_library('serial')

def setup():
    global mbit
    size(470, 280)
    mbit = Serial(this, Serial.list()[0], 115200)
    global xOffset
    xOffset = width*1/2
    global yOffset
    yOffset = height*3/4
    global l
    l = 400
    
def draw():
    while ((mbit.available()) > 0):
        incoming = mbit.readString()
        degree = int(incoming)/11
        theta = radians(degree-90)
        if incoming != 0:
            background(0)
            stroke(255)
            line(xOffset, yOffset, xOffset + l*cos(theta), yOffset + l*sin(theta))
