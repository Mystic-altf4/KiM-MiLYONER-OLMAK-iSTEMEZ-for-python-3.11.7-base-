#KİM MİLYONER OLMAK İSTEMEZ
import time
import pygame
global dogru
dogru = 0
global en
def intro():
    print("Kim Milyoner Olmak İstemez'e Hoşgeldiniz!")
    time.sleep(1)
    print("Yarışmamız şimdi başlıyor...")
def reklam():
    print("YARIŞMA KEYFİNİZİ BİR REKLAMLA BÖLÜYORUZ")
    time.sleep(2)
    print("lütfen youtube'da MysticGameDev'e abone olun")
    time.sleep(2)
    print("şu an okuduğunuz şeyi o yaptı")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("uwu")
    time.sleep(2)
    print("Şimdi yarışma devam ediyor...")
    time.sleep(2)
    print("TABİİ Kİ DE ASPEROX SARI GÜÇ'ÜN KATKILARIYLA")
    pygame.mixer.init()
    pygame.mixer.music.load("asperox.mp3")
    pygame.mixer.music.play()
def dogrugoster():
    print(f"Şu anki doğru sayınız: {dogru}")
def soru1():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Soru 1: Hangisine Dışarıdan Yiyecek İçecek Sokmak Yasaktır?")
    print("A: Çay Bahçesi, B: Uzay İstasyonu, C: Futbol Sahası, D: 51.Bölge")
    cevap1 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap1 == "A":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap1 == "B" or cevap1 == "C" or cevap1 == "D":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru1()
def soru2():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Soru 2: Türkiye'nin Başkenti Nedir?")
    print("A: Sivas, B: Konya, C: Ankara, D: Esenler")
    cevap2 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap2 == "C":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap2 == "B" or cevap2 == "A" or cevap2 == "D":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru2()
def soru3():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Soru 3: Türkiye Süper Lig'inin en iyi oyuncusu kimdir?")
    print("A: Piçardi, B: Rafa Sapla Sigma namıdiğer LİONEL RAFA MESSİLVA (prime pessi), C: Kariyerini Bitiren Osimhen, D: Batman Petrolcü Parashuayi")
    cevap3 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap3 == "B":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap3 == "C" or cevap3 == "A" or cevap3 == "D":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru3()
def soru4():
    global dogru
    print("Bu sorumuz sesli bir sorudur")
    time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load("fnf.mp3")
    pygame.mixer.music.play()
    print("Neyin menü müziğidir")
    print("A: Pro Stars, B:P2W Royale, C: Roblox'umu Geri Ver Ver Ver, D: Friday Night Fuckin 18+")
    cevap4 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap4 == "D":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap4 == "C" or cevap4 == "A" or cevap4 == "B":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru4()
    print("Tam şarkı için Gettin Freaky'i dinleyebilirsiniz")
    print("(Hiçbir menü müziği bu kadar sert saplamamıştı)")
def soru5():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Soru 5: 9'un karekökü kaçtır")
    print("A: 0 , B: 4, C: 2, D: 3")
    cevap5 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap5 == "D":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap5 == "C" or cevap5 == "A" or cevap5 == "B":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru5()
def soru6():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Soru 6: rev pavec netsret ayuros ub")
    print("A: ? , B: ???, C: ko, D: bu adam nasıl kod yazıyor")
    cevap6 = input("Lütfen sadece doğru cevabın şıkkını büyük harf şeklinde yazın\n")
    if cevap6 == "C":
        print("Doğru!")
        dogru += 1
        print("Sonraki soru!")
    elif cevap6 == "A" or cevap6 == "D" or cevap6 == "B":
        print("Yanlış")
        print("Sonraki soruyu yaparsın")
    else:
        print("BÖYLE BİR ŞIK YOK!")
        print("Tekrar Dene")
        soru6()
def introen():
    print("Welcome to Who doesn't want to be a millionare!")
    time.sleep(1)
    print("The competition starts now...")
def ad():
    print("WE ARE CUTTING YOUR FUN WITH AN AD")
    time.sleep(2)
    print("please sub to MysticGameDev on youtube")
    time.sleep(2)
    print("he made the thing you're reading rn")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("pwease")
    time.sleep(2)
    print("uwu")
    time.sleep(2)
    print("Now the competition is starting again...")
    time.sleep(2)
    print("WITH THE HELP OF ASPEROX SARI GÜÇ")
    pygame.mixer.init()
    pygame.mixer.music.load("asperox.mp3")
    pygame.mixer.music.play()
