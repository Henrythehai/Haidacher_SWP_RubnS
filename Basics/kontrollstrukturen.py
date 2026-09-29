#if: (else)
groesse = int(input("Geben Sie ihre Größe ein: "))
if groesse > 180:
    print("Sie sind groß")
elif groesse == 180:
    print("Sie sind genau 180")
else:
    print("Sie sind kleiner als 180")

print("if abgeschlossen")

#---------------------------------------------------------
#for:
heigts = [150, 160, 170, 180, 190]
for height in heigts:
    print(height)

for x in range(5):
    print(x)

for x in range(2, 10, 12):
    print(x)

print("for abgeschlossen")

#---------------------------------------------------------
#while (break):
counter = 0
while counter <= 5:
    print(counter)
    counter += 1

counter = 0
while True:
    print(counter)
    counter +=1
    if counter > 5:
        break

print("while abgeschlossen")

#---------------------------------------------------------
#pass
alter = 18

if alter > 18:
    pass

print("pass abgeschlossen")

#---------------------------------------------------------
#try-except:
try:
    zahl = int(input("geben sie eine zahl ein: "))
    print(zahl / 10)

except:
    print("Es ist ein Fehler aufgetreten")

print("try-except abgeschlossen")