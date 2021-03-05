
import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.1
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
COIN_COUNT = 50


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None
        
        self.good_coin_list = None
        self.score = 0
    

    

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # --- Manually place walls

        # Manually create and position a box at 300, 200
    

        

        # --- Place walls with a list
        coordinate_list = [[400, 250],
                           [470, 250],]
                           

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        ############################################################


        self.good_coin_list = arcade.SpriteList()

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin1 = arcade.Sprite("bad_coin.png", SPRITE_SCALING_COIN)

            coin1.center_x = random.randrange(SCREEN_WIDTH)
            coin1.center_y = random.randrange(SCREEN_HEIGHT)
           
            self.good_coin_list.append(coin1)


    def on_draw(self):
        arcade.start_render()
        self.wall_list.draw()
        self.player_list.draw()
        self.good_coin_list.draw()

        output = f"coin count (lamo try getting to 50): {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        self.physics_engine.update()
        self.good_coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.good_coin_list)

        for coin1 in coins_hit_list:
            coin1.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


main()