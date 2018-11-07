import numpy as np
import os 
#have to do: os.system('clear')


#constant variables
frequency = 2400 #[MHz] 
wave_length = 300/frequency #[m] 



##################### FUNCTIONS ########################

def usr_input():
    '''
    Function that takes data from the user.

    Returns: 
        length (float)
        base_height (float)
        subscriber_height (float)
        medium_height (float)
    '''
    while True:
        try:
            length = float(input("Podaj odległość między antenami, wyrażoną w metrach, w granicach między 0.2km a 8.31km: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")            
            continue
        else:
            if 0.2 <= length <= 8.31:
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')

    while True:
        try:
            base_height = float(input("Podaj wysokość zawieszenia anteny nadawczej, wyrażoną w metrach, w granicach między 30m a 120m: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if 30 <= base_height <= 120:
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')

    while True:
        try:
            subscriber_height = float(input("Podaj wysokość anteny odbiorczej, wyrażoną w metrach, w granicach między 3m a 48m: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if 3 <= subscriber_height <= 48:
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')   

    while True:    
        try:
            medium_height = float(input("Podaj średnią wysokość dachów budynków, wyrażoną w metrach, w granicach między 10.9m a 15.1m: "))      
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if 10.9 <= medium_height <= 15.1: 
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')        
            
    return length, base_height, subscriber_height, medium_height


def check_if_los():
    '''
    Function which asks if there is an obstacle
    on the propagation path. 

    Returns: 
        is_los_condition (str): if "yes" then there is an obstacle,
                                if "nie" then the condition of LOS 
                                is fulfilled.
    '''
    while True:    
        try:
            is_los_condition = str(input("Czy na drodze propagacji fali znajdują się przeszkody? Odpowiedz tak/nie: "))      
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if is_los_condition == 'tak' or is_los_condition == 'nie':
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.') 
    return is_los_condition


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



#################### MAIN PROGRAM ######################

loop = True
while(loop):
    
    print("\n-------------- KALKULATOR WYZNACZAJĄCY STRATY PROPAGACYJNE DLA MODELU KIEDROWSKIEGO-KATULSKIEGO ------------")
    print("----------- Wykonany na potrzeby kursu Media Transmisyjne 2 projekt. Autor: Anita Rybiałek 235133. -----------\n")
    print("\nZasada działania programu: ")
    print("Program pobiera od użytkownika wartości niezbędne do określenia jednego z 4 charakterystycznych przypadków modelu: ")
    print("LOS1, NLOS1, LOS2, NLOS2, następnie wylicza straty propagacyjne dla konkretnego modelu." +  
    " Częstotliwość sygnału jest stała i wynosi 2400[MHz]\n")

    print("\nMenu programu. Wybierz, co chcesz zrobić. \n" +
    "[ 1 ] Obliczyć straty propagacyjne dla określonego modelu. \n" +
    "[ 2 ] Nie wiem jaki konkretnie model użyć. Chcę podać jedynie wartości.\n"+    
    "[ 3 ] Zakończyć program.\n")
    
    try: 
        ans = int(input("Twój wybór: "))
        if ans == 1:
            on = True
            while (on):
                choose = str(input("\nWybrano opcję obliczenia strat propagacyjnych dla określonego modelu.\n" +
                "Wybierz model dla, którego chcesz obliczyć straty: \n" + " a) LOS1 \n b) NLOS1 \n c) LOS2 \n d) NLOS2 \n e) Powrót do głownego menu \nTwój wybór: "))
                if choose in ('c', 'C'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} [km]\nwysokość stacji nadawczej: {1} [m]\nwysokość stacji odbiorczej: {2} [m]\nśrednia wysokość dachów budynków: {3} [m]\nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku LOS2 straty propacyacyjne wynoszą: {0} [dB]".format(los2(2400, length, base_height, subscriber_height, medium_height, coefficient_f(p_height_func(base_height, subscriber_height, medium_height), 2400, wave_length))))

                elif choose in ('d', 'D'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} [km]\nwysokość stacji nadawczej: {1} [m]\nwysokość stacji odbiorczej: {2} [m]\nśrednia wysokość dachów budynków: {3} [m]\nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku NLOS2 straty propacyacyjne wynoszą: {0} [dB]".format(nlos2(2400, length, base_height, subscriber_height, medium_height)))
                
                elif choose in ('a', 'A'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} [km]\nwysokość stacji nadawczej: {1} [m]\nwysokość stacji odbiorczej: {2} [m]\nśrednia wysokość dachów budynków: {3} [m]\nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku LOS1 straty propacyacyjne wynoszą: {0} [dB]".format(los1(2400, length, base_height, subscriber_height, medium_height)))

                elif choose in ('b', 'B'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} [km]\nwysokość stacji nadawczej: {1} [m]\nwysokość stacji odbiorczej: {2} [m]\nśrednia wysokość dachów budynków: {3} [m]\nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku NLOS1 straty propacyacyjne wynoszą: {0} [dB]".format(nlos1(2400, length, base_height, subscriber_height, medium_height)))
                
                elif choose in ('e', 'E'):
                    print("\nPowrót do głównego menu.\n")
                    on = False
                else: 
                    print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
                    continue

        elif ans == 2:
            print("\nWybrano opcję podania wartości bez ustalonego modelu propagacyjnego. Proszę podać wartości: ")
            result = usr_input()
            length, base_height, subscriber_height, medium_height = result
            is_los_condition = check_if_los()

            print("\n\nWpisane wartości: \nodległość między antenami: {0} [m]\nwysokość stacji nadawczej: {1} [m]\nwysokość stacji odbiorczej: {2} [m]\nśrednia wysokość dachów budynków: {3} [m]\nstała częstotliwość sygnału: 2400[MHz] \nCzy na drodze propagacji fali znajdują się przeszkody?: {4}".format(length, base_height, subscriber_height, medium_height, is_los_condition))

            if subscriber_height >= medium_height and is_los_condition == 'nie':
                print(" \nJest to przypadek LOS2, a straty propacyacyjne wynoszą: {0} [dB]".format(los2(2400, length, base_height, subscriber_height, medium_height, coefficient_f(p_height_func(base_height, subscriber_height, medium_height), 2400, wave_length))))

            elif subscriber_height >= medium_height and is_los_condition == 'tak':
                print(" \nJest to przypadek NLOS2, a straty propacyacyjne wynoszą: {0} [dB]".format(nlos2(2400, length, base_height, subscriber_height, medium_height)))

            elif subscriber_height < medium_height and is_los_condition == 'nie':
                print(" \nJest to przypadek LOS1, a straty propacyacyjne wynoszą: {0} [dB]".format(los1(2400, length, base_height, subscriber_height, medium_height)))

            elif subscriber_height < medium_height and is_los_condition == 'tak':
                print(" \nJest to przypadek NLOS1, a straty propacyacyjne wynoszą: {0} [dB]".format(nlos1(2400, length, base_height, subscriber_height, medium_height)))

        elif ans == 3:
            print("\nZakończono działanie programu.\n")
            loop = False

        else:     
            print("\nWpisałeś niepoprawną wartość! Spróbuj ponownie.\n")

    except ValueError:
        print("\nWpisz cyfrę!\n")    
