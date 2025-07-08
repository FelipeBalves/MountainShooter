#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT, LAYER_X
from code.Background import Background
from code.Meteor import Meteor
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(8):  # 0 a 5
                    layer_name = f'Level1Bg{i}'
                    x = LAYER_X[layer_name]

                    list_bg.append(Background(layer_name, (x, 0)))

                    list_bg.append(Background(layer_name, (x, 0)))

                return list_bg
            case "Player":
                return Player("Player", (50, WIN_HEIGHT / 2 -30))
            case 'Meteor0':
                return Meteor('Meteor0', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor1':
                return Meteor('Meteor1', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor2':
                return Meteor('Meteor2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor3':
                return Meteor('Meteor3', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor4':
                return Meteor('Meteor4', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor5':
                return Meteor('Meteor5', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor6':
                return Meteor('Meteor6', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor7':
                return Meteor('Meteor7', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor8':
                return Meteor('Meteor8', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
            case 'Meteor9':
                return Meteor('Meteor9', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 64)))
        return None