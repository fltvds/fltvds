def otsustamine():
    otsus = int(input("Vali number 1 või 2: "))
    while otsus != 1 and otsus !=2:
        otsus = int(input("Vali number 1 või 2: "))
    print("\n\n")
    return otsus
print("ALGUS:")
window = 0
health = 3
light = 0
print("Sa ärkasid vana mahajäetud maja pööningul. Alumistelt korrustelt kostis õudseid ja pahaendelist müra. Õudselt! Pead siit minema!")
print("\nMida sa teed?")
print("1. Vaatan aknast välja")
print("2. Lähen trepist alla")
otsus = otsustamine()
if (otsus == 1):
    print("Aknalaual sa leidsid taskulambi. Aknast näed maja tagahoovi. Siin on suurt auku piirdeaedes.")
    window = 1
    light = 1
print("Sa suundusid trepist alla. Siin on pime ja väga külm. Kogu aeg on tunne, et keegi jälgib sind sellest pimedusest.")
if (light == 1):
    print("See on hea, et sul on olemas taskulamp. See võimaldab märgata astmel olevat auku ja astuda õigeaegselt üle selle. Sa kuuled, et kõrvalruumist tuleb midagi sinu poole.")
    print("Millised on sinu tegevused?")
    print("1. Väljalülitad taskulambi")
    print("2. Valgustad heliallikat")
    otsus = otsustamine()
    if(otsus == 1):
        print("Sa lülitasid taskulambi välja ja varjusid riidekappi. Midagi õudne ja haisev möödus sujuvalt ja kadus teise tuppa. Mõne aja pärast astusid kappist välja ja suundusid trepist alla. Kogu koht oli täis vastikuid putukaid. Tahtsid isegi taskulambi välja lülitada, aga ilma taskulambita oli veelgi hirmsam.")
    else:
        print("Sa valgustasid sinna, kust heli tuli. Sa kogesid kirjeldamatut õudust, mida hiljem kunagi ei unusta. Valgustusest ehmunud koledaim olend karjus ja jooksis sinu poole. See lükkas sind maha ja lõi taskulambi välja, mis kustus ja lendas tundmatus suunas.")
        health -=1
        light = 0
        if (health == 0):
            print("Sa oled surnud.")
            exit()
else:
    print("Sa oled väga hirmul, sest ei näe selles pimeduses peaaegu midagi. Üks vale samm ja sa astud trepikojas olevasse auku. Sa kukud kohutava müraga maha. Sa tunned, et oled end kukkumisel vigastanud.")
    health -=1
    if (health == 0):
        print("Sa oled surnud.")
        exit()
    print("Sa kuuled, et kõrvalruumist tuleb midagi sinu poole. Kuhu sa peidad end?")
    print("1. Peidad ennast kappi")
    print("2. Tuled tagasi pööningule")
    otsus = otsustamine()
    if (otsus == 2):
        print("Sa ei jõudnud õigel ajal seda teha ja koletis sõi sind ära.")
        exit()
    else:
        print("Sa istud kapis. Siit ei näe midagi, aga kõike saab kuulda. Midagi tuli toast välja ja hakkas nagu koer nuusutama. Tundub, et see sind välja nuusutanud. See jõudis kappi juurde ja hakkas ahnelt sisse hingama. See teab, et sa oled siin!  Kuid sel hetkel kostis põrandal allpool südamepiinav karjumine. Asi jõnkastas ja tormas sinna, unustades kapi.")

print("Hinge kinni hoides laskute teisele korrusele. Ruumi valgustas hämaralt kuu valgus. Taskulampi ei ole vaja. Samuti ei ole vaja tähelepanu pöörata. Sa pöördud trepist alla viiva trepi poole, kuid peatud just õigel ajal. Treppe ei ole. Teie ees ei ole midagi.")
print("Mida sa teed?")
print("1. Hüppa maha")
print("2. Leia köis")
otsus = otsustamine()
if (otsus == 1):
    print("Sa hüppad maha, terav valu läbistab su jalga. Luumurd! Näed kahte ust. Peauks ja tagahoovi viiv uks.")
    health -= 1
    if (health == 0):
        print("Sa oled surnud.")
        exit()
else:
    print("Näed kahte köit. Millise võtad?")
    otsus = otsustamine()
    if (otsus == 1):
        print("See ei ole köis! See on madu! See hammustas sind ja roomas minema.")
        health -= 1
        if (health == 0):
            print("Sa oled surnud.")
            exit()
    print("Sa haarad köie ja jooksed treppi juurde.  Sa laskud ettevaatlikult alla. Näed kahte ust. Peauks ja tagahoovi viiv uks.")
print("Millise ukse valid?")
print("1. peauks")
print("2. tagahoovi uks")
if(window == 1):
    print("Mäleta et tagahoovis on suur auk hekis")
otsus = otsustamine()
if (otsus == 1):
    print("Sa jooksed peauksest välja. Aga siia on kogunenud kõik kõige koletislikumad olendid. Sa jooksed tagahoovi, vaevu suuteline neid tõrjuma.")
    health -= 1
    if (health == 0):
        print("Sa oled surnud.")
        exit()
print("Tagahoovis näed suurt auku hekist ja põgened selle kaudu. Särav päike pimestab teie silmi. Sellel pool hekki on päev. Sa oled pääsenud, kuid sa ei ole enam kunagi endine.")


input()