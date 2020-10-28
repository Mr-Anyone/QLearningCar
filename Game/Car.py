import numpy as np


class Car():
    def __init__(self, pos):
        # These are the car parameters
        self.pos = np.array(pos)

        self.vel = 10
        self.current_degree = 0
        self.angular_velocity = 5

    def move_front(self):
        """
        :return: Move the car forward and stuff
        """
        self.pos += self.vel

    def show_pos(self):
        """
        :return: the position of the car
        """
        return self.pos

    def trun_left(self):
        """
        Turning to the left
        :param degree:
        :return:
        """

        self.current_degree += self.vel
        self.pos = np.array([(np.cos(self.current_degree) * self.angular_velocity) + self.pos[0],
                             (np.sin(self.current_degree) * self.angular_velocity) + self.pos[1]])

    def change_default_value(self, vel=10, angular_velocity=5):
        """
        Changing the default value of things in the program

        :param vel: The velocity of the car
        :param angular_velocity: The angular velocity of the car
        :return:
        """
        self.vel = vel
        self.angular = angular_velocity

    def get_current_degree(self):
        return self.current_degree
