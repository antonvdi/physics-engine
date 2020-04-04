# cd C:\Users\anton_mc03yx6\Documents\GitHub\physics_engine

import pygame
import time

pygame.init()
width = 700
height = 700
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0,255)
green = (0, 255, 0)
red = (255, 0, 0)

all_objects = list()

class Object:
	def __init__(self, mass, size, position_vertical, position_horizontal):
		self.mass = mass
		self.size = size
		self.force_horizontal = 0
		self.force_vertical = mass*9.82
		self.acceleration_horizontal = self.force_horizontal / mass
		self.acceleration_vertical = self.force_vertical / mass
		self.velocity_horizontal = -100
		self.velocity_vertical = 0
		self.position_horizontal = position_horizontal
		self.position_vertical = position_vertical
		self.last_update = time.time()

	def update(self):
		delta_time = (time.time()-self.last_update)*5
		self.velocity_horizontal += self.acceleration_horizontal*delta_time
		self.velocity_vertical += self.acceleration_vertical*delta_time
		self.position_horizontal += self.velocity_horizontal*delta_time
		self.position_vertical += self.velocity_vertical*delta_time
		self.last_update = time.time()

		pygame.draw.circle(screen, blue, (int(self.position_horizontal), int(self.position_vertical)), self.size)

	def wallcollision(self):
		if self.position_vertical + self.size >= height:
			self.velocity_vertical = -abs(self.velocity_vertical * 0.90)
			self.position_vertical = height-self.size

		if self.position_vertical - self.size <= 0:
			self.velocity_vertical = abs(self.velocity_vertical * 0.90)
			self.position_vertical = self.size

		if self.position_horizontal + self.size >= width:
			self.velocity_horizontal = -abs(self.velocity_horizontal * 0.90)
			self.position_horizontal = width-self.size

		if self.position_horizontal - self.size <= 0:
			self.velocity_horizontal = abs(self.velocity_horizontal * 0.90)
			self.position_horizontal = self.size

def main():
	done = False
	object1 = Object(20, 20, 350, 350)
	object2 = Object(40, 40, 100, 100)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		screen.fill(black)
		object1.update()
		object2.update()
		object1.wallcollision()
		object2.wallcollision()
		
		
		pygame.display.flip()

def collision_circle(circle1, circle2):
	pass

main()