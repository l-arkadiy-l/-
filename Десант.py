import pygame


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load("data/mountains.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("data/pt.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)
            screen.blit(self.image, (self.rect.x, self.rect.y))


if __name__ == '__main__':
    SIZE = width, height = (700, 500)
    mountain = Mountain()
    landings = pygame.sprite.Group()
    screen = pygame.display.set_mode(SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                landings.add(Landing(event.pos))
        for i in landings:
            i.update()
        screen.fill(pygame.Color('black'))
        landings.draw(screen)
        screen.blit(mountain.image, (mountain.rect.x, mountain.rect.y))
        pygame.display.flip()
