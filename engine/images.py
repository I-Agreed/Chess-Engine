import pygame
images = ["test.png"]

def getImages(tileSize, files=images):
    out = {}
    for i in images:
        out[i.split(".")[0]] = pygame.transform.scale(pygame.image.load("image_src\\" + i).convert(),
                                                      (tileSize, tileSize))
    return out

if __name__ == "__main__":
    getImages(32)