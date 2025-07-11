import dearpygui.dearpygui as dpg
#,,decorated=False
dpg.create_context()
#dpg.create_viewport(title='Custom Title1111', width=600, height=300)

#

def resize_viewport():
    #print(dpg.get_item_rect_size("Window"))
    width = dpg.get_viewport_width()
    height = dpg.get_viewport_height()
    #dpg.set_item_height("Window", size)
    dpg.set_item_width("Window", width)
    dpg.set_item_height("Window", height)
    # if dpg.does_alias_exist:
    #     dpg.delete_item("drawlist", children_only=True)
    # dpg.draw_image("image_id", (0, 0), (size, size), uv_min=(0, 0), uv_max=(1, 1), parent="drawlist")

# with dpg.item_handler_registry(tag="window_handler"):
#     dpg.add_item_resize_handler(callback=resize_viewport)

with dpg.window(tag="Window",label="Example Window",no_close=True,no_resize=True,no_move=True,no_collapse=True):
    # with dpg.add_table():
    #     dpg.add_table_column()
    
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")    
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    with dpg.child():
        dpg.add_text("Hello, world")
    with dpg.tab_bar():
        dpg.add_text("Hello, world1")
    
#dpg.bind_item_handler_registry("Window", "window_handler")
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.set_viewport_resize_callback(resize_viewport)
resize_viewport()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()