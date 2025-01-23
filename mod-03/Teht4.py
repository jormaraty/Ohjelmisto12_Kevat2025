'''
Ohjelma kysyy vuosiluvun ja ilmoittaa onko se karkausvuosi vai ei.
'''

# kysytään käyttäjältä vuosiluku, muunnetaan se heti kokonaisluvuksi
vuosi = int(input("Anna vuosiluku: "))

# vuosi ON karkausvuosi, jos se on jaollinen 400:lla
if vuosi % 400 == 0:
    print("Vuosi ON karkausvuosi")
# muuten, jos vuosi on jaollinen 100:lla, niin se EI ole karkausvuosi
elif vuosi % 100 == 0:
    print("Vuosi EI ole karkausvuosi")
# muuten, jos vuosi on jaollinen 4:lla, niin se on karkausvuosi
elif vuosi % 4 == 0:
    print("Vuosi ON karkausvuosi")
# muuten
else:
    print("Vuosi EI ole karkausvuosi")

# kokeillaan ratkaista tehtävä 1 lausekkeella:
# Vuosi on karkausvuosi,
# jos se on jaollinen 400:lla TAI
# (vuosi on jaollinen 4:lla mutta EI ole jaollinen 100:lla),
# muuten vuosi ei ole karkausvuosi
print("Lyhyt koodi sanoo:")

if vuosi % 400 == 0  or (vuosi % 4 == 0  and  vuosi % 100 != 0):
    print("Vuosi ON karkausvuosi")
else:
    print("Vuosi EI ole karkausvuosi")


