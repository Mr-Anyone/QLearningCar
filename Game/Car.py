import numpy as np


class Car():
    def __init__(self, pos):
        # These are the car parameters
        self.pos = np.array(pos)

        self.speed = 10
        self.vel = np.array([0, -self.speed]) # Moving 10 from each side

        self.current_degree = 0
        self.angular_velocity = 8

    def move_front(self):
        """
        Move the car forward and stuff
        :return: None
        """
        self.pos += self.vel

    def move_backward(self):
        """
        Move Backward
        :return: None
        """
        self.pos -= self.vel

    def show_pos(self):
        """
        :return: the position of the car
        """
        return self.pos

    def turn_left(self):
        """
        Turning to the left
        :param degree:
        :return:
        """

        self.current_degree -= self.angular_velocity
        self.vel = np.array([np.cos(self.current_degree * np.pi / 180) * self.speed,
                             np.sin(self.current_degree * np.pi / 180) * self.speed])

    def turn_right(self):
        """
        The math for turning right
        :return:
        """

        self.current_degree += self.angular_velocity
        self.vel = np.array([np.cos(self.current_degree * np.pi / 180) * self.speed,
                             np.sin(self.current_degree * np.pi / 180) * self.speed])


    def change_default_value(self, vel=10, angular_velocity=5):
        """
        Changing the default value of things in the program

        :param vel: The velocity of the car
        :param angular_velocity: The angular velocity of the car
        :return:
        """
        self.vel = vel
        self.angular_velocity = angular_velocity

