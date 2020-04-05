# cd C:\Users\anton_mc03yx6\Documents\GitHub\physics_engine

import pygame
import time, math

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
n = 0

class Object:
	def __init__(self, mass, size, position_vertical, position_horizontal, color):
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
		self.color = color

	def update(self):
		delta_time = (time.time()-self.last_update) * 7
		self.velocity_horizontal += self.acceleration_horizontal*delta_time
		self.velocity_vertical += self.acceleration_vertical*delta_time
		self.position_horizontal += self.velocity_horizontal*delta_time
		self.position_vertical += self.velocity_vertical*delta_time
		self.last_update = time.time()

		pygame.draw.circle(screen, self.color, (int(self.position_horizontal), int(self.position_vertical)), self.size)

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
	object1 = Object(20, 20, 350, 350, blue)
	object2 = Object(40, 40, 100, 100, red)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		screen.fill(black)
		object1.update()
		object2.update()
		object1.wallcollision()
		object2.wallcollision()
		collision_circle(object1, object2)
		#collision_circle(object2, object1)
		
		
		pygame.display.flip()

def collision_circle(circle1, circle2):
	#the vector in between the two circles, cartesian coordinates
	position_vector_horizontal = circle2.position_horizontal - circle1.position_horizontal
	position_vector_vertical = circle2.position_vertical - circle1.position_vertical

	#polar coordinates
	position_vector_length = math.sqrt((position_vector_horizontal)**2+(position_vector_vertical)**2)
	position_vector_direction = math.atan(position_vector_vertical/position_vector_horizontal)

	#calculate new velocities
	if position_vector_length <= circle1.size + circle2.size:
		tangent_vector_horizontal = position_vector_horizontal
		tangent_vector_vertical = -position_vector_vertical

		tangent_vector_direction = math.atan(tangent_vector_vertical/tangent_vector_horizontal)
		tangent_vector_length = math.sqrt(tangent_vector_horizontal**2+tangent_vector_vertical**2)

		circle1_velocity = math.sqrt(circle1.velocity_horizontal**2+circle1.velocity_vertical**2)

		approach_direction = math.acos((circle1.velocity_horizontal*tangent_vector_horizontal+circle1.velocity_vertical*tangent_vector_vertical)/(circle1_velocity*tangent_vector_length))

		outgoing_direction = approach_direction + tangent_vector_direction

		circle1.velocity_horizontal = circle1_velocity * math.cos(outgoing_direction)
		circle1.velocity_vertical = circle1_velocity * math.sin(outgoing_direction)

main()