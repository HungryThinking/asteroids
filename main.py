import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidField = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.is_collision(player):
				sys.exit("Game over!")
			for shot in shots:
				if asteroid.is_collision(shot):
					shot.kill()
					asteroid.split()
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
