def vraagbolletjes():
    while True:
    
        print("Welkom bij Papi Gelato.")
        Bolletjes = int(input("hoeveel bolletjes wilt u? : ")) #dit is een input waar ik de bolletjes vraag
        if Bolletjes >= 1 and Bolletjes <= 8:
            return Bolletjes
        else:
            print("sorry zulke grote bakken hebben wij niet")


def BakjeOfHoorntje(Bolletjes):
        if Bolletjes >= 1 and Bolletjes <= 3:
            while True:
                hoorntjeofbakje = input("Hoorntje of bakje?")
                if hoorntjeofbakje == 'hoorntje' or hoorntjeofbakje == "bakje":
                    return hoorntjeofbakje        
        elif Bolletjes >= 4:
            return "bakje"

def Smaken(Bolletjes):
    Bolletjes2 = Bolletjes
    while Bolletjes2 > 0:
        Bolletjes2 = Bolletjes2 - 1
        WelkeSmakenBolletjes = input("Welke smaken wilt u voor bolletje |aardbei |Chocolade |Munt |Vanille : ")
    if WelkeSmakenBolletjes == "aardbei" or WelkeSmakenBolletjes == "chocolade" or WelkeSmakenBolletjes == "vanille" or WelkeSmakenBolletjes == "munt":
            return WelkeSmakenBolletjes
    

    
def NogMeerBestellen():
    
    Nogmeerbestellen = input(f"Hier is uw {BakjeOfHoorntje} met {Bolletjes} bolletje(s) Wilt u nogmeer bestellen j/n ? : ")
    if Nogmeerbestellen == "j":
        return vraagbolletjes()
    elif Nogmeerbestellen == "n":
        print("Bedankt tot ziens!!")
        exit()
    else:
        Snapniet = print("sorry dat snap ik niet")
        
    



Bolletjes = vraagbolletjes()
WelkeSmakenBolletjes =  Smaken(Bolletjes)
BakjeOfHoorntje = BakjeOfHoorntje(Bolletjes)
NogMeerBestellen()


