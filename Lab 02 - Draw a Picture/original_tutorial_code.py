import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.AQUAMARINE)

arcade.draw_lrtb_rectangle_filled(0,599, 300, 0, arcade.csscolor.GREEN)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.BLACK)

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.BROWN)

arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.BROWN)

arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.BROWN)



arcade.finish_render()

arcade.run()