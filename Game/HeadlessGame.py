from Car import Car
from Constants import *
import numpy as np

class Game:
    """
    The game class that will take in a car object
    """
    car = Car(pos=np.array([WINDOWS_WIDTH/2, BOX_HEIGHT/2]))
    original_car = Car(pos=np.array([WINDOWS_WIDTH/2, BOX_HEIGHT/2]))

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
        pass
