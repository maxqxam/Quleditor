import pygame as pg
from typing import Literal
import time
from Structures.Window import Window
from Structures.Menu import Menu
from Structures.Pos import Pos
from Structures import Constants as c
from AssetManager import AssetManager
from Editor import Editor
from Structures.Color import Color


color = Color(0,0,0).swap_max('r')




pg.init()
window = Window(Pos(1200,750),Pos(1200,750),"Quleditor",60,c.WINDOW_REAL_SIZE)
editor = Editor(window.get_window_size())


frames = 0
l_time = time.time()
check_fps = 0


while window.is_running:
    events = pg.event.get()
    window.get_events(events)
    editor.get_events(events)

    window.check_events()
    editor.receive_grabbed_files(window.grab_dropped_files())
    editor.check_events()

    editor.render(window.get_window())
    window.render_and_update()

    if check_fps:
        frames += 1
        if frames % 60 == 0:
            t = time.time() - l_time
            print("approximate fps:",round(60 / t),"time",round(t,2))
            l_time = time.time()


