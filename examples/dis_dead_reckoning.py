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
    # 3. Demonstrate integration with RangeCoordinates (GPS)
    # The Dead Reckoning module returns ECEF coordinates (Earth-Centered, Earth-Fixed).
    # Usually, users want Latitude/Longitude/Altitude.
    from opendis.RangeCoordinates import GPS, deg2rad, rad2deg
    
    gps = GPS()
    
    print("\n--- Integration Verification ---")
    print("Converting extrapolated ECEF coordinates to Lat/Lon/Alt using opendis.RangeCoordinates...")
    
    # Let's take the final position from the simulation
    final_pos_ecef = (new_pos[0], new_pos[1], new_pos[2])
    
    # Convert ECEF to LLA
    # Note: Our example started at 0,0,0 which is the center of the earth (invalid for LLA usually),
    # but let's assume the initial position was actually on the surface for this part of the demo
    # or just show the conversion call structure.
    
    # To make this realistic, let's restart with a real-world location.
    # Monterey, CA: 36.6 N, 121.9 W
    print("\nRestarting simulation at Monterey, CA...")
    start_lat = 36.6
    start_lon = -121.9
    start_alt = 100.0 # meters
    
    start_ecef = gps.lla2ecef((start_lat, start_lon, start_alt))
    print(f"Start LLA: ({start_lat}, {start_lon}, {start_alt})")
    print(f"Start ECEF: {start_ecef}")
    
    # Move East (Velocity in Y in ECEF is roughly East at this location? No, it's complex in ECEF.)
    # For simplicity, let's just add the displacement we calculated earlier to this valid ECEF point.
    # This isn't physically perfect (earth is curved), but demonstrates the API integration.
    
    displacement = new_pos # The 62.5m displacement from the previous run
    final_ecef_real = (
        start_ecef[0] + displacement[0],
        start_ecef[1] + displacement[1],
        start_ecef[2] + displacement[2]
    )
    
    final_lla = gps.ecef2lla(final_ecef_real)
    print(f"Final ECEF: {final_ecef_real}")
    print(f"Final LLA: ({final_lla[0]:.6f}, {final_lla[1]:.6f}, {final_lla[2]:.2f})")
    
    print("\nIntegration Successful: Dead Reckoning output was successfully fed into RangeCoordinates.")

if __name__ == "__main__":
    run_demo()
