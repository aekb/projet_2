#coding: utf-8
import random

def Recherche(Nom):
    with open("score.txt", "r") as f:
        for line in f.readlines():
            # Traiter la ligne et ainsi de suite ...
            a=line.split()
            if a[0].lower()==Nom.lower():
                return int(a[1]),int(a[2])

def Affichage():
    for i in range(0,NombreTass):
        elm="*"*ListeJeux[i]
        print("{}| {}               |{}".format(i+1,elm,ListeJeux[i]))
def Score(Nb):
    s=0
    for i in range(1,Nb+1):
        s+=i*10**i
    return s
def Sauvegarde():
    ListeScore=[]
    f=open("score.txt", "r")
    d=open("Inter.txt", "w")
    for line in f.readlines():
        a=line.split()
        s=int(a[2])
        ListeScore.append((a[0],s))
        if a[0].lower()==Nom1R.lower() or a[0].lower()==Nom2R.lower():
            pass
        else:
            d.write(line)
    d.write(Nom1R+" "+str(DernierScoreJ1)+" "+str(MeilleurScore1)+"\n")
    N1=Nom1R.replace("_"," ")
    ListeScore.append((N1,MeilleurScore1))
    d.write(Nom2R+" "+str(DernierScoreJ2)+" "+str(MeilleurScore2)+"\n")
    N2=Nom2R.replace("_"," ")
    ListeScore.append((N2,MeilleurScore2))
    f.close()
    d.close()
    f=open("score.txt", "w")
    d=open("Inter.txt", "r")
    for line in d.readlines():
        f.write(line)
    f.close()
    d.close()
    return ListeScore

print("Bienvenue dans le jeux")
NomJouer1=input("Jouer Numéro 1: donner votre nom et prénom \n")
Nom1R=NomJouer1.replace(" ","_")
Question=input("Avez vous déja jouer ? \n")
if Question=="oui":
    DernierScoreJ1,MeilleurScore1=Recherche(Nom1R)
else:
    DernierScoreJ1=0
    MeilleurScore1=0
    NomJouer2=input("Joueur Numéro 2: donner votre nom et prénom \n")
    Nom2R=NomJouer2.replace(" ","_")
    Question=input("Avez vous déja jouer ?")
    if Question is "oui":
        DernierScoreJ2,MeilleurScore2=Recherche(NomJouer2)
    else:
        DernierScoreJ2=0
        MeilleurScore2=0
continuer=True
while continuer==True:  
    print("Joueur 1 dernier score : {} meilleur score: {} \n".format(DernierScoreJ1,MeilleurScore1))
    print("Joueur 2 dernier score : {} meilleur score: {} \n".format(DernierScoreJ2,MeilleurScore2))
    NombreTass=random.randint(3,7)
    print("----------- Joueur 1: {} ----------------- Joueur 2 : {} -------------------- \n".format(NomJouer1,NomJouer2))
    ListeJeux=[]
    print(NombreTass)
    TotalPierre=0
    for i in range(0,NombreTass):
        a=random.randint(3,23)
        ListeJeux.append(a)
        TotalPierre+=a
    Affichage()
    Reste=True
    Nbc1=0
    Nbc2=0
    while Reste:
        if TotalPierre==1:
            Reste=False
            Winner=2
        else:
            print("le tour du joueur 1: \n")
            j1=input("donner le tas et le nombre de pierre que vous voulez enlevez sous la forme NumTasse-NbrPierre\n")
            l=j1.split("-")
            i=int(l[0])
            j=int(l[1])
            ListeJeux[i-1]-=j
            TotalPierre-=j
            Nbc1+=1
            Affichage()
            if TotalPierre==1:
                Reste=False
                Winner=1
            else:
                print("le tour du joueur 2: \n")
                j1=input("donner le tas et le nombre de pierre que vous voulez enlevez sous la forme NumTasse-NbrPierre\n")
                l=j1.split("-")
                i=int(l[0])
                j=int(l[1])
                ListeJeux[i-1]-=j
                TotalPierre-=j
                Nbc2+=1
                Affichage()
    Score1=Score(Nbc1)
    Score2=Score(Nbc2)
    DernierScoreJ1=Score1
    DernierScoreJ2=Score2
    if Winner==1:
        if Score1 > MeilleurScore1:
            MeilleurScore1=Score1
    else:
        if Score2 > MeilleurScore2:
            MeilleurScore2=Score2
    ListeTopScore=[]
    ListeTopScore=Sauvegarde()
    ListeTopScore2=sorted(ListeTopScore, key=lambda colonnes: colonnes[1]).reverse()
    cmp=1
    print("Meilleur score :\n")
    for nom,s in ListeTopScore2:
        print("Nom: {} score: {} \n".format(nom,s))
        cmp+=1
        if cmp==11:
            break
    question2=input("voulez vous continuer ?\n")
    if question2 == "non":
        continuer=False
