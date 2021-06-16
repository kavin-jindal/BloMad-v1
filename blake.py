from numpy.core.shape_base import block
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader # you have to apply this shader to enties for them to recieve shadows.
import sys
app = Ursina()
'''
EditorCamera()
Entity(model='plane', scale=10, color=color.gray, shader=lit_with_shadows_shader)
Entity(model='cube', y=1, shader=lit_with_shadows_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True)
'''
block1 = 'textures/grass'
block2 = 'textures/brick'
block3 = 'textures/stoneg'
block4 = 'textures/wood2'
block5 = 'textures/birch'
block6 = 'textures/Dirt_11'

window.fullscreen = True
stone = load_texture('textures/stoneg')
block_pick = 1
def update():
    global block_pick 
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['x']:
        application.quit()
    if held_keys['t']:
        bg = BG()
    if held_keys['y']:
        return

        
gold = 0
counter = Text(text='Blocks destroyed: 0', y=.45, x=0, scale=1, origin=(0,0))
dev = Text(text='Developed by: Kavin Jindal', y=.435, x=.62, scale=.8)
vers = Text(text='BloMad v1.0', y=.406, x=.75, scale=.8)



class MenuMenu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused=True)

        # Create empty entities that will be parents of our menus content
        self.main_menu = Entity(parent=self, enabled=True)
        self.options_menu = Entity(parent=self, enabled=False)
        self.help_menu = Entity(parent=self, enabled=False)

        # Add a background. You can change 'shore' to a different texture of you'd like.
        

        # [MAIN MENU] WINDOW START
        # Titile of our menu
        Text("Press 'x' to exit", parent=self.main_menu, y=0.4, x=0, origin=(0,0))
        
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture= 'textures/psky',
            scale = 1000,
            double_sided = True)

class BG(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad', 
            visible = False,
            
        )
class Voxel(Button):
    def __init__(self, position=(0,0,0), texture = 'textures/Dirt_11'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            smooth = True,
            highlight_color = color.lime,
            #
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block1)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block2)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block3)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block4)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block5)
                if block_pick == 6:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block6)

                if held_keys['x']:
                    application.quit()

            if key == 'right mouse down':
                destroy(self)
                global gold
                gold += 1
                counter.text = str(gold)

class Ground(Button):
    def __init__(self, position = (0,0,0), texture='textures/stoneg'):
        super().__init__(
            parent = scene,
            position = position, 
            model = 'cube',
            texture = texture,
            origin_y = 0.5,
            color = color.color(0,0,random.uniform(0.9,1)),
            smooth = True,
            highlight_color = color.lime,
        )     

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block1)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block2)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block3)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block4)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block5)
                if block_pick == 6:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block6)
                

                if held_keys['x']:
                    application.quit()

class Tree(Button):
    def __init__(self, position = (5,0,5), texture = 'textures/treel'):
        super().__init__(
            parent = scene, 
            position = position, 
            texture = texture, 
            model = 'cube',
            origin_y = 0.5, 
            color = color.color(0,0,random.uniform(0.9,1)),
            smooth = True,
            highlight_color = color.green,
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block1)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block2)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block3)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block4)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block5)
                if block_pick == 6:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block6)
                

                if held_keys['x']:
                    application.quit()

            if key == 'right mouse down':
                destroy(self)
                global gold
                gold += 1
                counter.text = str(gold)
class Dirt(Button):
    def __init__(self, position = (5,0,5), texture = 'textures/Dirt_11'):
        super().__init__(
            parent = scene, 
            position = position, 
            texture = texture, 
            model = 'cube',
            origin_y = 0.5, 
            color = color.color(0,0,random.uniform(0.9,1)),
            smooth = True,
            highlight_color = color.green,
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block1)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block2)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block3)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block4)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block5)
                if block_pick == 6:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block6)

                if held_keys['x']:
                    application.quit()

            if key == 'right mouse down':
                destroy(self)
                global gold
                gold += 1
                counter.text = str(gold)

class Wood(Button):
    def __init__(self, position = (5,0,5), texture = 'textures/tree'):
        super().__init__(
            parent = scene, 
            position = position, 
            texture = texture, 
            model = 'cube',
            origin_y = 0.5, 
            color = color.color(0,0,random.uniform(0.9,1)),
            smooth = True,
            highlight_color = color.green,
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block1)
                if block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block2)
                if block_pick == 3:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block3)
                if block_pick == 4:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block4)
                if block_pick == 5:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block5)
                if block_pick == 6:
                    voxel = Voxel(position = self.position + mouse.normal, texture=block6)

                if held_keys['x']:
                    application.quit()

            if key == 'right mouse down':
                destroy(self)
                global gold
                gold += 1
                counter.text = str(gold)
for y in range(31):
    for z in range(31):
        voxel = Voxel(position = (y,0,z))

for y in range(31):
    for z in range(31):
        voxel = Dirt(position = (y,-1,z))

for y in range(31):
    for z in range(31):
        voxel = Dirt(position = (y,-2,z))

for y in range(31):
    for z in range(31):
        voxel = Ground(position = (y,-3,z))



    




        
# TREES
for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,2,10))

for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,1,10))

for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,3,10))
# tree leaves
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,10))
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,9))
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,3,9))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,10))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,9))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,11))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,3,11))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,11))

#------------------
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,4,10))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,4,9))


for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,4,10))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,4,11))

#---------------------------------

# another one

for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,2,30))

for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,1,30))

for y in range(1):
    for z in range(1):
        voxel = Wood(position = (0,3,30))
# tree leaves
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,30))
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,29))
for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,3,29))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,30))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,29))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,3,31))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,3,31))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,3,31))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (-1,4,30))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,4,29))


for y in range(1):
    for z in range(1):
        voxel = Tree(position = (1,4,30))

for y in range(1):
    for z in range(1):
        voxel = Tree(position = (0,4,31))


#_------------------------_
#-____________-----------------------



# Base layers
#-------------------------------------




        




player = FirstPersonController(speed = 10)
sky = Sky()
text = MenuMenu()
app.run()