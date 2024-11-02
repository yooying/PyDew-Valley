import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)

		# Load assets
		self.import_assets()
		self.status = 'down_idle'
		self.frame_index = 0

		# General setup
		if len(self.animations[self.status]) > 0:
			self.image = self.animations[self.status][self.frame_index]
		else:
			self.image = pygame.Surface((32, 64))  # Default placeholder if no images are loaded
			self.rect = self.image.get_rect(center=pos)

		# Movement attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.speed = 200

	def import_assets(self):
		# Define animations dictionary
		self.animations = {
			'up': [], 'down': [], 'left': [], 'right': [],
			'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
			'right_hoe': [], 'left_hoe': [], 'up_hoe': [], 'down_hoe': [],
			'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
			'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []
		}

		# Load images for each animation
		for animation in self.animations.keys():
			full_path = '../graphics/character/' + animation
			self.animations[animation] = import_folder(full_path)
			print(f"{animation}: {len(self.animations[animation])} frames loaded")  # Debug print

	def input(self):
		keys = pygame.key.get_pressed()

		# WASD for movement
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
		# Normalize vector to maintain consistent speed in diagonal movement
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
