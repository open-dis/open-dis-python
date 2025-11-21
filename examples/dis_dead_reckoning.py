#! /usr/bin/python

"""
Example of using the Dead Reckoning module to extrapolate entity position.

This script simulates receiving an EntityStatePdu with velocity and acceleration,
and then uses the DeadReckoning module to predict the entity's position
over a period of time.
"""

import time
import numpy as np
from opendis.dis7 import EntityStatePdu, Vector3Float, Vector3Double
from opendis.DeadReckoning import DeadReckoning

def run_demo():
    # 1. Create a mock PDU (as if received from the network)
    pdu = EntityStatePdu()
    
    # Initial State (t=0)
    # Position: Origin (0, 0, 0)
    pdu.entityLocation.x = 0.0
    pdu.entityLocation.y = 0.0
    pdu.entityLocation.z = 0.0
    
    # Velocity: 10 m/s in X direction
    pdu.entityLinearVelocity.x = 10.0
    pdu.entityLinearVelocity.y = 0.0
    pdu.entityLinearVelocity.z = 0.0
    
    # Acceleration: 1 m/s^2 in X direction
    pdu.deadReckoningParameters.entityLinearAcceleration.x = 1.0
    pdu.deadReckoningParameters.entityLinearAcceleration.y = 0.0
    pdu.deadReckoningParameters.entityLinearAcceleration.z = 0.0
    
    # Orientation: Facing East (0, 0, 0)
    pdu.entityOrientation.psi = 0.0
    pdu.entityOrientation.theta = 0.0
    pdu.entityOrientation.phi = 0.0
    
    # Angular Velocity: None
    pdu.deadReckoningParameters.entityAngularVelocity.x = 0.0
    pdu.deadReckoningParameters.entityAngularVelocity.y = 0.0
    pdu.deadReckoningParameters.entityAngularVelocity.z = 0.0

    # Extract numpy arrays for the DR function
    initial_pos = np.array([pdu.entityLocation.x, pdu.entityLocation.y, pdu.entityLocation.z])
    velocity = np.array([pdu.entityLinearVelocity.x, pdu.entityLinearVelocity.y, pdu.entityLinearVelocity.z])
    acceleration = np.array([
        pdu.deadReckoningParameters.entityLinearAcceleration.x,
        pdu.deadReckoningParameters.entityLinearAcceleration.y,
        pdu.deadReckoningParameters.entityLinearAcceleration.z
    ])
    orientation = np.array([pdu.entityOrientation.psi, pdu.entityOrientation.theta, pdu.entityOrientation.phi])
    angular_velocity = np.array([
        pdu.deadReckoningParameters.entityAngularVelocity.x,
        pdu.deadReckoningParameters.entityAngularVelocity.y,
        pdu.deadReckoningParameters.entityAngularVelocity.z
    ])

    print("--- Dead Reckoning Demonstration ---")
    print(f"Initial Position: {initial_pos}")
    print(f"Velocity: {velocity} m/s")
    print(f"Acceleration: {acceleration} m/s^2")
    print("Simulating 5 seconds of movement using RVW (Rotation, Velocity, World) algorithm...\n")

    # 2. Simulate extrapolation loop
    start_time = time.time()
    simulation_duration = 5.0 # seconds
    
    # We will simulate 'frames'
    current_sim_time = 0.0
    step = 0.5 # Update every 0.5 seconds
    
    while current_sim_time <= simulation_duration:
        # Calculate new position using RVW algorithm
        # Position = P0 + V0*t + 0.5*A0*t^2
        new_pos, new_ori = DeadReckoning.drm_rvw(
            initial_pos,
            velocity,
            acceleration,
            current_sim_time,
            orientation,
            angular_velocity
        )
        
        print(f"Time: {current_sim_time:.1f}s | Extrapolated Pos: {new_pos}")
        
        current_sim_time += step
        # time.sleep(0.1) # Uncomment to run in real-time

    print("\n--- End of Demonstration ---")
    print("Notice how the X position increases quadratically due to acceleration.")
    print("T=0: 0.0")
    print("T=1: 10*1 + 0.5*1*1^2 = 10.5")
    print("T=2: 10*2 + 0.5*1*2^2 = 22.0")
    print("T=5: 10*5 + 0.5*1*5^2 = 50 + 12.5 = 62.5")

if __name__ == "__main__":
    run_demo()
