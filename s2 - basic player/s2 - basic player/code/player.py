import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# general setup
		self.image = pygame.Surface((32, 64))
		self.image.fill('green')
		self.rect = self.image.get_rect(center=pos)

		# movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200

	def input(self):
		keys = pygame.key.get_pressed()

		# Use WASD for movement
		if keys[pygame.K_w]:  # Up
			self.direction.y = -1
		elif keys[pygame.K_s]:  # Down
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_d]:  # Right
			self.direction.x = 1
		elif keys[pygame.K_a]:  # Left
			self.direction.x = -1
		else:
			self.direction.x = 0

	def move(self, dt):
		# Normalize vector to ensure consistent speed in diagonal movement
		if self.direction.magnitude() > 0:
			self.direction = self.direction.normalize()

		# Horizontal movement
		self.pos.x += self.direction.x * self.speed * dt
		self.rect.centerx = self.pos.x

		# Vertical movement
		self.pos.y += self.direction.y * self.speed * dt
		self.rect.centery = self.pos.y

	def update(self, dt):
		self.input()
		self.move(dt)
