import pygame
import time

class conway:
    mouse_x = 0
    mouse_y = 0
    def __init__(self, window_width, window_height, cell_width, cell_height):
        self.screen=pygame.display.set_mode([window_width, window_height])
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.coords = []
        self.color = [255, 255, 255]
        for y in range(round(pygame.display.get_window_size()[0] / cell_width)):
            self.coords.append([])
            for x in range(round(pygame.display.get_window_size()[1] / cell_height)):
                self.coords[y].append(0)
        
        self.coords[15][15] = 1
        self.coords[15][14] = 1
        self.coords[14][15] = 1
        self.coords[13][15] = 1
        self.coords[14][13] = 1
        
        for i in range(len(self.coords)):
            print(self.coords[i])
        
    def draw_rect(self, x, y, width, height):
        pygame.draw.rect(self.screen, self.color, [x, y, width, height], 0)
        
    def set_color(self, r, g, b):
        self.color = [r, g, b]

    def update(self):
        counter = 0
        self.screen.fill([0, 0, 0])
        new_coords = []
        for y in range(round(pygame.display.get_window_size()[0] / self.cell_width)):
            new_coords.append([])
            for x in range(round(pygame.display.get_window_size()[1] / self.cell_height)):
                new_coords[y].append(0)
                
        for y in range(len(self.coords)):
            for x in range(len(self.coords[y])):
                neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if i == 0 and j == 0:
                                a = 2
                            elif self.coords[y+i][x+j] == True:
                                neighbours+=1
                        except IndexError:
                            counter+=1
                if neighbours == 3:
                    new_coords[y][x] = 1
                elif neighbours == 2 and self.coords[y][x] == True:
                    new_coords[y][x] = 1
                else:
                    new_coords[y][x] = 0
        self.coords = new_coords
        print("updated", counter)
        for i in range(len(self.coords)):
            print(self.coords[i])
        
    def render(self):
        self.screen.fill([0, 0, 0])
        for y in range(len(self.coords)):
            for x in range(len(self.coords[y])):
                if self.coords[y][x] == True:
                    self.draw_rect(x*self.cell_width, y*self.cell_height, self.cell_width, self.cell_width) 

running=True
c = conway(750, 750, 25, 25)
c.render()
while running:

    for event in pygame.event.get():
        if event.type==pygame.MOUSEMOTION:
            c.mouse_x, c.mouse_y = pygame.mouse.get_pos()
            #print(c.mouse_x, c.mouse_y)
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                c.update()
                c.render()
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()

pygame.quit()
print("end")