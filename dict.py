filename = input('Enter a filename:').strip()
infile = open(filename,"r")
wordCounts = {}
for line in infile:
    processLine(line.lower(),wordCounts)
pairs = list(wordCounts.items())
items = [[x,y] for (y,x) in pairs]
items.sort()

count = 10
data = []
words = []
yScale = 6
xScale = 30

turtle.title('词频结果柱装图')
turtle.setup(900,750,0,0)
t = turtle.Turtle()
t.hideturtle()
t.width(3)
drawGraph(t)

def drawLine(t,x1,y1,x2,y2):
    t.penup()
    t.goto (x1,y1)
    t.pendown()
    t.goto (x2,y2)
def drawText(t,x,y,text):
    t.penup()
    t.goto (x,y)
    t.pendown()
    t.write(text)

def drawRectangle(t,x,y):
    x = x*xScale
    y = y*yScale
    drawLine(t,x-5,0,x-5,y)
    drawLine(t,x-5,y,x+5,y)
    drawLine(t,x+5,y,x+5,0)
    drawLine(t,x+5,0,x-5,0)
def drawBar(t):
    for i in range(count):
        drawRectangle(t,i+1,data[i])
def drawGraph(t):
    drawLine(t,0,0,360,0)
    drawLine(t,0,300,0,0)
    for x in range(count):
        x=x+1
        drawText(t,x*xScale-4,-20,(words[x-1]))
        drawText(t,x*xScale-4,-20,data[x-1]))
