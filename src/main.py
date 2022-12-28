import pygame as pg

import time
from Structures.Window import Window
from Structures.Menu import Menu
from Structures.Pos import Pos
from Structures import Constants as c
from Editor import Editor

print("\n")


pg.init()
window = Window(Pos(1200,750),Pos(1200,750),"Quleditor",60,c.WINDOW_REAL_SIZE)

editor = Editor(window.get_window_size())

frames = 0
l_time = time.time()
check_fps = False

while window.is_running:
    events = pg.event.get()
    window.get_events(events)
    editor.get_events(event_list=events,mouse_pos=window.get_mouse_pos())

    editor.last_dropped_files = window.grab_dropped_files()

    window.check_events()
    editor.check_events()

    editor.render(window.get_window())
    window.render_and_update()

    if check_fps:
        frames += 1
        if frames % 60 == 0:
            t = time.time() - l_time

            print("approximate fps:",round(60 / t))

            l_time = time.time()


