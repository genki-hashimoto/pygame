import pygame
from pygame.locals import *
import sys

pygame.init()

while True:
	for event in pygame.event.get():
		if event.type == QUIT: sys.exit
		if event.type == KEYDOWN:
			if event.key == K_a:
				print "a"
