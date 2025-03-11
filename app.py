import streamlit as st
import json
import pandas as pd

# Load movie data
def load_movies():
    with open("movies.json", "r") as file:
        return json.load(file)

movies = load_movies()

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("""
    <style>
    .big-font { font-size:40px !important; text-align: center; }
    .movie-card {
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 10px;
        background-color: #f9f9f9;
        margin-bottom: 10px;
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
    }
    .movie-details {
        font-size: 16px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">🎬 Movie Recommender System</p>', unsafe_allow_html=True)
st.write("Find movies that match your preferences! 🎥")

st.sidebar.header("🎭 Filter Options")
genres = list(set(genre for movie in movies for genre in movie["genre"]))
selected_genre = st.sidebar.selectbox("Choose a genre", ["All"] + genres)
sort_option = st.sidebar.selectbox("Sort by", ["Rating (High to Low)", "Rating (Low to High)", "Year (Newest First)", "Year (Oldest First)"])

def filter_and_sort_movies(movies, genre, sort_option):
    filtered = movies if genre == "All" else [movie for movie in movies if genre in movie["genre"]]
    if sort_option == "Rating (High to Low)":
        return sorted(filtered, key=lambda x: x["rating"], reverse=True)
    elif sort_option == "Rating (Low to High)":
        return sorted(filtered, key=lambda x: x["rating"])
    elif sort_option == "Year (Newest First)":
        return sorted(filtered, key=lambda x: x["release_year"], reverse=True)
    elif sort_option == "Year (Oldest First)":
        return sorted(filtered, key=lambda x: x["release_year"])
    return filtered

filtered_movies = filter_and_sort_movies(movies, selected_genre, sort_option)

left_col, right_col = st.columns([3, 1])

with left_col:
    st.subheader(f"🎬 Movies in {selected_genre} Genre")
    for movie in filtered_movies:
        st.markdown(f"""
        <div class="movie-card">
        <p class="movie-title">{movie['title']}</p>
        <p class="movie-details"><b>Year:</b> {movie['release_year']}<br>
        <b>Genre:</b> {', '.join(movie['genre'])}<br>
        <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})</p>
        </div>
        """, unsafe_allow_html=True)

with right_col:
    st.subheader("🏆 Top 5 Rated Movies")
    top_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)[:5]
    for idx, movie in enumerate(top_movies):
        st.markdown(f"""
        <div class="movie-card">
        <p class="movie-title">{idx+1}. {movie['title']}</p>
        <p class="movie-details"><b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})</p>
        </div>
        """, unsafe_allow_html=True)