import pygame
import math
from pygamegraph.constants import Constants
from pygamegraph.text import Text


class BaseGraph(pygame.sprite.Sprite):
    """
        Base graph class
    """
    def __init__(
            self,
            size: tuple,
            x: list,
            y: list,
            text_size: int = 20
    ):
        """
        :param size:
        :param x: first list
        :param y: second list
        """
        pygame.sprite.Sprite.__init__(self)
        self.x_list = x
        self.y_list = y
        self.size = size  # size of graph
        self.xscale = len(self.x_list) or 1
        self.yscale = len(self.y_list) or 1
        self.grid = False
        self.color = Constants.BLACK.value
        self.line_color = Constants.BLACK.value  # line color
        self.line_width = 1
        self.xpart_size = self.size[0] / self.xscale
        self.image = pygame.Surface(size, 5)
        self.image.fill(Constants.BLACK.value)
        self.rect = self.image.get_rect()
        self.y_top_text = Text(text_size)  # print max(self.y_list) on the left-top edge
        self.x_bottom_text = Text(text_size)  # print last element self.x_list on the right-bottom edge
        self.title = Text(text_size)
        self.xlabel = Text(text_size)  # name of x axis
        self.ylabel = Text(text_size)  # name of y axis
        self.ylabel.angle = 90

    @staticmethod
    def _compress(lst):
        step = 2
        finaly_len = len(lst) // step
        i = 0
        while len(lst) > finaly_len:
            step = step if step <= len(lst[i:]) else len(lst[i:])
            if max(lst) in lst[i:step + i]:
                lst[i] = max(lst)
            elif min(lst) in lst[i:step + i]:
                lst[i] = min(lst)
            else:
                lst[i] = math.ceil(sum(lst[i:step + i]) / len(lst[i:step + i]))
            for _ in range(step - 1):
                lst.pop(i + 1)
            i += 1
        return lst

    def update(self):
        self.y_top_text.update(text=str(max(self.y_list)),
                               xy=(self.rect.left, self.rect.top - self.ylabel.size),
                               color=Constants.BLACK.value)
        # self.x_bottom_text.update(text=str(self.x_list[-1]),
        #                           xy=(
        #                               self.rect.right + self.x_bottom_text.size,
        #                               self.rect.bottom + self.ylabel.size // 4
        #                           ),
        #                           color=Constants.BLACK.value)
        self.ylabel.update(xy=(
            (self.rect.left - self.ylabel.size // 2) - self.x_bottom_text.size - len(str(max(self.y_list))),
            (self.size[1] - self.rect.top) // 2),
            color=Constants.BLACK.value
        )
        self.xlabel.update(xy=(self.rect.centerx, self.rect.bottom + self.x_bottom_text.size),
                           color=Constants.BLACK.value)
        self.title.update(xy=(self.rect.centerx, self.rect.top - self.title.size),
                          color=Constants.BLACK.value)
        self.xscale = len(self.x_list)

    def draw_grid(self):
        max_y_list = max(self.y_list)
        startxy = (self.rect.left, self.rect.bottom)
        percent = max_y_list if max(self.y_list) > 0 else 1
        for xpart in range(self.xscale):
            pygame.draw.line(
                pygame.display.get_surface(),
                self.color,
                (startxy[0], self.rect.bottom),
                (startxy[0], self.rect.top),
                1
            )
            startxy = (
                self.rect.left + int((xpart + 1) * self.xpart_size),
                self.rect.bottom - int((self.y_list[xpart] / percent) * self.size[1])
            )
            number = Text(15)
            number.update(
                text=f'{self.x_list[xpart]}',
                xy=(startxy[0], self.rect.bottom + number.size // 2),
                color=Constants.BLACK.value
            )
            number.draw()
        startxy = (self.rect.left, self.rect.bottom - self.size[1] // 10)
        for ypart in range(1, 11):
            pygame.draw.line(
                pygame.display.get_surface(),
                self.color,
                (self.rect.left, startxy[1]),
                (self.rect.right, startxy[1]),
                1
            )
            startxy = (
                0,
                self.rect.bottom - ((self.size[1] // 10) * ypart)
            )
            number = Text(15)
            number.update(
                text=f'{(max_y_list // 10) * ypart}',
                xy=(self.rect.left - number.size - len(str(max_y_list)) // 2, startxy[1]),
                color=Constants.BLACK.value
            )
            number.draw()

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.color, self, self.line_width)
        percent = max(self.y_list) if max(self.y_list) > 0 else 1
        startxy = (self.rect.left, self.rect.bottom)
        self.xpart_size = self.size[0] / self.xscale
        self.title.draw()
        self.y_top_text.draw()
        # self.x_bottom_text.draw()
        self.ylabel.draw()
        self.xlabel.draw()
        if self.grid:
            self.draw_grid()
        for part in range(self.xscale):
            # number = Text(15)
            # number.update(
            #     text=f'{self.x_list[part]}',
            #     xy=(startxy[0], self.rect.bottom + number.size // 2),
            #     color=Constants.BLACK.value
            # )
            # number.draw()
            pygame.draw.line(
                pygame.display.get_surface(),
                self.line_color,
                startxy,
                (
                   self.rect.left + int((part + 1) * self.xpart_size),
                   self.rect.bottom - (self.y_list[part] / percent) * self.size[1]
                ),
                2
            )
            startxy = (self.rect.left + int((part + 1) * self.xpart_size),
                       self.rect.bottom - int((self.y_list[part] / percent) * self.size[1]))
