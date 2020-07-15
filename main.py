import pygame #lets us use pygame
import turtle #lets us use turtle turtle
screen = pygame.display.set_mode((800,600)) #graphics
#color time C:
t = turtle.Turtle() #names turtle t so its easier to type in the rest of the code


YELLOW = pygame.Color(255,215,0)
White = pygame.Color(255,255,255)
screen.fill(YELLOW)

def draw_square(size,color):
  t.pendown()
  t.color(color)
  for x in range(4):
    t.forward(size)
    t.right(90)
  t.penup()

def draw_circle(size,color):
  t.pendown()
  t.color(color)
  for x in range(36):
    t.forward(size)
    t.right(10)
  t.penup()

def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit(0)
    screen.fill(YELLOW)
    t.speed(100)
    draw_square(100, 'red')
    draw_circle(10, 'blue')
    t.right(10)


main()


