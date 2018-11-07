import matplotlib.pyplot as plt 
import numpy as np
plt.style.use('ggplot')


#constant variables
frequency = 2400 #[MHz] 
wave_length = 300/frequency #[m] 



############################# FUNCTIONS ###############################

def p_height_func(base_height, subscriber_height, medium_height):
    '''
    The function that calculates the value of the parameter h_p 
    needed to determine the value of the coefficient c_F.

    Args: 
        base_height (float)
        subscriber_height (float)
        medium_height (float)

    Returns: 
        p_height (float)

    '''
    p_height = 0.5 * (base_height + subscriber_height) - medium_height
    return p_height


def coefficient_f(p_height, frequency, wave_length):
    '''
    The function that calculates the value of the coefficient c_F 
    needed to determine the value for the LOS2 situation.

    Args: 
        p_height (float)
        frequency (int)
        wave_length (float)

    Returns: 
        coefficient (int)

    '''
    coefficient = ((4 * np.power(p_height, 2))/wave_length)
    return int(np.round(coefficient))


def los1(frequency, length, base_height, subscriber_height, medium_height):
    '''
    The function which calculates the propagation attenuation 
    value for LOS1 situation.

    Args: 
        frequency (int)
        length (float)
        base_height (float)
        subscriber_height (float)
        medium_height (float)

    Returns: 
        result_los1 (float)

    '''
    result_los1 = ( 16.3 + 20 * np.log10(frequency) + 18.1 * np.log10(length) 
    + ( 19.1 * np.log10(base_height) - 6.7 * np.log10(subscriber_height))
    + 12 * np.log10(base_height - medium_height)
    + 0.6 * np.log10(medium_height - subscriber_height)
    - 16.2 * np.log10( 0.5 * (base_height - subscriber_height) )  )
    return np.round(result_los1, 2) 


def nlos1(frequency, length, base_height, subscriber_height, medium_height):
    '''
    The function which calculates the propagation attenuation 
    value for NLOS1 situation.

    Args: 
        frequency (int)
        length (float)
        base_height (float)
        subscriber_height (float)
        medium_height (float)

    Returns: 
        result_nlos1 (float)

    '''
    result_nlos1 = ( 83.1 + (20 * np.log10(frequency)) + (15.8 * np.log10(length))
    + ( (19.1 * np.log10(base_height)) - (20 * np.log10(subscriber_height)))
    - (47.2 * np.log10(base_height - medium_height))
    + (0.3 * np.log10(medium_height - subscriber_height))
    + (34.4 * np.log10( 0.5 * (base_height - subscriber_height) ) ) )
    return np.round(result_nlos1, 2) 


def los2(frequency, length, base_height, subscriber_height, medium_height, coefficient):
    '''
    The function which calculates the propagation attenuation 
    value for LOS2 situation.

    Args: 
        frequency (int)
        length (float)
        base_height (float)
        subscriber_height (float)
        medium_height (float)
        coefficient (int)

    Returns: 
        result_los2 (float)

    '''
    result_los2 = ( 23 + 20 * np.log10(frequency) + 16.57 * np.log10(length)
    + (22.1 * np.log10(base_height) - 10.3 * np.log10(subscriber_height) )
    + 8.45 * np.log10(base_height - medium_height) - 5.3 * np.log10(coefficient) )
    return np.round(result_los2, 2) 


def nlos2(frequency, length, base_height, subscriber_height, medium_height):
    '''
    The function which calculates the propagation attenuation 
    value for NLOS2 situation.

    Args: 
        frequency (int)
        length (float)
        base_height (float)
        subscriber_height (float)
        medium_height (float)

    Returns: 
        result_nlos2 (float)

    '''
    result_nlos2 = ( 108.6 + (20 * np.log10(frequency)) + (21.8 * np.log10(length))
    + ((-35 * np.log10(base_height)) + (16.6 * np.log10(subscriber_height))) 
    - (26.3 * np.log10(base_height - medium_height)) 
    + (23.9 * np.log10( 0.5 * (base_height - subscriber_height) ))  )
    return np.round(result_nlos2, 2) 


