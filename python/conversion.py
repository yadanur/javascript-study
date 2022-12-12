def temp_conversion(celsius):
	fahrenheit=celsius*9/5 +32
	kelvin=celsius + 273.15
	
	return(fahrenheit,kelvin)

print(temp_conversion(30))