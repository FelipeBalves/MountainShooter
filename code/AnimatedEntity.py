import os
import pygame
from code.Entity import Entity

class AnimatedEntity(Entity):
    def __init__(self, name: str, position: tuple, folder_path: str, frame_duration: int = 5, loop: bool = True):
        super().__init__(name, position)
        self.frames: list[pygame.Surface] = self.load_frames(folder_path)
        self.frame_index = 0
        self.frame_duration = frame_duration
        self.frame_timer = 0
        self.loop = loop
        self.finished = False
        self.surf = self.frames[0]  # Inicializa com o primeiro frame
        self.rect = self.surf.get_rect(center=position)


    def load_frames(self, folder_path: str) -> list:
        frames = []
        for file in sorted(os.listdir(folder_path)):
            if file.endswith('.png'):
                img = pygame.image.load(os.path.join(folder_path, file)).convert_alpha()
                frames.append(img)
        return frames

    def move(self):
        pass

    def update_animation(self):
        if self.finished:
            return
        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                if self.loop:
                    self.frame_index = 0
                else:
                    self.finished = True
                    self.frame_index = len(self.frames) - 1
        self.surf = self.frames[self.frame_index]
