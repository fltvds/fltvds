import pygame, random, sys

player_image = "player.png"
asteroid_image = ["asteroid.png", "asteroid1.png", "asteroid2.png", "asteroid3.png", "asteroid4.png"]

pygame.init()
surface = pygame.display.set_mode([640,480])

class Player:
	def __init__(self):
		self.x = 320
		self.y = 240
		self.vx = 0
		self.vy = 0
		self.img = pygame.image.load(player_image)
	def update(self, dt):
		self.x += self.vx * dt
		self.y += self.vy * dt
	def draw(self, s):
		s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
		
class Enemy:
	def __init__(self):
		self.x = random.uniform(0, 640)
		self.y = 0
		self.vx = 0
		self.vy = random.uniform(1, 2)
		i = random.randint(0, 4)
		self.img = pygame.image.load(asteroid_image[i])
	def update(self, dt):
		self.x += self.vx * dt
		self.y += self.vy * dt
		if(self.y > 480):
			self.die()
	def collide(self, b, particles):
		if self.x + self.img.get_width() > b.x > self.x - self.img.get_width():
                    if self.y + self.img.get_height() > b.y > self.y - self.img.get_height():
                        particles.extend([Particle(self.x, self.y) for _ in range(10)])
                        self.die()
	def die(self):
		self.y = 0
		self.x = random.uniform(0, 640)
		self.vy = random.uniform(1, 2)
	def draw(self, s):
		s.blit(self.img, [self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2])
		
class Bullet:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = -1
		self.ay = -1
		self.size = 4
		
	def update(self, dt):
		self.vy += self.ay * dt
		self.x += self.vx * dt
		self.y += self.vy * dt
	def shoot(self, p):
		if self.y < 0:
			self.x = p.x
			self.y = p.y
			self.vx = 0
			self.vy = -1
			self.ay = -1
	def draw(self, s):
		pygame.draw.rect(s,[205,50,0],[self.x - self.size, self.y - self.size, self.size * 2, self.size * 2],0)
		
class Particle:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vx = random.uniform(-2, 2)
		self.vy = random.uniform(-2, 2)
		self.col = [random.randint(0,105), random.randint(0,155), 0]
	def update(self, dt):
		self.x += self.vx * dt
		self.y += self.vy * dt
	def draw(self, s):
		pygame.draw.rect(s,self.col,[self.x, self.y, 5, 5],0)
		
def clean_particles(particles):
	particles = [p for p in particles if not 0 < p.y < 480 or not 0 < p.x < 640]
		
		
player = Player()
bullet = Bullet(0,0)
enemies = [Enemy() for _ in range(10)]
particles = []

default_movement = 5

clock = pygame.time.Clock()	
while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				player.vy += -default_movement
			if e.key == pygame.K_DOWN:
				player.vy += default_movement
			if e.key == pygame.K_LEFT:
				player.vx += -default_movement
			if e.key == pygame.K_RIGHT:
				player.vx += default_movement
			if e.key == pygame.K_SPACE:
				bullet.shoot(player)
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_UP:
				player.vy -= -default_movement
			if e.key == pygame.K_DOWN:
				player.vy -= default_movement
			if e.key == pygame.K_LEFT:
				player.vx -= -default_movement
			if e.key == pygame.K_RIGHT:
				player.vx -= default_movement

	dt = clock.get_time() / (1.0 / 60.0 * 1000)
	player.update(dt)
	bullet.update(dt)
	for enemy in enemies:
		enemy.update(dt)
		enemy.collide(bullet, particles)	
	for particle in particles:
		particle.update(dt)
	particles = [p for p in particles if 0 < p.y < 480 and 0 < p.x < 640]
	
	surface.fill([0,0,0])
	bullet.draw(surface)
	player.draw(surface)	
	for particle in particles:
		particle.draw(surface)
	for enemy in enemies:
		enemy.draw(surface)
	
	pygame.display.flip()
	clock.tick_busy_loop(60)
