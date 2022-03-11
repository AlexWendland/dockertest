"""
Created on Fri Mar 11 2022

Useless python file to test git actions and hopefully kubernetes.

@authors: Alex
"""
from utility import GracefulShutdown
from time import sleep

if __name__ == '__main__':

    graceful_shutdown = GracefulShutdown()

    while not graceful_shutdown.exit:
        print("I'm a kickin'.")
        sleep(1)

    print("Stopped like a graceful bird.")