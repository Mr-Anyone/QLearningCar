import numpy as np
from Constants import *
from utils import rotation

class Car():
    def __init__(self, pos):
        # These are the car parameters
        self.pos = np.array(pos)

        self.speed = 10
        self.vel = np.array([self.speed, 0])  # Moving 10 from each side

        self.current_degree = 0
        self.angular_velocity = 8

        self.line_degree = [0, 45, 90, 135, 180, 225, 270,315]  # The sensor angle for distance 45, 90, 135, 180, 225, 270 ,315
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

    def get_four_side(self):
        """
        The Math Calculation that find the 4 points of the car
        :return: the 4 points of the car
        """
        top_right = self.pos + rotation(self.current_degree, np.array([BOX_WIDTH/2, -BOX_HEIGHT/2]))
        top_left = self.pos + rotation(self.current_degree, np.array([-BOX_WIDTH / 2, -BOX_HEIGHT / 2]))
        bottom_right = self.pos + rotation(self.current_degree, np.array([BOX_WIDTH / 2, BOX_HEIGHT / 2]))
        bottom_left = self.pos + rotation(self.current_degree, np.array([-BOX_WIDTH / 2, BOX_HEIGHT / 2]))
        return [top_right, top_left, bottom_right, bottom_left]

    def center_point(self):
        return self.pos[0], self.pos[1]

    def sensor_line(self):
        """
        Sensor line is a line that that car sees (a line to check for intersection)

        8 Line in different degree from the center point [0, 45, 90, 135, 180, 225, 270 ,315]
        :return: A line for checking intersection
        """
        reference_line = np.array([self.pos[0] + 1000, self.pos[1]])  # The reference has to be long to prevent no line from intersecting
        line_points = []
        for angle in self.line_degree:
            line_points.append([self.pos, rotation(angle+self.current_degree, reference_line)])
        return line_points
