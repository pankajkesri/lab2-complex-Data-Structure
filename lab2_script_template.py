def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Pankaj kesri",
        "Student": 10284560,
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

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    Student_ID = about_me["Student"]
    print(f'My name is {full_name},but you can call me Sir {first_name}.\nMy student ID is {Student_ID}.')
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()