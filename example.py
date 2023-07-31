import pygame
import random

from pygamegraph.base_graph import BaseGraph

HEIGHT = 500
WIDTH = 800
MAXLEN = 20
FPS = 10
GREEN = (50, 100, 50)
BLUE = (0, 0, 255)


class Example:
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Pygamegraph example")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    def run(self):
        first = []
        second = []

        # init graph
        graph = BaseGraph(
            x=first,
            y=second,
            size=(250, 150)
        )
        graph.rect.left = 30  # left graph edge
        graph.rect.top = 30  # top graph edge
        graph.color = BLUE  # color of the line
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(GREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            first.append(random.randint(0, 20))
            if len(first) > MAXLEN:
                first.pop(0)
            second.append(random.randint(0, 400))
            if len(second) > MAXLEN:
                second.pop(0)
            graph.update()
            graph.draw()
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    example = Example()
    example.run()
