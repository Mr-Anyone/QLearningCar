import numpy as np
from Car import Car
from Constants import *
from GameUpdate import get_data_from_sensor, check_all_collision
from utils import read_csv

outer_track, inner_track = read_csv() # Constant variable


class Game:
    """
    The game class that will take in a car object
    """
    car = Car(pos=np.array([WINDOWS_WIDTH / 2, BOX_HEIGHT / 2]))
    original_car = Car(pos=np.array([WINDOWS_WIDTH / 2, BOX_HEIGHT / 2]))

    def reset(self):
        """
        Car reset to the original position
        """
        self.car = self.original_car

    def step(self, action):
        """
        Move -> Check for collision -> A list of distances between track -> Reward

        :param action:
        :return:
        """
        if action == ACTION_FRONT:
            self.car.move_front()
        elif action == ACTION_LEFT:
            self.car.turn_left()
        elif action == ACTION_RIGHT:
            self.car.turn_right()

        state = get_data_from_sensor(self.car, "_", inner_track, outer_track, draw=False) # This is in the from (car, windows, inner_track, outer_track, draw)
        done = check_all_collision(self.car, inner_track, outer_track)
        reward = self.get_reward() # Finding a reward function

        return state, reward, done

    def render(self):
        """
        Render the game I guess
        This would only be used for debug
        :return: None
        """
        pass

    def get_reward(self):
        """

        :return: reward
        """
        return "A Place Holder"
