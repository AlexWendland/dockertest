"""
Created on Wed Feb 23 2022

The defines a class that can be used to gracefully shutdown all docker
containers when asked.

@authors: Alex
"""
from signal import signal, SIGINT, SIGTERM
from typing import Union
from types import FrameType

class GracefulShutdown:
    """
    This class tracks the signals provided by the container and changes the
    variable exit to True when messages for shutdown are provided.
    """

    exit = False

    def __init__(self):
        """
        When it initialises, it just tracks the two signals.
            SIGINT - the keyboard interupt signal.
            SIGTERM - the daemon interupt signal from docker.
        """
        signal(SIGINT, self.exit_gracefully)
        signal(SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signal_number:int, frame:Union[None,FrameType]):
        """
        Handler for shutdown signals. This just sets the exit variable to True.

        Args:
            signal_number (int): The signal number from the operating system.
            frame (None or FrameType): The frame of the error stack, if it
                exists.
        """
        self.exit = True
