	

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
A = 50
B = 50 





def snowman (x, y):
     # Snow
    arcade.draw_circle_filled(300+x, 200+y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300+x, 280+y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300+x, 340+y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285+x, 350+y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315+x, 350+y, 5, arcade.color.BLACK)
    



def on_draw(delta_time):
    global A
    global B

    arcade.start_render()
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    
    A = A + 1
    B = B + 2
    snowman(A, B)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    
      
 
    arcade.schedule(on_draw, 1/60)
    
    arcade.run()
   



main()
