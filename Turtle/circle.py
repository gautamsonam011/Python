from turtle import*
import colorsys

bgcolor('black')
tracer(2)
# persize(2)

h = 0

for i in range(329):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    # persize(3)
    circle(1.100)
    rt(91)
    fillcolor('blue')
    begin_fill()
    circle(i/2.90)
    end_fill()
    rt(91)
    circle(60.90)
done()