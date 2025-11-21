#! /usr/bin/python

"""
Dead Reckoning (DR) algorithms for Distributed Interactive Simulation (DIS).

This module implements the standard Dead Reckoning algorithms defined in IEEE 1278.1.
These algorithms are used to extrapolate the position and orientation of an entity
based on its last known state (position, velocity, acceleration, orientation, angular velocity).

The algorithms are categorized by:
1.  Fixed (F) or Rotation (R) - whether orientation is fixed or changing.
2.  Position (P) or Velocity (V) - whether the entity is static or moving.
3.  World (W) or Body (B) - whether the velocity/acceleration vectors are in World or Body coordinates.

Supported Algorithms:
- Static: No movement.
- DRM_FPW: Fixed Position, World.
- DRM_RPW: Rotation, Position, World.
- DRM_RVW: Rotation, Velocity, World.
- DRM_FVW: Fixed Velocity, World.
- DRM_FPB: Fixed Position, Body.
- DRM_RPB: Rotation, Position, Body.
- DRM_RVB: Rotation, Velocity, Body.
- DRM_FVB: Fixed Velocity, Body.

Author: Open-DIS-Python Team
"""

import math
import numpy as np
from typing import Tuple, List

# Constants
EARTH_SEMI_MAJOR_AXIS = 6378137.0  # WGS84
EARTH_SEMI_MINOR_AXIS = 6356752.3142  # WGS84

