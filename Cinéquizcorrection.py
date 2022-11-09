import random
import os
# movies = []
# years = []

# for i in range(0,4):
#     movies += [input("Saisir le titre d'un film : ")]
#     years += [input(f"Saisir l'année de sortie de \"{movies[i]}\" : ")]

movies = ["Titanic","LOL","Star wars VI","300","Avatar"]
years = [1990,2008,1976,2010,2005]

menu = ["Quitter","Afficher tous les films"] + [f"Afficher l'année de sortie du film {movie}" for movie in movies] + ["Lancer le Quizz"]

choice = 1
while choice != 0:
    for (index,menuItem) in enumerate(menu):
        print(f"{index}. {menuItem}")
    choice = int(input("Votre choix : "))
    if choice == 1:
        os.system("cls")
        res = ""
        for movie in movies:
            res += f"{movie}\n"
        print(res)
    elif choice >= 2 and choice < len(menu) - 1:
        os.system("cls")
        print("\n-------------------------------------------------------------")
        print(f"Le film {movies[choice-2]} est sorti en {years[choice-2]}.")
        print("-------------------------------------------------------------\n")
    elif choice == len(menu) - 1: # Quizz
        score = 0
        movieIndexesKnown = []
        for i in range(0,len(movies)):
            # Tirage d'un film au hasard
            randomMovieIndex = random.randint(0, len(movies) - 1)
            while randomMovieIndex in movieIndexesKnown:
                randomMovieIndex = random.randint(0, len(movies) - 1)
            movieIndexesKnown += [randomMovieIndex]

            # On stock la bonne réponse (la bonne année)
            goodAnswer = years[randomMovieIndex]

            # On genère 3 choix d'année aléatoire
            randomYears = []
            for i in range(0,3):
                randomYear = random.randint(1891,2022)
                while randomYear in randomYears:
                    randomYear = random.randint(1891,2022)
                randomYears += [randomYear]

            # On ajoute ces 3 années au tableau de réponses possibles
            choices = [goodAnswer] + randomYears

            # On affiche la question et les choix
            print(f"En quelle année est sortie le film {movies[randomMovieIndex]} ?")
            letters = ["A","B","C","D"]
            random.shuffle(choices)
            for j in range(0, len(choices)):
                print(f"{letters[j]}. {choices[j]}")

            # On analyse la réponse
            answer = "Z"
            while answer not in letters:
                answer = input("Votre réponse : ").upper()

            # On traite le score
            if choices[letters.index(answer)] == goodAnswer:
                score += 1
        os.system("cls")
        print(f"Votre score est de {score}/{len(movies)}")