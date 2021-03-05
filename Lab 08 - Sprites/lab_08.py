""" Sprite Sample Program """


import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.good_coin_list = None
        self.bad_coin_list = None
        self.player_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin1 = arcade.Sprite("bad_coin.png", SPRITE_SCALING_COIN)

            coin2 = arcade.Sprite("rock.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin1.center_x = random.randrange(SCREEN_WIDTH)
            coin1.center_y = random.randrange(SCREEN_HEIGHT)

            coin2.center_x = random.randrange(SCREEN_WIDTH)
            coin2.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_coin_list.append(coin1)
            self.bad_coin_list.append(coin2)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
    

        self.good_coin_list.draw()
        self.bad_coin_list.draw()
        self.player_list.draw()
    
        output = f"coin count: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.good_coin_list.update()
        self.bad_coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.good_coin_list)

        for coin1 in coins_hit_list:
            coin1.remove_from_sprite_lists()
            self.score += 1

        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.bad_coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.

        for coin2 in coins_hit_list:
            coin2.remove_from_sprite_lists()
            self.score -= 1
        
    

    

def main():
    print('main function running')
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

main()