class DeadReckoning:
    """
    Implements DIS Dead Reckoning algorithms.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_rotation_matrix(psi: float, theta: float, phi: float) -> np.ndarray:
        """
        Calculates the rotation matrix R_wb (Body to World) from Euler angles.
        
        Args:
            psi (float): Yaw (rotation about Z-axis) in radians.
            theta (float): Pitch (rotation about Y-axis) in radians.
            phi (float): Roll (rotation about X-axis) in radians.
            
        Returns:
            np.ndarray: 3x3 Rotation Matrix.
        """
        # Precompute sines and cosines
        c_psi = math.cos(psi)
        s_psi = math.sin(psi)
        c_theta = math.cos(theta)
        s_theta = math.sin(theta)
        c_phi = math.cos(phi)
        s_phi = math.sin(phi)

        # Rotation matrix R = R_z(psi) * R_y(theta) * R_x(phi)
        # Row 1
        r11 = c_psi * c_theta
        r12 = c_psi * s_theta * s_phi - s_psi * c_phi
        r13 = c_psi * s_theta * c_phi + s_psi * s_phi
        
        # Row 2
        r21 = s_psi * c_theta
        r22 = s_psi * s_theta * s_phi + c_psi * c_phi
        r23 = s_psi * s_theta * c_phi - c_psi * s_phi
        
        # Row 3
        r31 = -s_theta
        r32 = c_theta * s_phi
        r33 = c_theta * c_phi

        return np.array([
            [r11, r12, r13],
            [r21, r22, r23],
            [r31, r32, r33]
        ])

    @staticmethod
    def get_angular_velocity_matrix(omega: np.ndarray) -> np.ndarray:
        """
        Creates the skew-symmetric matrix for angular velocity (Omega_x).
        
        Args:
            omega (np.ndarray): Angular velocity vector [wx, wy, wz].
            
        Returns:
            np.ndarray: 3x3 Skew-symmetric matrix.
        """
        return np.array([
            [0, -omega[2], omega[1]],
            [omega[2], 0, -omega[0]],
            [-omega[1], omega[0], 0]
        ])

    @staticmethod
    def drm_static(position: np.ndarray, orientation: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Static Dead Reckoning (No movement).
        
        Args:
            position (np.ndarray): Initial position [x, y, z].
            orientation (np.ndarray): Initial orientation [psi, theta, phi].
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        return position, orientation

    @staticmethod
    def drm_fpw(position: np.ndarray, velocity: np.ndarray, dt: float, orientation: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fixed Position, World (FPW).
        Entity is assumed to be moving at constant velocity (though name suggests fixed position, 
        in DIS FPW often implies simple linear extrapolation if velocity is present, 
        but strictly speaking 'Fixed Position' might mean velocity is ignored. 
        However, standard interpretation usually involves velocity if provided).
        
        Actually, FPW usually means:
        Position = P0 + V0 * dt
        Orientation = Fixed
        
        Args:
            position (np.ndarray): Initial position [x, y, z].
            velocity (np.ndarray): Initial velocity [vx, vy, vz].
            dt (float): Time delta in seconds.
            orientation (np.ndarray): Initial orientation [psi, theta, phi].
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        new_position = position + velocity * dt
        return new_position, orientation

    @staticmethod
    def drm_rpw(position: np.ndarray, velocity: np.ndarray, dt: float, 
                orientation: np.ndarray, angular_velocity: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Rotation, Position, World (RPW).
        Position = P0 + V0 * dt
        Orientation changes based on Angular Velocity.
        
        Args:
            position (np.ndarray): Initial position.
            velocity (np.ndarray): Initial velocity.
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation [psi, theta, phi].
            angular_velocity (np.ndarray): Angular velocity [wx, wy, wz] (Body coordinates usually).
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        # Position extrapolation
        new_position = position + velocity * dt
        
        # Orientation extrapolation
        # For small dt, we can integrate Euler angles directly or use rotation matrices.
        # Using the standard DR matrix update approach:
        # R_new = R_old * exp(Omega_x * dt)
        # But for simplicity and common usage, we often just integrate Euler rates if provided,
        # or transform body rates to Euler rates.
        
        # Here we assume angular_velocity is in Body coordinates (standard for DIS).
        # We need to convert body rates (p, q, r) to Euler rates (d_psi, d_theta, d_phi).
        
        psi, theta, phi = orientation
        p, q, r = angular_velocity
        
        c_phi = math.cos(phi)
        s_phi = math.sin(phi)
        c_theta = math.cos(theta)
        t_theta = math.tan(theta)
        
        # Euler rates transformation
        # d_phi = p + (q * sin(phi) + r * cos(phi)) * tan(theta)
        # d_theta = q * cos(phi) - r * sin(phi)
        # d_psi = (q * sin(phi) + r * cos(phi)) / cos(theta)
        
        # Handle gimbal lock (cos(theta) close to 0)
        if abs(c_theta) < 1e-6:
            d_phi = p
            d_theta = q * c_phi - r * s_phi
            d_psi = 0 # Undefined, keep constant
        else:
            d_phi = p + (q * s_phi + r * c_phi) * t_theta
            d_theta = q * c_phi - r * s_phi
            d_psi = (q * s_phi + r * c_phi) / c_theta
            
        new_orientation = np.array([
            psi + d_psi * dt,
            theta + d_theta * dt,
            phi + d_phi * dt
        ])
        
        return new_position, new_orientation

    @staticmethod
    def drm_rvw(position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray, dt: float,
                orientation: np.ndarray, angular_velocity: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Rotation, Velocity, World (RVW).
        Position = P0 + V0 * dt + 0.5 * A0 * dt^2
        Orientation changes based on Angular Velocity.
        
        Args:
            position (np.ndarray): Initial position.
            velocity (np.ndarray): Initial velocity.
            acceleration (np.ndarray): Initial acceleration.
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            angular_velocity (np.ndarray): Angular velocity.
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        # Position extrapolation with acceleration
        new_position = position + velocity * dt + 0.5 * acceleration * (dt ** 2)
        
        # Orientation extrapolation (Same as RPW)
        _, new_orientation = DeadReckoning.drm_rpw(position, velocity, dt, orientation, angular_velocity)
        
        return new_position, new_orientation

    @staticmethod
    def drm_fvw(position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray, dt: float,
                orientation: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fixed Velocity, World (FVW).
        Position = P0 + V0 * dt + 0.5 * A0 * dt^2
        Orientation = Fixed.
        
        Args:
            position (np.ndarray): Initial position.
            velocity (np.ndarray): Initial velocity.
            acceleration (np.ndarray): Initial acceleration.
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        new_position = position + velocity * dt + 0.5 * acceleration * (dt ** 2)
        return new_position, orientation

    @staticmethod
    def drm_fpb(position: np.ndarray, velocity: np.ndarray, dt: float, 
                orientation: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fixed Position, Body (FPB).
        Velocity is in Body coordinates.
        Position = P0 + R_wb * (Vb * dt)
        Orientation = Fixed.
        
        Args:
            position (np.ndarray): Initial position (World).
            velocity (np.ndarray): Initial velocity (Body).
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        R_wb = DeadReckoning.get_rotation_matrix(*orientation)
        velocity_world = R_wb @ velocity
        
        new_position = position + velocity_world * dt
        return new_position, orientation

    @staticmethod
    def drm_rpb(position: np.ndarray, velocity: np.ndarray, dt: float,
                orientation: np.ndarray, angular_velocity: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Rotation, Position, Body (RPB).
        Velocity is in Body coordinates.
        Orientation changes.
        Position = P0 + R_wb * (Vb * dt) (Simplified, assumes R constant for linear step or small dt)
        NOTE: For high precision with rotating body, one should integrate R(t) * Vb.
        Standard DIS often simplifies this or assumes Vb is rotated by average R or initial R.
        Here we use initial R for the linear step, which is the standard first-order approximation.
        
        Args:
            position (np.ndarray): Initial position (World).
            velocity (np.ndarray): Initial velocity (Body).
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            angular_velocity (np.ndarray): Angular velocity (Body).
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        # Orientation update
        _, new_orientation = DeadReckoning.drm_rpw(position, np.zeros(3), dt, orientation, angular_velocity)
        
        # Position update using initial orientation (First order)
        # Ideally: Integral(R(t) * Vb dt)
        R_wb = DeadReckoning.get_rotation_matrix(*orientation)
        velocity_world = R_wb @ velocity
        new_position = position + velocity_world * dt
        
        return new_position, new_orientation

    @staticmethod
    def drm_rvb(position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray, dt: float,
                orientation: np.ndarray, angular_velocity: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Rotation, Velocity, Body (RVB).
        Velocity and Acceleration in Body coordinates.
        Orientation changes.
        
        Args:
            position (np.ndarray): Initial position (World).
            velocity (np.ndarray): Initial velocity (Body).
            acceleration (np.ndarray): Initial acceleration (Body).
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            angular_velocity (np.ndarray): Angular velocity (Body).
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        # Orientation update
        _, new_orientation = DeadReckoning.drm_rpw(position, np.zeros(3), dt, orientation, angular_velocity)
        
        # Position update
        # P_new = P_old + R * (Vb * dt + 0.5 * Ab * dt^2)
        R_wb = DeadReckoning.get_rotation_matrix(*orientation)
        displacement_body = velocity * dt + 0.5 * acceleration * (dt ** 2)
        displacement_world = R_wb @ displacement_body
        
        new_position = position + displacement_world
        
        return new_position, new_orientation

    @staticmethod
    def drm_fvb(position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray, dt: float,
                orientation: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fixed Velocity, Body (FVB).
        Velocity and Acceleration in Body coordinates.
        Orientation Fixed.
        
        Args:
            position (np.ndarray): Initial position (World).
            velocity (np.ndarray): Initial velocity (Body).
            acceleration (np.ndarray): Initial acceleration (Body).
            dt (float): Time delta.
            orientation (np.ndarray): Initial orientation.
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (New Position, New Orientation).
        """
        R_wb = DeadReckoning.get_rotation_matrix(*orientation)
        displacement_body = velocity * dt + 0.5 * acceleration * (dt ** 2)
        displacement_world = R_wb @ displacement_body
        
        new_position = position + displacement_world
        
        return new_position, orientation
