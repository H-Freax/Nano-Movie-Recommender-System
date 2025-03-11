import streamlit as st
import json
from load_data import load_movies, load_users

# Load data
movies = load_movies("movies.json")
users = load_users("users.json")

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Nice UI styling
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
    .user-card {
        border: 2px solid #6c5ce7;
        padding: 15px;
        border-radius: 10px;
        background-color: #e8e4ff;
        margin-bottom: 15px;
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
    }
    .movie-details {
        font-size: 16px;
        color: #555;
    }
    .explanation {
        background-color: #fffae6;
        border-left: 5px solid #ffc107;
        padding: 10px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">🎬 Multi-Strategy Movie Recommendations</p>', unsafe_allow_html=True)
st.write("Compare different recommendation algorithms to see which works best for you!")

# User selection
st.sidebar.header("👤 Select User")
user_names = [user['name'] for user in users]
selected_name = st.sidebar.selectbox("Choose a user:", user_names)
selected_user = next((user for user in users if user['name'] == selected_name), None)

if selected_user:
    # Basic user profile
    st.header(f"👤 {selected_user['name']}'s Profile")
    st.markdown(f"""
    <div class="user-card">
    <p><b>User ID:</b> {selected_user['user_id']}</p>
    <p><b>Name:</b> {selected_user['name']}</p>
    <p><b>Movies Watched:</b> {len(selected_user['watched_movies'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display user's watched movies
    with st.expander("🎞️ Your Watched Movies", expanded=False):
        for movie_title in selected_user['watched_movies']:
            movie = next((m for m in movies if m['title'] == movie_title), None)
            if movie:
                st.markdown(f"""
                <div class="movie-card">
                <p class="movie-title">{movie['title']}</p>
                <p class="movie-details">
                <b>Genre:</b> {', '.join(movie['genre'])}<br>
                <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                <b>Release Year:</b> {movie['release_year']}
                </p>
                </div>
                """, unsafe_allow_html=True)
    
    # Prepare data for recommendations
    watched_titles = set(selected_user['watched_movies'])
    unwatched_movies = [m for m in movies if m['title'] not in watched_titles]
    
    # Calculate user's genre preferences
    genre_counts = {}
    for title in watched_titles:
        movie = next((m for m in movies if m['title'] == title), None)
        if movie:
            for genre in movie['genre']:
                genre_counts[genre] = genre_counts.get(genre, 0) + 1
    
    favorite_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    
    # RECOMMENDATION STRATEGY 1: Genre-based
    st.header("🎬 Strategy 1: Genre-Based Recommendations")
    st.markdown("""
    <div class="explanation">
    <p><b>How it works:</b> This strategy analyzes your watched movies to determine 
    your favorite genres, then recommends top-rated movies from those genres 
    that you haven't seen yet.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show genre preference analysis
    st.subheader("Your Genre Preferences:")
    genre_text = ", ".join([f"{genre} ({count} movies)" for genre, count in favorite_genres])
    st.write(genre_text)
    
    # Get genre recommendations
    genre_recommendations = []
    if favorite_genres:
        top_genre = favorite_genres[0][0]
        st.write(f"Based on your history, you seem to enjoy **{top_genre}** movies the most.")
        
        # Get unwatched movies from favorite genre
        for movie in unwatched_movies:
            if top_genre in movie['genre']:
                genre_recommendations.append(movie)
        
        # Sort by rating
        genre_recommendations.sort(key=lambda x: x['rating'], reverse=True)
        
        if genre_recommendations:
            for movie in genre_recommendations[:3]:
                st.markdown(f"""
                <div class="movie-card">
                <p class="movie-title">{movie['title']}</p>
                <p class="movie-details">
                <b>Genre:</b> {', '.join(movie['genre'])}<br>
                <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                <b>Release Year:</b> {movie['release_year']}<br>
                <b>Recommended because:</b> Contains your favorite genre ({top_genre})
                </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No genre-based recommendations found.")
    
    # RECOMMENDATION STRATEGY 2: Collaborative Filtering
    st.header("👥 Strategy 2: Similar Users Recommendations")
    st.markdown("""
    <div class="explanation">
    <p><b>How it works:</b> This strategy finds users with similar movie tastes 
    (people who watched the same movies as you), then recommends movies they enjoyed 
    that you haven't seen yet.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Find similar users
    similar_users = []
    for user in users:
        if user['name'] != selected_user['name']:
            common_movies = set(user['watched_movies']).intersection(watched_titles)
            if common_movies:
                similar_users.append({
                    'user': user,
                    'common_movies': common_movies,
                    'similarity_score': len(common_movies)
                })
    
    similar_users.sort(key=lambda x: x['similarity_score'], reverse=True)
    
    if similar_users:
        st.write(f"Found {len(similar_users)} users with similar taste:")
        for i, sim_user in enumerate(similar_users[:2]):
            st.write(f"- {sim_user['user']['name']}: {sim_user['similarity_score']} movies in common")
        
        # Get recommendations from similar users
        collaborative_recommendations = []
        for sim_user in similar_users[:2]:  # Use top 2 similar users
            for movie_title in sim_user['user']['watched_movies']:
                if movie_title not in watched_titles:
                    movie = next((m for m in movies if m['title'] == movie_title), None)
                    if movie and movie not in collaborative_recommendations:
                        collaborative_recommendations.append({
                            'movie': movie,
                            'recommender': sim_user['user']['name'],
                            'common_count': sim_user['similarity_score']
                        })
        
        if collaborative_recommendations:
            for rec in collaborative_recommendations[:3]:
                movie = rec['movie']
                st.markdown(f"""
                <div class="movie-card">
                <p class="movie-title">{movie['title']}</p>
                <p class="movie-details">
                <b>Genre:</b> {', '.join(movie['genre'])}<br>
                <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                <b>Release Year:</b> {movie['release_year']}<br>
                <b>Recommended because:</b> Watched by {rec['recommender']}, who shares {rec['common_count']} movies with you
                </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No recommendations found from similar users.")
    else:
        st.write("No similar users found.")
    
    # RECOMMENDATION STRATEGY 3: Top-Rated Movies
    st.header("⭐ Strategy 3: Top-Rated Movie Recommendations")
    st.markdown("""
    <div class="explanation">
    <p><b>How it works:</b> This simple strategy recommends the highest-rated movies
    that you haven't watched yet, regardless of genre or other factors.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sort unwatched movies by rating
    rating_recommendations = sorted(unwatched_movies, key=lambda x: x['rating'], reverse=True)
    
    if rating_recommendations:
        for movie in rating_recommendations[:3]:
            st.markdown(f"""
            <div class="movie-card">
            <p class="movie-title">{movie['title']}</p>
            <p class="movie-details">
            <b>Genre:</b> {', '.join(movie['genre'])}<br>
            <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
            <b>Release Year:</b> {movie['release_year']}<br>
            <b>Recommended because:</b> Among the highest-rated movies you haven't seen (Rating: {movie['rating']})
            </p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No top-rated recommendations found.")
    
    # RECOMMENDATION STRATEGY 4: Recency-Based
    st.header("🆕 Strategy 4: Recent Release Recommendations")
    st.markdown("""
    <div class="explanation">
    <p><b>How it works:</b> This strategy focuses on newer movies (released in the last few years)
    that match your genre preferences, helping you discover recent content you might enjoy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get recent movies (2015 and newer) in favorite genres
    if favorite_genres:
        top_two_genres = [genre for genre, _ in favorite_genres[:2]]
        recent_recommendations = []
        
        for movie in unwatched_movies:
            if (movie['release_year'] >= 2015 and 
                any(genre in movie['genre'] for genre in top_two_genres)):
                recent_recommendations.append(movie)
        
        # Sort by year (newest first)
        recent_recommendations.sort(key=lambda x: x['release_year'], reverse=True)
        
        if recent_recommendations:
            for movie in recent_recommendations[:3]:
                matching_genres = [g for g in movie['genre'] if g in top_two_genres]
                st.markdown(f"""
                <div class="movie-card">
                <p class="movie-title">{movie['title']}</p>
                <p class="movie-details">
                <b>Genre:</b> {', '.join(movie['genre'])}<br>
                <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                <b>Release Year:</b> {movie['release_year']}<br>
                <b>Recommended because:</b> Recent release ({movie['release_year']}) in your preferred genres ({', '.join(matching_genres)})
                </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No recent movie recommendations found.")
    
    # Final comparison
    st.header("🏆 Which Strategy Works Best?")
    st.write("""
    Different recommendation strategies can produce very different results:
    
    - **Genre-based** is good for finding more of what you already like
    - **Similar users** can help discover unexpected movies from people with similar taste
    - **Top-rated** ensures you don't miss critically acclaimed classics
    - **Recent releases** keeps you up to date with new content you might enjoy
    
    The best approach often combines multiple strategies for diverse recommendations!
    """) 