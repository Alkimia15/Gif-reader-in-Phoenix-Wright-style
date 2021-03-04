import pyglet

from pyglet import shapes

frase = input('insert frase: ')

ag_file = input('insert the gif name: ')

animation = pyglet.resource.animation(ag_file)

sprite = pyglet.sprite.Sprite(animation)

win = pyglet.window.Window(width=1280, height=720)

bg = pyglet.image.load('courtroom.png')

label = pyglet.text.Label(frase,
                          font_name='Times New Roman',
                          font_size=24,
                          x=win.width//5, y=win.height//5,
                          anchor_x='center', anchor_y='center')

batch = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()
co_x = 75
co_y = 10
co2_x = 65
co2_y = 1
width = 1130
height = 150
width2 = 1150
height2 = 170
color = (0, 0, 0)
color2 = (255, 255, 255)

rec = shapes.Rectangle(co_x, co_y, width, height, color = color, batch = batch)

rec2 = shapes.Rectangle(co2_x, co2_y, width2, height2, color = color2, batch = batch2)

rec.opacity = 255

@win.event
def on_draw():
    bg.blit(0, 0)
    sprite.draw()
    batch2.draw()
    batch.draw()
    label.draw()

pyglet.app.run()
