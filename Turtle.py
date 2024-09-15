import math
import random
from turtle import *
from time import sleep


generation_string = "Quinn is slow his pc is very bad"


red = 0
green = 0
blue = 0
t_speed = 0
t_distance = 0
t_angle = 0
for char in generation_string:
	if char in "ABDFGJPRSUdgnoqsxyz57":
		red += len(generation_string)
	elif char in "IKLQWYZabcehijlrtuvw6":
		green += len(generation_string)
	elif char in "CEHMNOTVXfkmp1234089":
		blue += len(generation_string)
	if char in "ABDFGJPRSUdgnoqsxyz57":
		t_speed += len(generation_string)
	elif char in "IKLQWYZabcehijlrtuvw6":
		t_distance += len(generation_string)
	elif char in "CEHMNOTVXfkmp1234089":
		t_angle += len(generation_string) * math.pi
red %= 255
green %= 255
blue %= 255
t_speed = int(t_speed % 25 + 6)
t_distance %= 400
t_angle %= 360

red += 30
if red > 255: red -= 30
green += 30
if green > 255: green -= 30
blue += 30
if blue > 255: blue -= 30
t_distance += 30
t_angle += 15

colormode(255)
ht()
bgcolor((0, 0, 0))

color((red, green, blue))
speed(t_speed)

while True:
	forward(t_distance) #400
	left(t_angle) #121.1113