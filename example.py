import pygame
import random

from pygamegraph.base_graph import BaseGraph

HEIGHT = 700
WIDTH = 1000
MAXLEN = 20
FPS = 1
GREEN = (255, 255, 255)
BLUE = (0, 0, 255)


class Example:
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Pygamegraph example")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    def run(self):
        first = []#[i for i in range(20)]
        second = []#[0 for _ in range(20)]

        # init graph
        graph = BaseGraph(
            x=first,
            y=second,
            size=(650, 550)
        )
        graph.rect.left = 50  # left graph edge
        graph.rect.top = 50  # top graph edge

        graph.title.text = 'Title'
        graph.title.size = 30

        graph.xlabel.text = 'Text1'
        graph.xlabel.size = 25

        graph.ylabel.text = 'Text2'
        graph.ylabel.size = 25

        graph.grid = True

        graph.line_color = BLUE  # color of the line
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.fill(GREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # first.append(random.randint(0, 20))
            first.append(first[-1] + 1 if first else 0)
            if len(first) > MAXLEN:
                first.pop(0)
            second.append(random.randint(0, 100))
            print(second)
            if len(second) > MAXLEN:
                second.pop(0)
            graph.update()
            graph.draw()
            pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    example = Example()
    example.run()
