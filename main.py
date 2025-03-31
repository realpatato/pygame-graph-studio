import math
import pygame

pygame.init()

# Center and radius of pie chart
cx, cy, r = 125, 125, 75

val=float(input("input percentage "))
total=float(input("input total "))
# Calculate the angle in degrees
angle = (val*360/total)

# Start list of polygon points
p = [(cx, cy)]

# Get points on arc
for n in range(0, int(360-angle)):
    x = cx + int(r*math.cos(n*math.pi/180))
    y = cy+int(r*math.sin(n*math.pi/180))
    p.append((x, y))
p.append((cx, cy))

val=int(input("input num "))
total=int(input("input total "))
# Calculate the angle in degrees
angle2 = (val*360/total)

# Start list of polygon points
p2 = [(cx, cy)]

# Get points on arc
for n in range(0, int((360-angle)-angle2)):
    x = cx+int(r*math.cos(n*math.pi/180))
    y = cy+int(r*math.sin(n*math.pi/180))
    p2.append((x, y))
p2.append((cx, cy))

surface=pygame.Surface((250, 250), pygame.SRCALPHA)
# Background circle
pygame.draw.circle(surface, (0, 0, 255), (cx, cy), r)
# Draw pie segment
if len(p) > 2:
    pygame.draw.polygon(surface, (255, 0, 0), p)
if len(p2) > 2:
    pygame.draw.polygon(surface, (0, 255, 0), p2)
pygame.image.save(surface, "file.jpg")