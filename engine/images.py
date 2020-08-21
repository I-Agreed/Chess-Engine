import pygame

images = ["test", "pawn", "king", "queen", "bishop", "rook", "knight"]


def getImages(tileSize, files=images):
    out = {}
    for i in images:
        out[i + "_white"] = pygame.transform.scale(pygame.image.load("image_src\\" + i + "_white.png").convert_alpha(),
                                                   (tileSize, tileSize))
        out[i + "_black"] = pygame.transform.scale(pygame.image.load("image_src\\" + i + "_black.png").convert_alpha(),
                                                   (tileSize, tileSize))
    return out


if __name__ == "__main__":
    getImages(32)
