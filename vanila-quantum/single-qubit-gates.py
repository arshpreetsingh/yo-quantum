import math

import numpy as np

# pauli-Gate
pauli_x = np.array([[0,1],[1,0]])
pauli_y = np.array([0,-1j],[1j,0])
pauli_z = np.array([[1,0],[0,-1]])

# Hadamard Gate!
hadamard_gate = 1/np.sqrt(2)*np.array([[1,1],[1,-1]])

# S-gate (phase-gate)
s_gate = np.array([[1,0],[0,1j]])

# T-Gate representation
t_gate = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
theta = 90
lamda = 2
psi = 1

# U1, U2 and U3 Gates
def get_U3(theta,lamda,psi):
    U3 = np.array([[math.cos(theta/2), -np.exp(1j * lamda) * math.sin(theta/2)],
                   [np.exp(1j * psi) * math.sin(theta/2), np.exp(1j * (psi + lamda)) * math.cos(theta/2)]])
    return U3

# U2 is special case of U3 when Theta=pi/2
def get_U2(theta=math.pi/2, lamda=None, psi=None):
    U3 = np.array([[math.cos(theta/2), -np.exp(1j * lamda) * math.sin(theta/2)],
                   [np.exp(1j * psi) * math.sin(theta/2), np.exp(1j * (psi + lamda)) * math.cos(theta/2)]])
    return U3

# U1 is special case of U3 when Theta=0 , psi = 0
def get_U2(theta=0, lamda=None, psi=0):
    U3 = np.array([[math.cos(theta/2), -np.exp(1j * lamda) * math.sin(theta/2)],
                   [np.exp(1j * psi) * math.sin(theta/2), np.exp(1j * (psi + lamda)) * math.cos(theta/2)]])
    return U3


def rotate_X(theta):
    rotation_X = np.array([[math.cos(theta/2),-1j*math.sin(theta/2)],[-1j*math.sin(theta/2),math.cos(theta/2)]])
    return rotation_X

def rotate_Y(theta):
    rotation_Y = np.array([[math.cos(theta/2),-1*math.sin(theta/2)],[math.sin(theta/2),math.cos(theta/2)]])
    return rotation_Y

def rotate_Z(theta):
    rotation_Z = np.array([[np.exp(-1j*theta/2),0],[0,np.exp(1j*theta/2)]])
    return rotation_Z