import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Wildlife Project")

# Load images (make sure background.png and penguin.png are in the same folder)
bg = pygame.transform.scale(pygame.image.load("background.png"), (500, 500))
animal = pygame.transform.scale(pygame.image.load("penguin.png"), (200, 200))

# Kid-style font and fun facts
font = pygame.font.SysFont("comicsansms", 24)
fact1 = font.render("Animal: Emperor Penguin", True, "blue")
fact2 = font.render("Fact: Penguins cant fly!", True, "red")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0, 0))
    screen.blit(animal, (150, 80))
    screen.blit(fact1, (90, 310))
    screen.blit(fact2, (95, 360))
    pygame.display.flip()

pygame.quit()
