import model
import constants
import math

m - model.Model()

m.m1.speed = 10
m.m2.speed = 10
print ("First model : {}".format(m))

linear_speed, rotational_speed = m.dk()
print("Model : {}".format(m))
if linear_speed == 10 and rotational_speed == 0:
    print ("Test1 OK")
    else: 
        print("Test1 FAILED")


print ("### Setting same speed for both motors")
m.m1.speed = 0.1
m.m2.speed = -0.1
print ("\n###############\n model: {}". format(m))
linear_speed, rotational_speed = m.dk()
print ("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed))

print ("### Setting same speed for both motors")
m.m1.speed = 0.1
m.m2.speed = 0.2
print ("\n###############\n model: {}". format(m))
linear_speed, rotational_speed = m.dk()
print ("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed))

