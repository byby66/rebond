import pygame

# Initialisation
pygame.init()

# Fenêtre
LARGEUR = 800
HAUTEUR = 500
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Animation Pygame - Balle rebondissante")

# Horloge (pour limiter le nombre d'images par seconde)
clock = pygame.time.Clock()

# Position de la balle
x = 100
y = 100

# Vitesse
vx = 5
vy = 4

# Rayon
rayon = 25

running = True

while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement de la balle
    x += vx
    y += vy

    # Rebond sur les bords
    if x <= rayon or x >= LARGEUR - rayon:
        vx = -vx

    if y <= rayon or y >= HAUTEUR - rayon:
        vy = -vy

    # Dessin
    screen.fill((30, 30, 30))                      # Fond gris foncé
    pygame.draw.circle(screen, (255, 100, 100), (x, y), rayon)

    # Mise à jour de la fenêtre
    pygame.display.flip()

    # 60 images par seconde
    clock.tick(60)

pygame.quit()