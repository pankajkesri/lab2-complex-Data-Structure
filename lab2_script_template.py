def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Pankaj kesri",
        "Student_ID": 10284560,
        "pizza_toppings": ["TOMATO", "ONION", "GREEN PEPPER"],
        "movies":[
            {"title": "ironman", "genre": "sci-fi"},
            {"title": "thor", "genre": "sci-fi"}
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "haunted mansion", "genre": "comedy"}
    about_me["movies"].append(new_movie)

    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ["mushrooms", "red pepper"])
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    print(f'My name is {full_name},but you can call me Sir {first_name}.\nMy student ID is {about_me["Student_ID"]}.')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'] += toppings
    about_me["pizza_toppings"] = sorted(set(about_me["pizza_toppings"]), key=str.lower)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favorite pizza toppings:")
    for topping in about_me["pizza_toppings"]:
        print(f'- {topping}')
    return 

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    print("movie genres : "+", ".join(genres))
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie["title"] for movie in movie_list]
    print("movie titles : "+", ".join(titles))
    return
    
if __name__ == '__main__':
    main()