import pygame

# C
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_PURPLE = (128, 0, 128)

# E
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Player': 0,
    'PlayerShot': 0,
    'Meteor0': 50,
    'Meteor1': 50,
    'Meteor2': 100,
    'Meteor3': 100,
    'Meteor4': 100,
    'Meteor5': 150,
    'Meteor6': 400,
    'Meteor7': 100,
    'Meteor8': 150,
    'Meteor9': 500,
    'Explosion': 0,
    'ExhaustTop': 0,
    'ExhaustBottom': 0
}

ENTITY_SHOT_DELAY = {
    'Player': 12,

}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0.25,
    'Level1Bg2': 0.25,
    'Level1Bg3': 0.25,
    'Level1Bg4': 0.25,
    'Level1Bg5': 0.25,
    'Level1Bg6': 0.25,
    'Level1Bg7': 0.25,
    'Player': 5,
    'PlayerShot': 10,
    'Meteor0': 2,
    'Meteor1': 2,
    'Meteor2': 3,
    'Meteor3': 3,
    'Meteor4': 4,
    'Meteor5': 5,
    'Meteor6': 10,
    'Meteor7': 4,
    'Meteor8': 5,
    'Meteor9': 10,
    'Explosion': 0,
    'ExhaustTop': 0,
    'ExhaustBottom': 0
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Player': 100,
    'PlayerShot': 1,
    'Meteor0': 80,
    'Meteor1': 100,
    'Meteor2': 90,
    'Meteor3': 80,
    'Meteor4': 120,
    'Meteor5': 150,
    'Meteor6': 80,
    'Meteor7': 70,
    'Meteor8': 150,
    'Meteor9': 100,
    'Explosion': 999,
    'ExhaustTop': 999,
    'ExhaustBottom':999
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Player': 999,
    'PlayerShot': 15,
    'Meteor0': 15,
    'Meteor1': 20,
    'Meteor2': 20,
    'Meteor3': 5,
    'Meteor4': 10,
    'Meteor5': 15,
    'Meteor6': 20,
    'Meteor7': 15,
    'Meteor8': 15,
    'Meteor9': 25,
    'Explosion': 0,
    'ExhaustTop': 0,
    'ExhaustBottom': 0
}

# L
LAYER_X = {
    'Level1Bg0': 0,
    'Level1Bg1': 100,
    'Level1Bg2': 100,
    'Level1Bg3': 100,
    'Level1Bg4': 1200,
    'Level1Bg5': 1200,
    'Level1Bg6': 2000,
    'Level1Bg7': 2800,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}
# S


SPAWN_TIME = 4000


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}
