import pygame

from pygamegraph.constants import Constants


class Text(pygame.sprite.Sprite):
    def __init__(self, size: int = 20):
        pygame.sprite.Sprite.__init__(self)
        self._size = size
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), self._size)
        self.text = ''
        self.angle = 0
        self.color = Constants.BLACK.value
        self.text_surface = self.font.render(str(self.text), True, self.color)
        self.text_rect = self.text_surface.get_rect()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value
        self.font = pygame.font.SysFont(pygame.font.match_font('arial'), self._size)

    def update(self, xy: tuple, color: tuple, text=''):
        self.text = text if text != '' else self.text
        self.text_surface = self.font.render(str(self.text), True, color)
        self.text_surface = pygame.transform.rotate(self.text_surface, self.angle)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = xy

    def draw(self):
        pygame.display.get_surface().blit(self.text_surface, self.text_rect)
