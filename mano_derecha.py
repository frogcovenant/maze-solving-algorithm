import numpy as np
import cv2
import os
from PIL import Image

maze = [
[1,.25,1,1,1],
[1,0,0,0,1],
[1,0,1,1,1],
[1,0,0,0,1],
[1,1,1,0,1],
]

counter = 0
maze_np = np.array(maze) * 255
maze_np = 255 - maze_np
cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np) # laberinto vacio
counter += 1
pos = [4, 3] # posicion de inicio
print(pos)
maze_np[pos[0], pos[1]] = 128
cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)
facing = "up"
visited= {} # añadir a visitados

while 1:
    try:
        if maze[pos[0]][pos[1]] == 0.25: 
            print("termino")
            break # revisar que llego

        print(f"pos actual: {pos[0]}, {pos[1]}\t facing: {facing}")
        #print(pos for pos in visited)
        #input()
        if pos[0] >= 0 and pos[0] < len(maze[0]):
                if pos[1] >= 0 and pos[1] < len(maze[1]): # revisar que no se ha salido del arreglo
                    if facing == "up":
                        if maze[pos[0]][pos[1]+1] in [0, 0.25]: # si a tu derecha hay camino, debes girar
                            counter += 1
                            facing = "right"
                            pos[1]+=1
                            
                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]-1][pos[1]] in [0, 0.25]: # sino, trata de seguir adelante
                            counter += 1
                            pos[0] -= 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]][pos[1]-1] in [0, 0.25]: # sino, revisa tu izquierda
                            counter += 1
                            facing = "left"
                            pos[1]-=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        else: # sino, regresa
                            counter += 1
                            facing = "down"
                            pos[0] += 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                    if facing == "down":
                        if maze[pos[0]][pos[1]] == 2: break # revisar que llego
                        if maze[pos[0]][pos[1]-1] in [0, 0.25]: # si a tu derecha hay camino, debes girar
                            counter += 1
                            facing = "left"
                            pos[1]-=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]+1][pos[1]] in [0, 0.25]: # sino, trata de seguir adelante
                            counter += 1
                            pos[0] += 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]][pos[1]+1] in [0, 0.25]: # sino, revisa tu izquierda
                            counter += 1
                            facing = "right"
                            pos[1]+=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        else: # sino, regresa
                            counter += 1
                            facing = "up" 
                            pos[0] -= 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                    if facing == "left":
                        if maze[pos[0]][pos[1]] == 2: break # revisar que llego
                        if maze[pos[0]-1][pos[1]] in [0, 0.25]: # si a tu derecha hay camino, debes girar
                            counter += 1
                            facing = "up"
                            pos[0]-=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)
                            
                        elif maze[pos[0]][pos[1]-1] in [0, 0.25]: # sino, trata de seguir adelante
                            counter += 1
                            pos[1] -= 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]+1][pos[1]] in [0, 0.25]: # sino, revisa tu izquierda
                            counter += 1
                            facing = "down"
                            pos[0]+=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)
                        
                        else: # sino, regresa
                            counter += 1
                            facing = "right" 
                            pos[1] += 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                    if facing == "right":
                        if maze[pos[0]][pos[1]] == 2: break # revisar que llego
                        if maze[pos[0]+1][pos[1]] in [0, 0.25]: # si a tu derecha hay camino, debes girar
                            counter += 1
                            facing = "down"
                            pos[0]+=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]][pos[1]+1] in [0, 0.25]: # sino, trata de seguir adelante
                            counter += 1
                            pos[1] += 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        elif maze[pos[0]-1][pos[1]] in [0, 0.25]: # sino, revisa tu izquierda
                            counter += 1
                            facing = "up"
                            pos[0]-=1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

                        else: # sino, regresa
                            counter += 1
                            facing = "left" 
                            pos[1] -= 1

                            maze_np[pos[0], pos[1]] = 128
                            cv2.imwrite("maze_images/maze"+str(counter)+".png", maze_np)

    except:
        continue
        print("out of bonds")

