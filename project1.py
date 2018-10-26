x = 1000
a = 9429
c = 3967
K = 16384

def random_number_generator():
	x = (a*x + c) % K
	u = x / K
	return u