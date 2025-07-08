from abc import ABC

from code.AnimatedEntity import AnimatedEntity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Const import WIN_WIDTH
from code.Meteor import Meteor
from code.Entity import Entity


class EntityMediator(ABC):

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Meteor):
            if ent.rect.right < 0 - ent.rect.width:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.right > WIN_WIDTH + ent.rect.width:
                ent.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0 and ent.name.startswith("Meteor"):
                explosion = AnimatedEntity(
                    name="Explosion",
                    position=ent.rect.center,
                    folder_path="assets/explosion",
                    frame_duration=4,
                    loop=False
                )
                entity_list.append(explosion)
                entity_list.remove(ent)
                EntityMediator.__give_score(ent, entity_list)
            elif ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1,entity2)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Meteor) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Meteor):
            valid_interaction = True
        elif isinstance(ent1, Meteor) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Meteor):
            valid_interaction = True


        if valid_interaction:
            if ((ent1.rect.right >= ent2.rect.left) and
                (ent1.rect.left <= ent2.rect.right) and
                (ent1.rect.top <= ent2.rect.bottom) and
                (ent1.rect.bottom >= ent2.rect.top) and
                (ent1.rect.top <= ent2.rect.bottom)):

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Meteor, entity_list: list[Entity]):
        if enemy.last_dmg == "PlayerShot" and enemy.rect.x >= 0:
            for ent in entity_list:
                if ent.name == "Player":
                    ent.score += enemy.score




