import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code import Entity
from code.AnimatedEntity import AnimatedEntity
from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, C_GREEN
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, player_score: list[int]):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.player = EntityFactory.get_entity('Player')
        self.player.score = player_score[0]
        self.entity_list.append(self.player)
        self.spawn_time = SPAWN_TIME
        self.spawn_thresholds = [1000, 200, 3000, 4000]  # pontuações que diminuem o tempo de spawn
        self.spawn_speedups = [SPAWN_TIME // 2, SPAWN_TIME // 3, SPAWN_TIME // 4, SPAWN_TIME // 5]
        self.current_threshold_index = -1
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)



    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:

            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if isinstance(ent, AnimatedEntity):
                    ent.update_animation()
                    if ent.finished:
                        self.entity_list.remove(ent)
                        continue

                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot:
                        self.entity_list.append(shoot)
                    player_score[0] = ent.score
                    self.level_text(14, f"Player - Health: {ent.health} | Score: {ent.score}", C_GREEN, (10, 10))
                    exhaust1 = self.player.exhaust_top
                    exhaust2 = self.player.exhaust_bottom

                    exhaust1.rect.center = (self.player.rect.centerx - 70, self.player.rect.centery - 12)
                    exhaust2.rect.center = (self.player.rect.centerx - 70, self.player.rect.centery + 12)

                    exhaust1.update_animation()
                    exhaust2.update_animation()

                    self.window.blit(exhaust1.surf, exhaust1.rect)
                    self.window.blit(exhaust2.surf, exhaust2.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Meteor0', 'Meteor1', 'Meteor2', 'Meteor3', 'Meteor4', 'Meteor5', 'Meteor6', 'Meteor7', 'Meteor8', 'Meteor9'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            if self.current_threshold_index + 1 < len(self.spawn_thresholds):
                next_threshold = self.spawn_thresholds[self.current_threshold_index + 1]
                if self.player.score >= next_threshold:
                    self.current_threshold_index += 1
                    self.spawn_time = self.spawn_speedups[self.current_threshold_index]
                    pygame.time.set_timer(EVENT_ENEMY, self.spawn_time)

            pygame.display.flip()

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            if self.player.health <= 0:
                return True


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
