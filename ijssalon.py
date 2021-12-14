def vraagbolletjes():
    print("Welkom bij Papi Gelato.")
    while True:
        Bolletjes = int(input("hoeveel bolletjes wilt u? : ")) #dit is een input waar ik de bolletjes vraag
        if Bolletjes >= 1 and Bolletjes <= 8:
            return Bolletjes
        else:
            print("sorry zulke grote bakken hebben wij niet")


def BakjeOfHoorntje(Bolletjes):
        if Bolletjes >= 1 and Bolletjes <= 3:
            while True:
                hoorntjeofbakje = input("Hoorntje of bakje?")
                Bakje = "bakje" and 0
                hoorntje = "bakje" and 0
                if hoorntjeofbakje == "bakje":
                    bakje = 1
                elif hoorntjeofbakje == "hoorntje":
                    hoorntje = 1
    

def Smaken(Bolletjes):
    Bolletjes2 = Bolletjes
    GekozenSmaken = []
    while Bolletjes2 > 0:
        Bolletjes2 = Bolletjes2 - 1
        WelkeSmakenBolletjes = input("Welke smaken wilt u voor bolletje |aardbei |Chocolade |Munt |Vanille : ")
        if WelkeSmakenBolletjes == "aardbei" or WelkeSmakenBolletjes == "chocolade" or WelkeSmakenBolletjes == "vanille" or WelkeSmakenBolletjes == "munt":
            GekozenSmaken.append(WelkeSmakenBolletjes)
    return GekozenSmaken
    
def bonnetje():
    totaal = (Bolletjes*1.10)

    
    print("-------------{papigelato}-------------")
    if BakjeOfHoorntje == "bakje":
        print(BakjeOfHoorntje*)

    

    
def NogMeerBestellen():
    while True:
        Nogmeerbestellen = input("Wilt u nogmeer bestellen j/n ? : ")
        if Nogmeerbestellen == "j":
            return True

        elif Nogmeerbestellen == "n":
            print("Bedankt tot ziens!!")
            
            return False
        else:
            Snapniet = print("sorry dat snap ik niet")
        


while True:
    Bolletjes = vraagbolletjes()
    WelkeSmakenBolletjes =  Smaken(Bolletjes)
    print(WelkeSmakenBolletjes)
    Hoorntjeofbakje = BakjeOfHoorntje(Bolletjes)
    bonnetje()
    if NogMeerBestellen() == False:
        break


