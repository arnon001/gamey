# collider functions #
def checkCollision(object1, object2):
    if object1.x + object1.w <=object2.x+object2.w:
        return True