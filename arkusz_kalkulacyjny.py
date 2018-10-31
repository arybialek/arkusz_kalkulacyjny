import numpy as np

#constant variables
frequency = 2400 #[MHz] 
wave_length = 300/frequency #[m] 

#changeable variables - inputs from user
length = 4 #[km] 
base_height = 75 #[m] 
subscriber_height = 23 #[m] 
medium_height = 13 #[m] 


def p_height_func(base_height, subscriber_height, medium_height):
    p_height = 0.5 * (base_height + subscriber_height) - medium_height
    return p_height

def coefficient_f(p_height, frequency, wave_length):
    coefficient = ((4 * np.power(p_height, 2))/wave_length)
    return int(np.round(coefficient))

def los1(frequency, length, base_height, subscriber_height, medium_height, coefficient):
    result_los1 = ( 23 + 20 * np.log10(frequency) + 16.57 * np.log10(length)
    + (22.1 * np.log10(base_height) - 10.3 * np.log10(subscriber_height) )
    + 8.45 * np.log10(base_height - medium_height) - 5.3 * np.log10(coefficient) )
    return np.round(result_los1, 2) #118.6650244835433

def nlos1(frequency, length, base_height, subscriber_height, medium_height):
    result_nlos1 = ( 108.6 + (20 * np.log10(frequency)) + (21.8 * np.log10(length))
    + ((-35 * np.log10(base_height)) + (16.6 * np.log10(subscriber_height))) 
    - (26.3 * np.log10(base_height - medium_height)) 
    + (23.9 * np.log10( 0.5 * (base_height - subscriber_height) ))  )
    return np.round(result_nlos1, 2) #132.9846320870627

def los2(frequency, length, base_height, subscriber_height, medium_height):
    result_los2 = ( 16.3 + 20 * np.log10(frequency) + 18.1 * np.log10(length) 
    + ( 19.1 * np.log10(base_height) - 6.7 * np.log10(subscriber_height))
    + 12 * np.log10(base_height - medium_height)
    + 0.6 * np.log10(medium_height - subscriber_height)
    - 16.2 * np.log10( 0.5 * (base_height - subscriber_height) )  )
    return np.round(result_los2, 2) #119.98224942273157


def nlos2(frequency, length, base_height, subscriber_height, medium_height):
    result_nlos2 = ( 83.1 + (20 * np.log10(frequency)) + (15.8 * np.log10(length))
    + ( (19.1 * np.log10(base_height)) - (20 * np.log10(subscriber_height)))
    + (47.2 * np.log10(base_height - medium_height))
    + (0.3 * np.log10(medium_height - subscriber_height))
    + (34.4 * np.log10( 0.5 * (base_height - subscriber_height) ) ) )
    return np.round(result_nlos2, 2) #303.04692849058847
