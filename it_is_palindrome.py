# message d'acceuil et explication de l'objectif du programme

print("Salut cher utilisateur,ce programme vous permettra de vérifier si un mot est un\npalindrome")
print("NB:Un palindrome est un mot dont l'ordre des lettres reste le même si on le lit\nde gauche à droite ou de droite à gauche\n")

#saisie du mot 
word=input("Entrez un mot de votre choix : ")

#conversion du mot en miniscule et comparaison

if word.lower()==word.lower()[::-1]:
    print(f"Le mot '{word}' est un palindrome")
else:
    print(f"Le mot '{word}' n'est pas un palindrome")