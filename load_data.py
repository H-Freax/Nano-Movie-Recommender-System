import json  # Built-in module for working with JSON files

# Step 2: Opening a JSON File
def load_movies(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Step 3: Verifying Loaded Data
def print_movies(movies):
    print(movies)

# Step 4: Looping Through Movies
def print_movie_titles(movies):
    for movie in movies:
        print("Movie Title:", movie["title"])

# Step 5: Extracting Movies by Genre
def get_movies_by_genre(movies, genre):
    return [movie for movie in movies if genre in movie["genre"]]

# Step 6: Displaying Filtered Movies
def print_sci_fi_movies(movies):
    sci_fi_movies = get_movies_by_genre(movies, "Sci-Fi")
    print(sci_fi_movies)

# Step 7: Finding Top-Rated Movies
def get_top_rated_movies(movies, top_n=3):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return sorted_movies[:top_n]

# Step 8: Filtering Movies by Release Year
def get_movies_by_year(movies, year):
    return [movie for movie in movies if movie["release_year"] >= year]

# Step 9: Loading User Data
def load_users(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Step 10: Finding a User’s Favorite Movies
def get_user_favorites(users, user_id):
    for user in users:
        if user["user_id"] == user_id:
            return user["watched_movies"]
    return []

if __name__ == "__main__":
    # Load movies and users
    movies = load_movies("movies.json")
    users = load_users("users.json")
    
    # Print loaded movies
    print_movies(movies)
    
    # Print movie titles
    print_movie_titles(movies)
    
    # Print Sci-Fi movies
    print_sci_fi_movies(movies)
    
    # Print top-rated movies
    top_movies = get_top_rated_movies(movies)
    print("Top 3 Rated Movies:", top_movies)
    
    # Print movies from a specific year
    movies_after_2010 = get_movies_by_year(movies, 2010)
    print("Movies released after 2010:", movies_after_2010)
    
    # Print user favorite movies
    user_101_favorites = get_user_favorites(users, 101)
    print("User 101's Favorite Movies:", user_101_favorites)
