import obd

connection = obd.OBD(fast=False, timeout=30)

speed = obd.commands.SPEED
res_speed = connection.query(speed)
print("speed", res_speed.value)

rpm = obd.commands.RPM
res_rpm = connection.query(rpm)
print("rpm", res_rpm.value)

troubles = obd.commands.GET_DTC
res_troubles = connection.query(troubles)
print("troubles", res_troubles)

throttle = obd.commands.THROTTLE_POS
res_throttle = connection.query(throttle)
print("throttle", throttle.value)