def truecount():
    print(f"Your current amonut of correct answers: {dogru}")
def q1():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Question 1: Where is it unallowed to bring food and drinks?")
    print("A: Cafe, B: ISS, C: Stadium, D: Area 51")
    cevap1 = input("Please write the correct option's letter in uppercase\n")
    if cevap1 == "A":
        print("Correct!")
        dogru += 1
        print("Next Question")
    elif cevap1 == "B" or cevap1 == "C" or cevap1 == "D":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try again")
        q1()
def q2():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Question 2: Where is the capital of Türkiye?")
    print("A: Sivas, B: Konya, C: Ankara, D: Esenler")
    cevap2 = input("Please write the correct option's letter in uppercase\n")
    if cevap2 == "C":
        print("Correct!")
        dogru += 1
        print("Next Question")
    elif cevap2 == "B" or cevap2 == "A" or cevap2 == "D":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try again")
        q2()
def q3():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Question 3: Who is the current best player of Turkish Süper Lig?")
    print("A: Bitchardi(who puts his d in his teammate's wife), B: Rafa Sapla Sigma aka LİONEL RAFA MESSİLVA (prime pessi), C: Slave Osimhen, D: Batman Oils Moneyshuayi")
    cevap3 = input("Please write the correct option's letter in uppercase\n")
    if cevap3 == "B":
        print("Correct!")
        dogru += 1
        print("Next Question!")
    elif cevap3 == "C" or cevap3 == "A" or cevap3 == "D":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try again")
        q3()
def q4():
    global dogru
    print("This question is a music one")
    time.sleep(1)
    pygame.mixer.init()
    pygame.mixer.music.load("fnf.mp3")
    pygame.mixer.music.play()
    print("What menu music is this?")
    print("A: Pro Stars, B:P2W Royale, C: Give my Roblox Back, Back, Back, D: Friday Night Fuckin 18+")
    cevap4 = input("Please write the correct option's letter in uppercase\n")
    if cevap4 == "D":
        print("Correct!")
        dogru += 1
        print("Next Question")
    elif cevap4 == "C" or cevap4 == "A" or cevap4 == "B":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try again")
        q4()
    print("For the whole song listen to Gettin Freaky")
    print("(No menu music hit this hard)")
def q5():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Question 5: What is the squareroot of 9 ?")
    print("A: 0 , B: 4, C: 2, D: 3")
    cevap5 = input("Please write the correct option's letter in uppercase\n")
    if cevap5 == "D":
        print("Correct!")
        dogru += 1
        print("Next Question")
    elif cevap5 == "C" or cevap5 == "A" or cevap5 == "B":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try again")
        q5()
def q6():
    global dogru
    pygame.mixer.init()
    pygame.mixer.music.load("cr.mp3")
    pygame.mixer.music.play()
    print("Question 6: sdrawkcab noitseuq siht rewsna")
    print("A: ? , B: ???, C: ko, D: how is this guy writing code?")
    cevap6 = input("Please write the correct option's letter in uppercase\n")
    if cevap6 == "C":
        print("Correct!")
        dogru += 1
        print("Next Question")
    elif cevap6 == "A" or cevap6 == "D" or cevap6 == "B":
        print("Wrong")
        print("Better Luck Next Time")
    else:
        print("This doesn't exist!")
        print("Try Again")
        q6()
en = input("This is a Turkish Game, press 9 and enter for English.\n Türkçe için 9 olmayan bir tuş ve enter'a basın\n")
if en != "9":
    intro()
    time.sleep(1)
    soru1()
    dogrugoster()
    soru2()
    dogrugoster()
    soru3()
    dogrugoster()
    time.sleep(1)
    soru4()
    dogrugoster()
    reklam()
    time.sleep(3)
    soru5()
    dogrugoster()
    soru6()
    dogrugoster()
elif en == "9":
    introen()
    time.sleep(1)
    q1()
    truecount()
    q2()
    truecount()
    q3()
    truecount()
    time.sleep(1)
    q4()
    truecount()
    ad()
    time.sleep(3)
    q5()
    truecount()
    q6()
    truecount()