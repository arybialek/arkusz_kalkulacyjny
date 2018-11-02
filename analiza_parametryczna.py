import matplotlib.pyplot as plt 
import numpy as np
plt.style.use('ggplot')

#constant variables
frequency = 2400 #[MHz] 
wave_length = 300/frequency #[m] 

#counts hp
def p_height_func(base_height, subscriber_height, medium_height):
    p_height = 0.5 * (base_height + subscriber_height) - medium_height
    return p_height

#counts cF
def coefficient_f(p_height, frequency, wave_length):
    coefficient = ((4 * np.power(p_height, 2))/wave_length)
    return int(np.round(coefficient))

#LOS1
def los1(frequency, length, base_height, subscriber_height, medium_height, coefficient):
    result_los1 = ( 23 + 20 * np.log10(frequency) + 16.57 * np.log10(length)
    + (22.1 * np.log10(base_height) - 10.3 * np.log10(subscriber_height) )
    + 8.45 * np.log10(base_height - medium_height) - 5.3 * np.log10(coefficient) )
    return np.round(result_los1, 2) #118.6650244835433

#NLOS1
def nlos1(frequency, length, base_height, subscriber_height, medium_height):
    result_nlos1 = ( 108.6 + (20 * np.log10(frequency)) + (21.8 * np.log10(length))
    + ((-35 * np.log10(base_height)) + (16.6 * np.log10(subscriber_height))) 
    - (26.3 * np.log10(base_height - medium_height)) 
    + (23.9 * np.log10( 0.5 * (base_height - subscriber_height) ))  )
    return np.round(result_nlos1, 2) #132.9846320870627

#LOS2
def los2(frequency, length, base_height, subscriber_height, medium_height):
    result_los2 = ( 16.3 + 20 * np.log10(frequency) + 18.1 * np.log10(length) 
    + ( 19.1 * np.log10(base_height) - 6.7 * np.log10(subscriber_height))
    + 12 * np.log10(base_height - medium_height)
    + 0.6 * np.log10(medium_height - subscriber_height)
    - 16.2 * np.log10( 0.5 * (base_height - subscriber_height) )  )
    return np.round(result_los2, 2) #119.98224942273157

#NLOS2
def nlos2(frequency, length, base_height, subscriber_height, medium_height):
    result_nlos2 = ( 83.1 + (20 * np.log10(frequency)) + (15.8 * np.log10(length))
    + ( (19.1 * np.log10(base_height)) - (20 * np.log10(subscriber_height)))
    + (47.2 * np.log10(base_height - medium_height)) # a może minus?
    + (0.3 * np.log10(medium_height - subscriber_height))
    + (34.4 * np.log10( 0.5 * (base_height - subscriber_height) ) ) )
    return np.round(result_nlos2, 2) #303.04692849058847
