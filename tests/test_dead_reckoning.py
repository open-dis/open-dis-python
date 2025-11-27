import unittest
import numpy as np
import math
from opendis import DeadReckoning

class TestDeadReckoning(unittest.TestCase):

    def setUp(self):
        # self.dr = DeadReckoning() # Removed class
        self.zero_pos = np.array([0.0, 0.0, 0.0])
        self.zero_vel = np.array([0.0, 0.0, 0.0])
        self.zero_acc = np.array([0.0, 0.0, 0.0])
        self.zero_ori = np.array([0.0, 0.0, 0.0]) # psi, theta, phi
        self.zero_ang_vel = np.array([0.0, 0.0, 0.0])

    def test_static(self):
        pos, ori = DeadReckoning.drm_static(self.zero_pos, self.zero_ori)
        np.testing.assert_array_equal(pos, self.zero_pos)
        np.testing.assert_array_equal(ori, self.zero_ori)

    def test_fpw(self):
        # Move 10m/s in X for 1 second
        vel = np.array([10.0, 0.0, 0.0])
        dt = 1.0
        pos, ori = DeadReckoning.drm_fpw(self.zero_pos, vel, dt, self.zero_ori)
        
        expected_pos = np.array([10.0, 0.0, 0.0])
        np.testing.assert_array_equal(pos, expected_pos)
        np.testing.assert_array_equal(ori, self.zero_ori)

    def test_rpw_rotation(self):
        # Rotate 90 deg/s around Z (Yaw) for 1 second
        # Angular velocity in body coords. If aligned with world, Z body = Z world.
        ang_vel = np.array([0.0, 0.0, math.pi/2]) # [p, q, r] -> [roll_rate, pitch_rate, yaw_rate]
        # Wait, standard mapping: p=roll(x), q=pitch(y), r=yaw(z)
        # My implementation: psi(z), theta(y), phi(x)
        # r corresponds to d_psi (roughly)
        
        dt = 1.0
        pos, ori = DeadReckoning.drm_rpw(self.zero_pos, self.zero_vel, dt, self.zero_ori, ang_vel)
        
        # Expected: Yaw (psi) increases by pi/2
        expected_ori = np.array([math.pi/2, 0.0, 0.0])
        
        np.testing.assert_array_almost_equal(pos, self.zero_pos)
        np.testing.assert_array_almost_equal(ori, expected_ori)

    def test_rvw_acceleration(self):
        # Accelerate 1m/s^2 in X for 2 seconds
        acc = np.array([1.0, 0.0, 0.0])
        dt = 2.0
        pos, ori = DeadReckoning.drm_rvw(self.zero_pos, self.zero_vel, acc, dt, self.zero_ori, self.zero_ang_vel)
        
        # d = 0.5 * a * t^2 = 0.5 * 1 * 4 = 2.0
        expected_pos = np.array([2.0, 0.0, 0.0])
        
        np.testing.assert_array_almost_equal(pos, expected_pos)

    def test_fpb_aligned(self):
        # Body aligned with World. Velocity in Body X should be Velocity in World X.
        vel_body = np.array([10.0, 0.0, 0.0])
        dt = 1.0
        pos, ori = DeadReckoning.drm_fpb(self.zero_pos, vel_body, dt, self.zero_ori)
        
        expected_pos = np.array([10.0, 0.0, 0.0])
        np.testing.assert_array_almost_equal(pos, expected_pos)

    def test_fpb_rotated(self):
        # Body rotated 90 deg around Z (Yaw).
        # Body X is now World Y.
        # Velocity in Body X should result in movement in World Y.
        ori = np.array([math.pi/2, 0.0, 0.0]) # 90 deg yaw
        vel_body = np.array([10.0, 0.0, 0.0])
        dt = 1.0
        
        pos, new_ori = DeadReckoning.drm_fpb(self.zero_pos, vel_body, dt, ori)
        
        expected_pos = np.array([0.0, 10.0, 0.0]) # Moved in Y
        
        np.testing.assert_array_almost_equal(pos, expected_pos)
        np.testing.assert_array_almost_equal(new_ori, ori)

    def test_input_flexibility(self):
        # Test passing lists instead of numpy arrays
        pos_list = [0.0, 0.0, 0.0]
        vel_list = [10.0, 0.0, 0.0]
        ori_list = [0.0, 0.0, 0.0]
        dt = 1.0
        
        pos, ori = DeadReckoning.drm_fpw(pos_list, vel_list, dt, ori_list)
        
        expected_pos = np.array([10.0, 0.0, 0.0])
        np.testing.assert_array_equal(pos, expected_pos)

if __name__ == '__main__':
    unittest.main()
