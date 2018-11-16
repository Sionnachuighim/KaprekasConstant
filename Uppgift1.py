# Programmet beräknar för ett givet tal hur många iterationer som krävs innan givet tal blir 6174, där iterationerna följer Kaprekas specifika uträkningar. 

n = (int)(input("Ange ett fyra-siffrigt tal: "))
itert = 0
if n == 6174:
    print("6174 i 0 iterationer")                                           
else:
    while True:
        large = int( "".join(sorted(str(n).zfill(4), reverse = True)))          
        small = int( "".join(sorted(str(n).zfill(4))))                      
        itert += 1
        n = int(large)-int(small)                                           
        if n == 0:                                                          
            print("Välj ett 4-siffrigt tal n, där ej alla siffor är detsamma")
            break
        if n == 6174:
            print(str(n) + " i " + str(itert) + " iterationer " )           
            break