########################### PLOTS ###############################

def length_analize():
    '''
    A function that calculates the propagation loss for all situations, 
    and creates plots based on the given data. 

    The parameter related to the distance between antennas has changed.

    '''
    #SUBPLOT1: LOS2, NLOS2
    propagation_loss1 = []
    propagation_loss2 = []

    #SUBPLOT2: LOS1, NLOS1
    propagation_loss3 = []
    propagation_loss4 = []

    length = np.arange(2, 8.1, 0.1)

    for leng in length:
        #SUBPLOT1
        propagation_loss3.append(los1(2400, leng, 32, 7, 13))
        propagation_loss4.append(nlos1(2400, leng, 32, 7, 13))
        #SUBPLOT2
        propagation_loss1.append(los2(2400, leng, 75, 25, 13, coefficient_f(p_height_func(75, 25, 13), 2400, wave_length)))
        propagation_loss2.append(nlos2(2400, leng, 75, 25, 13))

    #SUBPLOT1
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)
    #SUBPLOT2
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #Creates two subplots 
    plt.figure(figsize=(17,6.5))
    plt.suptitle("Wpływ zmiany długości ścieżek łącza radiowego na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)

    plt.subplot(1,2,2)
    plt.plot(length, propagation_loss1,'b-', label = "LOS2")
    plt.plot(length, propagation_loss2,'r--', label = "NLOS2")
    plt.ylim(105, 160)
    plt.xlim(2,8)
    plt.xticks([2, 4, 6, 8])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.legend(loc='best' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Długość ścieżek łącza radiowego [km]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')

    plt.subplot(1,2,1)
    plt.plot(length, propagation_loss3,'y-', label = "LOS1")
    plt.plot(length, propagation_loss4,'g--', label = "NLOS1")
    plt.ylim(105, 160)
    plt.xlim(2,8)
    plt.xticks([2, 4, 6, 8])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Długość ścieżek łącza radiowego [km]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='best' )
    plt.show()

length_analize()


def base_height_analize():
    '''
    A function that calculates the propagation loss for all situations, 
    and creates plots based on the given data. 

    The parameter related to the height of base station antenna has changed.

    '''
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss3 = []
    propagation_loss4 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss1 = []
    propagation_loss2 = []

    base_height = np.arange(30, 120.5, 0.5)
    
    for height in base_height:
        #SUBPLOT1
        propagation_loss3.append(los1(2400, 4, height, 7, 13))
        propagation_loss4.append(nlos1(2400, 4, height, 7, 13))
        #SUBPLOT2
        propagation_loss1.append(los2(2400, 4, height, 25, 13, coefficient_f(p_height_func(height, 25, 13), 2400, wave_length)))
        propagation_loss2.append(nlos2(2400, 4, height, 25, 13))

    #SUBPLOT1
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)
    #SUBPLOT2
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #Creates two subplots 
    plt.figure(figsize=(17,6.5)) 
    plt.suptitle("Wpływ zmiany wysokości anteny stacji bazowej na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)

    plt.subplot(1,2,2)
    plt.plot(base_height, propagation_loss1,'b-', label = "LOS2")
    plt.plot(base_height, propagation_loss2,'r--', label = "NLOS2")
    plt.ylim(105, 160)
    plt.xlim(30,120)
    plt.xticks([30, 60, 90, 120])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160]) 
    plt.legend(loc='best' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji bazowej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')

    plt.subplot(1,2,1)
    plt.plot(base_height, propagation_loss3,'y-', label = "LOS1")
    plt.plot(base_height, propagation_loss4,'g--', label = "NLOS1")
    plt.ylim(105, 160)
    plt.xlim(30,120)
    plt.xticks([30, 60, 90, 120])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])  
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji bazowej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='best' )
    plt.show()    

