import random
import os
# movies = []
# years = []

# for i in range(0,4):
#     movies += [input("Enter the title of a movie : ")]
#     years += [input(f"Enter the year of exit of \"{movies[i]}\" : ")]

movies = ["Titanic","LOL","Star wars VI","300","Avatar"]
years = [1990,2008,1976,2010,2005]

menu = ["Leave","View all movies"] + [f"Show the year of release of the film {movie}" for movie in movies] + ["Launch the Quiz"]

choice = 1
while choice != 0:
    for (index,menuItem) in enumerate(menu):
        print(f"{index}. {menuItem}")
    choice = int(input("Your choice : "))
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
    elif choice == len(menu) - 1: # Quiz
        score = 0
        movieIndexesKnown = []
        for i in range(0,len(movies)):
            # Drawing of a random film
            randomMovieIndex = random.randint(0, len(movies) - 1)
            while randomMovieIndex in movieIndexesKnown:
                randomMovieIndex = random.randint(0, len(movies) - 1)
            movieIndexesKnown += [randomMovieIndex]

            # We stock the right answer (the right year)
            goodAnswer = years[randomMovieIndex]

            # We generate 3 random year choices
            randomYears = []
            for i in range(0,3):
                randomYear = random.randint(1891,2022)
                while randomYear in randomYears:
                    randomYear = random.randint(1891,2022)
                randomYears += [randomYear]

            # We add these 3 years to the table of possible answers
            choices = [goodAnswer] + randomYears

            # We display the question and the choices
            print(f"In which year was the film released {movies[randomMovieIndex]} ?")
            letters = ["A","B","C","D"]
            random.shuffle(choices)
            for j in range(0, len(choices)):
                print(f"{letters[j]}. {choices[j]}")

            # We analyze the response
            answer = "Z"
            while answer not in letters:
                answer = input("Your response : ").upper()

            # We process the score
            if choices[letters.index(answer)] == goodAnswer:
                score += 1
        os.system("cls")
        print(f"Votre score est de {score}/{len(movies)}")
