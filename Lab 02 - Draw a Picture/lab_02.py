import arcade


#opens window 
arcade.open_window(1000, 800, "self portrait")

#strats render 
arcade.start_render()

#draws cirlce for face 
arcade.draw_circle_filled(500, 400, 400, arcade.csscolor.YELLOW)


#circles needed for eye 1
arcade.draw_circle_filled(666, 600, 100, arcade.csscolor.BLACK)

arcade.draw_circle_filled(666, 600, 75, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(666, 600, 50, arcade.csscolor.BLACK)

arcade.draw_circle_filled(666, 600, 25, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(666, 600, 10, arcade.csscolor.BLACK)




#circles needed for eye 2
arcade.draw_circle_filled(333, 600, 100, arcade.csscolor.BLACK)

arcade.draw_circle_filled(333, 600, 75, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(333, 600, 50, arcade.csscolor.BLACK)

arcade.draw_circle_filled(333, 600, 25, arcade.csscolor.YELLOW)

arcade.draw_circle_filled(333, 600, 10, arcade.csscolor.BLACK)


#rectangle needed for mouth 
arcade.draw_rectangle_filled(500, 300, 500, 50, arcade.csscolor.BLACK)

arcade.finish_render()

arcade.run()