base_height_analize()


def subscriber_height_analize():
    '''
    A function that calculates the propagation loss for all situations, 
    and creates plots based on the given data. 

    The parameter related to the height of the subscriber antenna has changed.

    '''
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss3 = []
    propagation_loss4 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss1 = []
    propagation_loss2 = []
 
    subscriber_height = np.arange(13, 39.5, 0.5)  

    for height in subscriber_height:
        #SUBPLOT2
        propagation_loss1.append(los2(2400, 4, 75, height, 13, coefficient_f(p_height_func(75, height, 13), 2400, wave_length)))
        propagation_loss2.append(nlos2(2400, 4, 75, height, 13))

    subscriber_height2 = np.arange(4, 12.1, 0.1)

    for height in subscriber_height2:
        #SUBPLOT1
        propagation_loss3.append(los1(2400, 4, 32, height, 13))
        propagation_loss4.append(nlos1(2400, 4, 32, height, 13))

    #SUBPLOT1
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)
    #SUBPLOT2
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #Creates two subplots
    plt.figure(figsize=(17,6.5))
    plt.suptitle("Wpływ zmiany wysokości anteny stacji abonenckiej na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)

    plt.subplot(1,2,2)
    plt.plot(subscriber_height, propagation_loss1,'b-', label = "LOS2")
    plt.plot(subscriber_height, propagation_loss2,'r--', label = "NLOS2")
    plt.ylim(105, 160)
    plt.xlim(13, 39)
    plt.xticks([13, 26, 39])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.legend(loc='best' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji abonenckiej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')

    plt.subplot(1,2,1)
    plt.plot(subscriber_height2, propagation_loss3,'y-', label = "LOS1")
    plt.plot(subscriber_height2, propagation_loss4,'g--', label = "NLOS1")
    plt.ylim(105, 160)
    plt.xlim(4, 12)    
    plt.xticks([4, 8, 12])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji abonenckiej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='best' )
    plt.show()    

subscriber_height_analize()


def medium_height_analize():
    '''
    A function that calculates the propagation loss for all situations, 
    and creates plots based on the given data. 

    The parameter related to the average height of the building has changed.

    '''
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss3 = []
    propagation_loss4 = []
    
    #SUBPLOT2: LOS2, NLOS2
    propagation_loss1 = []
    propagation_loss2 = []

    medium_height = np.arange(11, 15.1, 0.1)
    
    for height in medium_height:
        #SUBPLOT2
        propagation_loss1.append(los2(2400, 4, 75, 25, height, coefficient_f(p_height_func(75, 25, height), 2400, wave_length)))
        propagation_loss2.append(nlos2(2400, 4, 75, 25, height))
        #SUBPLOT1
        propagation_loss3.append(los1(2400, 4, 32, 7, height))
        propagation_loss4.append(nlos1(2400, 4, 32, 7, height))

    #SUBPLOT1
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)
    #SUBPLOT2
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #Creates two subplots
    plt.figure(figsize=(17,6.5)) 
    plt.suptitle("Wpływ zmiany średniej wysokości dachów budynków na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)

    plt.subplot(1,2,2)
    plt.plot(medium_height, propagation_loss1,'b-', label = "LOS2")
    plt.plot(medium_height, propagation_loss2,'r--', label = "NLOS2")
    plt.ylim(105, 160)
    plt.xlim(11,15)
    plt.xticks([11, 12, 13, 14, 15])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.legend(loc='best' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Średnia wysokość dachów budynków [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')

    plt.subplot(1,2,1)
    plt.plot(medium_height, propagation_loss3,'y-', label = "LOS1")
    plt.plot(medium_height, propagation_loss4,'g--', label = "NLOS1")
    plt.ylim(105, 160)
    plt.xlim(11,15)
    plt.xticks([11, 12, 13, 14, 15])
    plt.yticks([110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Średnia wysokość dachów budynków [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='best' )
    plt.show()  

medium_height_analize()  
