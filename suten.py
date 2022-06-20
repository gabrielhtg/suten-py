import random
import os

os.system("cls||clear")

skor_pemain = 0
skor_komputer = 0

while True :
    os.system("cls||clear")
    computer_input = random.choice([1, 2, 3])
    print("-------------------------------------------------------")
    print("Skor pemain      :", skor_pemain)
    print("Skor komputer    :", skor_komputer)
    print("-------------------------------------------------------")
    print(" 1. Jari Jempol\n 2. Jari Telunjuk\n 3. Jari Kelingking\n 4. Exit the program")
    print("-------------------------------------------------------")
    user_input = int(input("Masukkan jari yang anda masukkan sesuai nomornya : "))
    print("-------------------------------------------------------")
    
    if user_input == 4 :
        quit()
        
    elif (user_input not in [1, 2 ,3]) or (user_input == computer_input) :
        continue
    
    elif (user_input == 1) and (computer_input == 2) :
        skor_pemain += 1
        
    elif (user_input == 1) and (computer_input == 3) :
        skor_komputer += 1     
        
    elif (user_input == 2) and (computer_input == 1) :
        skor_komputer += 1
        
    elif (user_input == 2) and (computer_input == 3) :
        skor_pemain += 1
        
    elif (user_input == 3) and (computer_input == 1) :
        skor_pemain += 1
    
    else :
        skor_komputer += 1
        
