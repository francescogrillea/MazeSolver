from PIL import Image
from Labirinto import Labirinto
from SearchingAlgorithms import *

def identifyWalls(img, rowNumber, colNumber):
    """
    :param img: maze picture
    :param rowNumber: number of steps that can be done from low to high
    :param colNumber: number of steps that can be done left low to right
    :return: the position of the walls at every step
    """

    neutralColor = (255, 255, 255) #white
    width, height = img.size
    block_width = width / colNumber
    block_height = height / rowNumber
    walls = {}

    for i in range(rowNumber):
        for j in range(colNumber):
            block = img.crop((j*block_width, i*block_height ,(j+1)*block_width, (i+1)*block_height))
            x,y = block.size
            #color = block.getpixel((x/2,y/2))
            block_wall = []

            #the pixel of each edge of the block
            left = (0, y/2)
            up = (x/2, 0)
            right = (x-1, y/2)
            bottom = (x/2, y-1)

            #check if there is a wall for each side of the block
            #left
            if not block.getpixel(left) == neutralColor:
                block_wall.append('left')
            #up
            if not block.getpixel(up) == neutralColor:
                block_wall.append('up')
            #right
            if not block.getpixel(right) == neutralColor:
                block_wall.append('right')
            #bottom
            if not block.getpixel(bottom) == neutralColor:
                block_wall.append('bottom')

            walls[f'({i},{j})'] = block_wall
    return walls


if __name__ == '__main__':
    try:
        img = Image.open('labirinto.jpg')
        walls = identifyWalls(img, 4, 4)
        img.close()
        #print(walls)

        startPosition = '(3,0)'
        endPosition = '(1,3)'
        mylab = Labirinto(startPosition, endPosition, walls)
        solution = depth_first_search_tree(mylab)
        print(solution[0])
        print(solution[1])
        print(solution[2])
        print(solution[3])

    except IOError as e:
        print('An error occurred:' + e)
