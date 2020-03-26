import model

m - model.Model()

print ("Default model: {}". format(m))

print ("### Setting same speed for both motors")
m.m1.speed = 0.1
m.m2.speed = 0.1
print ("\n###############\n model: {}". format(m))
linear_speed, rotational_speed = m.dk()
print ("linear_speed={}\nrotational_speed={}".format(linear_speed, rotational_speed))

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

