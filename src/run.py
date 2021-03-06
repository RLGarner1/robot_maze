"""Top-level script for letting the robot run."""

import sys
import time

import mount
import robot
import sensor
import state


def go():
	r = robot.Robot()
	m = mount.SwivelMount(driver=r.driver, servo_center=93)
	s = sensor.UltrasonicSensor(driver=r.driver, mount=m)
	cs = state.CorridorState(robot=r)

	r.sensor = s
	r.state = cs

	try:
		print 'Starting in 5 seconds...'
		time.sleep(5)
		r.run()
	except KeyboardInterrupt:
		r.stop()
		sys.exit()


if __name__ == '__main__':
	go()
