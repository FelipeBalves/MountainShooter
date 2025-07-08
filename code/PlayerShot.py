from code.AnimatedEntity import AnimatedEntity
from code.Const import ENTITY_SPEED



class PlayerShot(AnimatedEntity):
    def __init__(self, name: str, position: tuple):
        super().__init__(
            name=name,
            position=position,
            folder_path="assets/shot_anim",
            frame_duration=2,
            loop=True
        )
    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]

