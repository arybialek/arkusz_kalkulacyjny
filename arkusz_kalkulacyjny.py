import numpy as np
import os #os.system('clear') gdzie sensownie jest wrzucić czyszczenie ekranu?


#constant variables
frequency = 2400 #[MHz] 
wave_length = 300/frequency #[m] 

#changeable variables - inputs from user
#length = 4 #[km] 
#base_height = 62 #[m] 
#subscriber_height = 10 #[m] 
#medium_height = 13 #[m] 

#da się to ładniej zrobić?
########################################################################################################################
def usr_input():
    while True:
        try:
            length = int(input("Podaj odległość między antenami, wyrażoną w metrach, w granicach między 200m a 8310m: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            os.system('clear')
            continue
        else:
            if length in range(200, 8311, 1):
                length = np.round(length/1000, 3)
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')

    while True:
        try:
            base_height = int(input("Podaj wysokość zawieszenia anteny nadawczej, wyrażoną w metrach, w granicach między 30m a 120m: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if base_height in range(30, 121, 1):
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')

    while True:
        try:
            subscriber_height = int(input("Podaj wysokość anteny odbiorczej, wyrażoną w metrach, w granicach między 3m a 48m: "))        
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if subscriber_height in range(3, 49, 1):
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')   

    while True:    
        try:
            medium_height = int(input("Podaj średnią wysokość dachów budynków, wyrażoną w metrach, w granicach między 1090cm a 1510cm: "))      
            
        except:            
            print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
            continue
        else:
            if medium_height in range(1090, 1511, 1): #jak to zamienić na frange?
                medium_height = np.round(medium_height/100, 3)
                break
            else:
                print('Wpisałeś niepoprawną wartość! Spróbuj ponownie.')      

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
            
    return length, base_height, subscriber_height, medium_height, is_los_condition

########################################################################################################################

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
    + (47.2 * np.log10(base_height - medium_height))
    + (0.3 * np.log10(medium_height - subscriber_height))
    + (34.4 * np.log10( 0.5 * (base_height - subscriber_height) ) ) )
    return np.round(result_nlos2, 2) #303.04692849058847


######################################################MAIN PROGRAM#####################################################################

print("\n-------------- KALKULATOR WYZNACZAJĄCY STRATY PROPAGACYJNE DLA MODELU KIEDROWSKIEGO-KATULSKIEGO ------------")
print("----------- Wykonany na potrzeby kursu Media Transmisyjne 2 projekt. Autor: Anita Rybiałek 235133. -----------\n")
print("\nZasada działania programu: ")
print("Program pobiera od użytkownika wartości niezbędne do określenia jednego z 4 charakterystycznych przypadków modelu: ")
print("LOS1, NLOS1, LOS2, NLOS2, następnie wylicza straty propagacyjne dla konkretnego modelu." +  
" Częstotliwość sygnału jest stała i wynosi 2400[MHz]\n")


loop = True
while(loop):
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
                if choose in ('a', 'A'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height, _ = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} \nwysokość stacji nadawczej: {1} \nwysokość stacji odbiorczej: {2} \nśrednia wysokość dachów budynków: {3} \nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku LOS1 straty propacyacyjne wynoszą: {0} [dB]".format(los1(2400, length, base_height, subscriber_height, medium_height, coefficient_f(p_height_func(base_height, subscriber_height, medium_height), 2400, wave_length))))

                elif choose in ('b', 'B'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height, _ = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} \nwysokość stacji nadawczej: {1} \nwysokość stacji odbiorczej: {2} \nśrednia wysokość dachów budynków: {3} \nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku NLOS1 straty propacyacyjne wynoszą: {0} [dB]".format(nlos1(2400, length, base_height, subscriber_height, medium_height)))
                
                elif choose in ('c', 'C'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height, _ = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} \nwysokość stacji nadawczej: {1} \nwysokość stacji odbiorczej: {2} \nśrednia wysokość dachów budynków: {3} \nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku LOS2 straty propacyacyjne wynoszą: {0} [dB]".format(los2(2400, length, base_height, subscriber_height, medium_height)))

                elif choose in ('d', 'D'):
                    result = usr_input()
                    length, base_height, subscriber_height, medium_height, _ = result
                    print("\n\nWpisane wartości: \nodległość między antenami: {0} \nwysokość stacji nadawczej: {1} \nwysokość stacji odbiorczej: {2} \nśrednia wysokość dachów budynków: {3} \nstała częstotliwość sygnału: 2400[MHz]".format(length, base_height, subscriber_height, medium_height))
                    print(" \nDla przypadku NLOS2 straty propacyacyjne wynoszą: {0} [dB]".format(nlos2(2400, length, base_height, subscriber_height, medium_height)))
                
                elif choose in ('e', 'E'):
                    print("\nPowrót do głównego menu.\n")
                    on = False
                else: 
                    print("Wpisałeś niepoprawną wartość! Spróbuj ponownie.")
                    continue

        elif ans == 2:
            print("\nWybrano opcję podania wartości bez ustalonego modelu propagacyjnego. Proszę podać wartości: ")
            result = usr_input()
            length, base_height, subscriber_height, medium_height, is_los_condition = result

            print("\n\nWpisane wartości: \nodległość między antenami: {0} \nwysokość stacji nadawczej: {1} \nwysokość stacji odbiorczej: {2} \nśrednia wysokość dachów budynków: {3} \nstała częstotliwość sygnału: 2400[MHz] \nCzy na drodze propagacji fali znajdują się przeszkody?: {4}".format(length, base_height, subscriber_height, medium_height, is_los_condition))

            if subscriber_height >= medium_height and is_los_condition == 'nie':
                print(" \nJest to przypadek LOS1, a straty propacyacyjne wynoszą: {0} [dB]".format(los1(2400, length, base_height, subscriber_height, medium_height, coefficient_f(p_height_func(base_height, subscriber_height, medium_height), 2400, wave_length))))

            elif subscriber_height >= medium_height and is_los_condition == 'tak':
                print(" \nJest to przypadek NLOS1, a straty propacyacyjne wynoszą: {0} [dB]".format(nlos1(2400, length, base_height, subscriber_height, medium_height)))

            elif subscriber_height < medium_height and is_los_condition == 'nie':
                print(" \nJest to przypadek LOS2, a straty propacyacyjne wynoszą: {0} [dB]".format(los2(2400, length, base_height, subscriber_height, medium_height)))

            elif subscriber_height < medium_height and is_los_condition == 'tak':
                print(" \nJest to przypadek NLOS2, a straty propacyacyjne wynoszą: {0} [dB]".format(nlos2(2400, length, base_height, subscriber_height, medium_height)))

        elif ans == 3:
            print("\nZakończono działanie programu.\n")
            loop = False
        else:     
            print("\nWpisałeś niepoprawną wartość! Spróbuj ponownie.\n")
    except ValueError:
        print("\nWpisz cyfrę!\n")    
