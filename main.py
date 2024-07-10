import dearpygui.dearpygui as dpg
from getsysinfo import getSystemInfo
from cmdhandler import *

width = 800
height = 500

dpg.create_context()
dpg.create_viewport(title="GERAHN", width=width, height=height)
dpg.setup_dearpygui()

font = "fonts/font.ttf"

with dpg.font_registry():
    default_font = dpg.add_font(file=font, size=30)
    custom_font = dpg.add_font(file=font, size=80)
    main_menu_b_f = dpg.add_font(file=font, size=35)
    system_menu_header_f = dpg.add_font(file=font, size=60)


path = ["main_menu"]



# Callbacks

#path = ["main_menu", "system_menu"]

# def askpass():
#     dpg.configure_item("color", show=True)
#     subprocess.run('pkexec')
#     dpg.configure_item("color", show=False)

def back():
    dpg.configure_item(path[-1], show=False)
    print("Show false: " + path[-1])
    dpg.configure_item( path[-1-1] , show=True)
    print("Show true: " + path[-1-1])
    dpg.set_primary_window( path[-1-1] , True)
    path.pop()
    print(path)

def open_system_window():
    dpg.configure_item("main_menu", show=False)
    dpg.configure_item("system_menu", show=True)
    dpg.set_primary_window("system_menu", True)
    to("main_menu", "system_menu", 1)
    # askpass()

def open_check_sysinfo_window():
    dpg.configure_item("system_menu", show=False)
    dpg.configure_item("sysinfo_menu", show=True)
    dpg.set_primary_window("sysinfo_menu", True)
    to("system_menu", "sysinfo_menu", 2)

def to(frm, to:str, qur:int):
    path.append(1)
    path[qur] = to
    print(path)


tab = 0
with dpg.window(tag="color", show=False):
    pass

with dpg.window(tag="sysinfo_menu", show=False):
    with dpg.group(horizontal=True):

        back_button = dpg.add_button(
            callback=back,
            label = "<<<",
            pos=[10,10],
            width=70,
            height=40
        )

        for key, value in getSystemInfo().items():
            tab += 27
            info = dpg.add_text(
                default_value=(f"{key} >>> {value}"),
                pos=[20, 30 + tab]
            )

with dpg.window(tag="system_menu", show=False):
    with dpg.group(horizontal=True):
        title = dpg.add_text(
            default_value="System operations", 
            pos=[width // 2 - 220, height // 2 - 230]
            )
        dpg.bind_item_font(title, system_menu_header_f)
        
        back_button = dpg.add_button(
            callback=back,
            label = "<<<",
            pos=[10,10],
            width=70,
            height=40
        )

        update_button = dpg.add_button( # Install Updates
            callback=upgrade_cmd,
            label = "Install Updates",
            pos=[width // 4 - 80, height // 2 - 150],
            width=280, height=50
        )
        del_packets_button = dpg.add_button( # Install Updates
            callback=del_packets_cmd,
            label = "Del unnecessary pcks",
            pos=[width // 4 - 80, height // 2 - 90],
            width=280, height=50
        )

        info_button = dpg.add_button( # Install Updates
            callback=open_check_sysinfo_window,
            label = "Check info",
            pos=[width // 2 + 20, height // 2 - 150],
            width=280, height=50
        )

        dpg.bind_item_font(update_button, main_menu_b_f)
        dpg.bind_item_font(info_button, main_menu_b_f)

with dpg.window(tag="main_menu", min_size=[width, height]):
    with dpg.group(horizontal=True):
        title = dpg.add_text(
            default_value="GERAHb", 
            pos=[width // 2 - 110, height // 2 - 150]
            )
        dpg.bind_item_font(title, custom_font)

        func_button = dpg.add_button( # SYSTEM
            callback=open_system_window,
            label = "System",
            pos=[width // 4 - 45, height // 2 - 60],
            width=230, height=50
        )

        git_button = dpg.add_button( # GITMENU
            label = "GitMenu",
            pos=[width // 2, height // 2 - 60],
            width=230, height=50
        )

        settings_button = dpg.add_button(
            label = "Settings",
            pos=[width // 2, height // 2],
            width=230, height=50
        )

        dpg.bind_item_font(func_button, main_menu_b_f)
        dpg.bind_item_font(git_button, main_menu_b_f)
        dpg.bind_item_font(settings_button, main_menu_b_f)


# dpg.set_viewport_max_height(height)
# dpg.set_viewport_max_width(width)
dpg.set_viewport_min_height(height)
dpg.set_viewport_min_width(width)

dpg.bind_font(default_font)
dpg.set_primary_window("main_menu", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()