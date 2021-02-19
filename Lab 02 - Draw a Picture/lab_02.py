import arcade

arcade.open_window(1000, 800, "self portrait")

arcade.start_render()

arcade.draw_circle_filled(500, 400, 400, arcade.csscolor.YELLOW)



arcade.draw_circle_filled(666, 600, 100, arcade.csscolor.BLACK)

arcade.draw_circle_filled(666, 600, 75, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(666, 600, 50, arcade.csscolor.BLACK)

arcade.draw_circle_filled(666, 600, 25, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(666, 600, 10, arcade.csscolor.BLACK)





arcade.draw_circle_filled(333, 600, 100, arcade.csscolor.BLACK)

arcade.draw_circle_filled(333, 600, 75, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(333, 600, 50, arcade.csscolor.BLACK)

arcade.draw_circle_filled(333, 600, 25, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(333, 600, 10, arcade.csscolor.BLACK)



arcade.draw_rectangle_filled(500, 300, 500, 50, arcade.csscolor.BLACK)

arcade.finish_render()

arcade.run()