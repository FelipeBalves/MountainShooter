
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.position_x = float(self.rect.centerx)

    def move(self):
        self.position_x -= ENTITY_SPEED[self.name]
        self.rect.centerx = int(self.position_x)
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