#########################################################################################################################################################
def length_analize():
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss1 = []
    propagation_loss2 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss3 = []
    propagation_loss4 = []

    #common for all subplots
    length = np.arange(2, 8.1, 0.1)

    for leng in length:
        #SUBPLOT1
        propagation_loss1.append(los1(2400, leng, 75, 25, 13, coefficient_f(p_height_func(75, 25, 13), 2400, wave_length)))
        propagation_loss2.append(nlos1(2400, leng, 75, 25, 13))

        #SUBPLOT2
        propagation_loss3.append(los2(2400, leng, 32, 7, 13))
        propagation_loss4.append(nlos2(2400, leng, 32, 7, 13))


    #SUBPLOT1
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #SUBPLOT2
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)


    #Creates two subplots and unpacks the output array immediately
    plt.figure(figsize=(13,6)) #tworzy nowe okienko
    plt.suptitle("Wpływ zmiany długości ścieżek łącza radiowego na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)
    plt.subplot(1,2,1)
    plt.plot(length, propagation_loss1,'b-', label = "LOS1")
    plt.plot(length, propagation_loss2,'r-', label = "NLOS1")
    plt.ylim(100, 280)
    plt.xlim(2,8)
    plt.xticks([2, 4, 6, 8])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.legend(loc='center right' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Długość ścieżek łącza radiowego [km]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')


    plt.subplot(1,2,2)
    plt.plot(length, propagation_loss3,'y-', label = "LOS2")
    plt.plot(length, propagation_loss4,'g-', label = "NLOS2")
    plt.ylim(100, 280)
    plt.xlim(2,8)
    plt.xticks([2, 4, 6, 8])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Długość ścieżek łącza radiowego [km]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='center right' )
    plt.show()
length_analize()

#######################################################################################################################################################
def base_height_analize():
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss1 = []
    propagation_loss2 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss3 = []
    propagation_loss4 = []

    base_height = np.arange(30, 120.5, 0.5)
    
    for height in base_height:
        #SUBPLOT1
        propagation_loss1.append(los1(2400, 4, height, 25, 13, coefficient_f(p_height_func(height, 25, 13), 2400, wave_length)))
        propagation_loss2.append(nlos1(2400, 4, height, 25, 13))

        #SUBPLOT2
        propagation_loss3.append(los2(2400, 4, height, 7, 13))
        propagation_loss4.append(nlos2(2400, 4, height, 7, 13))

    #SUBPLOT1
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #SUBPLOT2
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)


    #Creates two subplots and unpacks the output array immediately
    plt.figure(figsize=(13,6)) #tworzy nowe okienko
    plt.suptitle("Wpływ zmiany wysokości anteny stacji bazowej na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)
    plt.subplot(1,2,1)
    plt.plot(base_height, propagation_loss1,'b-', label = "LOS1")
    plt.plot(base_height, propagation_loss2,'r-', label = "NLOS1")
    plt.ylim(100, 340)
    plt.xlim(30,120)
    plt.xticks([30, 60, 90, 120])
    plt.yticks([110, 120, 130, 140, 260, 280, 300, 320, 340])    
    plt.legend(loc='center right' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji bazowej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')


    plt.subplot(1,2,2)
    plt.plot(base_height, propagation_loss3,'y-', label = "LOS2")
    plt.plot(base_height, propagation_loss4,'g-', label = "NLOS2")
    plt.ylim(100, 340)
    plt.xlim(30,120)
    plt.xticks([30, 60, 90, 120])
    plt.yticks([110, 120, 130, 140, 260, 280, 300, 320, 340])    
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji bazowej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='center right' )
    plt.show()    

base_height_analize()

#######################################################################################################################################################
def subscriber_height_analize():
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss1 = []
    propagation_loss2 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss3 = []
    propagation_loss4 = []
 
    subscriber_height = np.arange(13, 39.5, 0.5)  

    for height in subscriber_height:
        #SUBPLOT1
        propagation_loss1.append(los1(2400, 4, 75, height, 13, coefficient_f(p_height_func(75, height, 13), 2400, wave_length)))
        propagation_loss2.append(nlos1(2400, 4, 75, height, 13))

    subscriber_height2 = np.arange(3, 12.1, 0.1)
    for height in subscriber_height2:
        #SUBPLOT2
        propagation_loss3.append(los2(2400, 4, 32, height, 13))
        propagation_loss4.append(nlos2(2400, 4, 32, height, 13))

    #SUBPLOT1
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #SUBPLOT2
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)


    #Creates two subplots and unpacks the output array immediately
    plt.figure(figsize=(13,6))
    plt.suptitle("Wpływ zmiany wysokości anteny stacji abonenckiej na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)
    plt.subplot(1,2,1)
    plt.plot(subscriber_height, propagation_loss1,'b-', label = "LOS1")
    plt.plot(subscriber_height, propagation_loss2,'r-', label = "NLOS1")
    plt.ylim(100, 280)
    plt.xlim(13, 39)
    plt.xticks([13, 26, 39])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.legend(loc='center right' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji abonenckiej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')


    plt.subplot(1,2,2)
    plt.plot(subscriber_height2, propagation_loss3,'y-', label = "LOS2")
    plt.plot(subscriber_height2, propagation_loss4,'g-', label = "NLOS2")
    plt.ylim(100, 280)
    plt.xlim(3, 12)    
    plt.xticks([3, 6, 9, 12])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Wysokość anteny stacji abonenckiej [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='center right' )
    plt.show()    

subscriber_height_analize()

#######################################################################################################################################################
def medium_height_analize():
    #SUBPLOT1: LOS1, NLOS1
    propagation_loss1 = []
    propagation_loss2 = []

    #SUBPLOT2: LOS2, NLOS2
    propagation_loss3 = []
    propagation_loss4 = []

    medium_height = np.arange(11, 15.1, 0.1)
    
    for height in medium_height:
        #SUBPLOT1
        propagation_loss1.append(los1(2400, 4, 75, 25, height, coefficient_f(p_height_func(75, 25, height), 2400, wave_length)))
        propagation_loss2.append(nlos1(2400, 4, 75, 25, height))

        #SUBPLOT2
        propagation_loss3.append(los2(2400, 4, 32, 7, height))
        propagation_loss4.append(nlos2(2400, 4, 32, 7, height))

    #SUBPLOT1
    propagation_loss1 = np.asarray(propagation_loss1)
    propagation_loss2 = np.asarray(propagation_loss2)

    #SUBPLOT2
    propagation_loss3 = np.asarray(propagation_loss3)
    propagation_loss4 = np.asarray(propagation_loss4)


    #Creates two subplots and unpacks the output array immediately
    plt.figure(figsize=(13,6)) #tworzy nowe okienko
    plt.suptitle("Wpływ zmiany średniej wysokości dachów budynków na straty propagacyjne", style = 'oblique', fontweight='bold')
    plt.subplots_adjust(wspace = 0.4)
    plt.subplot(1,2,1)
    plt.plot(medium_height, propagation_loss1,'b-', label = "LOS1")
    plt.plot(medium_height, propagation_loss2,'r-', label = "NLOS1")
    plt.ylim(100, 280)
    plt.xlim(11,15)
    plt.xticks([11, 12, 13, 14, 15])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.legend(loc='center right' )
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Średnia wysokość dachów budynków [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')


    plt.subplot(1,2,2)
    plt.plot(medium_height, propagation_loss3,'y-', label = "LOS2")
    plt.plot(medium_height, propagation_loss4,'g-', label = "NLOS2")
    plt.ylim(100, 280)
    plt.xlim(11,15)
    plt.xticks([11, 12, 13, 14, 15])
    plt.yticks([110, 120, 130, 140, 260, 270, 280])
    plt.ylabel('Straty propagacyjne [dB]', horizontalalignment='center', size = 'smaller', fontweight='bold')
    plt.xlabel('Średnia wysokość dachów budynków [m]', horizontalalignment='center', x=0.5, size = 'smaller', fontweight='bold')
    plt.legend(loc='center right' )
    plt.show()  

medium_height_analize()  
