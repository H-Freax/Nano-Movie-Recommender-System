import streamlit as st
import json
import copy
from load_data import load_movies, load_users

# Load data
movies = load_movies("movies.json")
users = load_users("users.json")

st.set_page_config(page_title="Recommendation System Insights", layout="wide")

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
    .info-box {
        background-color: #e5f6ff;
        border-left: 5px solid #1e88e5;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    .warning-box {
        background-color: #fff3e0;
        border-left: 5px solid #ff9800;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
    }
    .success-box {
        background-color: #e8f5e9;
        border-left: 5px solid #4caf50;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 4px;
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

st.markdown('<p class="big-font">🔍 Recommendation System Insights</p>', unsafe_allow_html=True)

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Cold Start Problem", "Adding New Ratings", "User Activity Impact"])

with tab1:
    st.header("Understanding the Cold Start Problem")
    
    st.markdown("""
    <div class="info-box">
    <h3>What is the Cold Start Problem?</h3>
    <p>The cold start problem occurs when a recommendation system doesn't have enough data
    about new users or new items to make effective recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Types of Cold Start Problems")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4>New User Cold Start</h4>
        <p>When a new user joins the platform, the system doesn't know their preferences.
        It can't make personalized recommendations until the user provides some initial data.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>New Item Cold Start</h4>
        <p>When a new movie is added to the catalog, the system doesn't have enough data 
        about who might like it, since no users have rated or watched it yet.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.subheader("Simulation: New User Cold Start")
    
    # Create a new user simulation
    st.write("Let's simulate adding a new user with no watch history:")
    
    new_user_name = st.text_input("Enter a name for the new user", "New User")
    
    if st.button("Simulate New User"):
        st.markdown("""
        <div class="warning-box">
        <h4>Cold Start Challenge</h4>
        <p>Without any watch history or ratings, the system can only provide generic recommendations
        based on overall popularity.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show generic recommendations (top-rated movies)
        st.subheader("Generic Recommendations for New User")
        st.write("Since we don't know your preferences, here are the most popular movies overall:")
        
        top_rated = sorted(movies, key=lambda x: x['rating'], reverse=True)[:5]
        
        for movie in top_rated:
            st.markdown(f"""
            <div class="movie-card">
            <p class="movie-title">{movie['title']}</p>
            <p class="movie-details">
            <b>Genre:</b> {', '.join(movie['genre'])}<br>
            <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
            <b>Release Year:</b> {movie['release_year']}<br>
            <b>Recommendation reason:</b> One of our highest-rated movies
            </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>Cold Start Solutions</h4>
    <p><b>Common solutions to the cold start problem include:</b></p>
    <ul>
        <li><b>Onboarding Questionnaires:</b> Ask new users about their preferences</li>
        <li><b>Content-Based Filtering:</b> Recommend based on item characteristics</li>
        <li><b>Hybrid Approaches:</b> Combine multiple recommendation techniques</li>
        <li><b>Social Network Integration:</b> Use social connections to infer preferences</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.header("How New Ratings Change Recommendations")
    
    st.markdown("""
    <div class="info-box">
    <p>Every time a user rates a movie, the recommendation system learns more about their preferences.
    Let's see how adding ratings changes the recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Select a user to simulate
    selected_name = st.selectbox("Choose a user to simulate:", [user['name'] for user in users])
    selected_user = next((user for user in users if user['name'] == selected_name), None)
    
    if selected_user:
        # Make a copy of the user to simulate changes
        simulation_user = copy.deepcopy(selected_user)
        watched_titles = set(simulation_user['watched_movies'])
        
        # Current recommendations before new ratings
        st.subheader("Current Recommendations")
        
        # Calculate current genre preferences
        genre_counts = {}
        for title in watched_titles:
            movie = next((m for m in movies if m['title'] == title), None)
            if movie:
                for genre in movie['genre']:
                    genre_counts[genre] = genre_counts.get(genre, 0) + 1
        
        favorite_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:2]
        favorite_genre_names = [genre for genre, _ in favorite_genres]
        
        # Get initial recommendations based on genre preferences
        unwatched_movies = [m for m in movies if m['title'] not in watched_titles]
        initial_recommendations = []
        
        for movie in unwatched_movies:
            if any(genre in movie['genre'] for genre in favorite_genre_names):
                initial_recommendations.append(movie)
        
        initial_recommendations = sorted(initial_recommendations, key=lambda x: x['rating'], reverse=True)[:3]
        
        for movie in initial_recommendations:
            matching_genres = [g for g in movie['genre'] if g in favorite_genre_names]
            st.markdown(f"""
            <div class="movie-card">
            <p class="movie-title">{movie['title']}</p>
            <p class="movie-details">
            <b>Genre:</b> {', '.join(movie['genre'])}<br>
            <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
            <b>Recommended because:</b> Matches your preferred genres ({', '.join(matching_genres)})
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Let user add new ratings
        st.subheader("Add New Movies to Your Watch History")
        
        available_to_add = [m for m in movies if m['title'] not in watched_titles]
        
        # Group movies by genre for better selection
        genre_options = list(set(genre for movie in movies for genre in movie['genre']))
        selected_add_genre = st.selectbox(
            "Filter by genre:", 
            ["All Genres"] + genre_options
        )
        
        # Filter movies by selected genre
        if selected_add_genre != "All Genres":
            filtered_to_add = [m for m in available_to_add if selected_add_genre in m['genre']]
        else:
            filtered_to_add = available_to_add
            
        # Display movies that can be added
        selected_titles = []
        for i in range(0, len(filtered_to_add), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(filtered_to_add):
                    movie = filtered_to_add[i + j]
                    with cols[j]:
                        if st.checkbox(f"{movie['title']} ({movie['rating']}⭐)", key=f"add_{movie['title']}"):
                            selected_titles.append(movie['title'])
        
        if st.button("Update Watch History"):
            # Update the simulation user's watched movies
            simulation_user['watched_movies'].extend(selected_titles)
            updated_watched = set(simulation_user['watched_movies'])
            
            st.markdown("""
            <div class="success-box">
            <h4>Watch History Updated!</h4>
            <p>Your simulated watch history has been updated with the selected movies.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Recalculate genre preferences
            updated_genre_counts = {}
            for title in updated_watched:
                movie = next((m for m in movies if m['title'] == title), None)
                if movie:
                    for genre in movie['genre']:
                        updated_genre_counts[genre] = updated_genre_counts.get(genre, 0) + 1
            
            updated_favorite_genres = sorted(updated_genre_counts.items(), key=lambda x: x[1], reverse=True)[:2]
            updated_genre_names = [genre for genre, _ in updated_favorite_genres]
            
            # Before and after genre comparison
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Before: Genre Preferences")
                st.write(", ".join([f"{genre} ({count})" for genre, count in favorite_genres]))
            
            with col2:
                st.subheader("After: Genre Preferences")
                st.write(", ".join([f"{genre} ({count})" for genre, count in updated_favorite_genres]))
            
            # Updated recommendations
            st.subheader("Updated Recommendations")
            
            # Get new recommendations
            updated_unwatched = [m for m in movies if m['title'] not in updated_watched]
            updated_recommendations = []
            
            for movie in updated_unwatched:
                if any(genre in movie['genre'] for genre in updated_genre_names):
                    updated_recommendations.append(movie)
            
            updated_recommendations = sorted(updated_recommendations, key=lambda x: x['rating'], reverse=True)[:3]
            
            for movie in updated_recommendations:
                matching_genres = [g for g in movie['genre'] if g in updated_genre_names]
                st.markdown(f"""
                <div class="movie-card">
                <p class="movie-title">{movie['title']}</p>
                <p class="movie-details">
                <b>Genre:</b> {', '.join(movie['genre'])}<br>
                <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                <b>Recommended because:</b> Matches your updated preferences ({', '.join(matching_genres)})
                </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Show changes in recommendations
            initial_titles = set(m['title'] for m in initial_recommendations)
            updated_titles = set(m['title'] for m in updated_recommendations)
            
            new_recommendations = updated_titles - initial_titles
            if new_recommendations:
                st.markdown("""
                <div class="info-box">
                <h4>Changes in Recommendations</h4>
                <p>Based on your updated watch history, these new movies appeared in your recommendations:</p>
                </div>
                """, unsafe_allow_html=True)
                st.write(", ".join(new_recommendations))

with tab3:
    st.header("User Activity Impact on Recommendations")
    
    st.markdown("""
    <div class="info-box">
    <p>Recommendation systems continuously learn from user activity. Let's explore how 
    different types of user activity can influence recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    activity_type = st.radio(
        "Choose a type of user activity to simulate:",
        ["Watching history", "Explicit ratings", "Browsing behavior", "Time-based preferences"]
    )
    
    if activity_type == "Watching history":
        st.markdown("""
        <div class="info-box">
        <h4>How Watching History Affects Recommendations</h4>
        <p>Every movie you watch provides data about your preferences, especially genre preferences.
        Systems typically give more weight to recently watched movies when making recommendations.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Simulation: Recent vs. Old Watch History")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Scenario: All movies watched long ago**")
            st.markdown("""
            <div class="warning-box">
            <p>When watch history is old, the system might not have a good sense of your current preferences.
            Recommendations may be outdated.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("**Example recommendations:**")
            st.write("- Based more on general popularity")
            st.write("- Less personalized to current tastes")
            st.write("- May include older movies")
        
        with col2:
            st.write("**Scenario: Recently watched movies**")
            st.markdown("""
            <div class="success-box">
            <p>Recent watch history provides strong signals about current preferences.
            Recommendations will be more relevant to what you enjoy now.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("**Example recommendations:**")
            st.write("- Highly personalized to current tastes")
            st.write("- More likely to include recent releases")
            st.write("- Better genre targeting")
    
    elif activity_type == "Explicit ratings":
        st.markdown("""
        <div class="info-box">
        <h4>How Explicit Ratings Affect Recommendations</h4>
        <p>When you rate movies (e.g., 1-5 stars), you provide strong signals about your preferences.
        Explicit ratings are typically weighted more heavily than implicit signals like viewing history.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Simulation: Rating Impact")
        
        # Create a simple rating simulation
        user_to_rate = st.selectbox("Select user:", [user['name'] for user in users])
        selected_user = next((user for user in users if user['name'] == user_to_rate), None)
        
        if selected_user:
            watched_movies = selected_user['watched_movies']
            st.write(f"Select a movie from {selected_user['name']}'s watch history to rate:")
            
            movie_to_rate = st.selectbox("Movie:", watched_movies)
            rating = st.slider("Your rating:", 1, 10, 8)
            
            if st.button("Submit Rating"):
                movie_info = next((m for m in movies if m['title'] == movie_to_rate), None)
                
                st.markdown(f"""
                <div class="success-box">
                <h4>Rating Submitted!</h4>
                <p>You rated {movie_to_rate} as {rating}/10</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.subheader("How this rating affects recommendations:")
                
                if rating >= 8:
                    st.write(f"✅ More movies like '{movie_to_rate}' will be recommended")
                    st.write(f"✅ More {', '.join(movie_info['genre'])} movies will be recommended")
                    st.write(f"✅ Movies from {movie_info['release_year']} era may be recommended more")
                elif rating <= 4:
                    st.write(f"❌ Fewer movies like '{movie_to_rate}' will be recommended")
                    st.write(f"❌ Fewer {', '.join(movie_info['genre'])} movies might be recommended")
                    st.write(f"❌ The system will prioritize different genres and styles")
                else:
                    st.write(f"➖ Neutral rating - minor impact on recommendations")
    
    elif activity_type == "Browsing behavior":
        st.markdown("""
        <div class="info-box">
        <h4>How Browsing Behavior Affects Recommendations</h4>
        <p>Modern recommendation systems track what items you view, how long you look at them,
        and which ones you click on. This implicit feedback helps refine recommendations even
        without explicit ratings.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Simulation: Browsing Session")
        
        # Simulate browsing behavior
        st.write("Let's simulate a browsing session. Select movies you're interested in:")
        
        # Group movies by genre for browsing
        genre_for_browsing = st.selectbox(
            "You're browsing this genre:", 
            list(set(genre for movie in movies for genre in movie['genre']))
        )
        
        genre_movies = [m for m in movies if genre_for_browsing in m['genre']]
        
        viewed_movies = []
        for i in range(0, len(genre_movies), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(genre_movies):
                    movie = genre_movies[i + j]
                    with cols[j]:
                        if st.checkbox(f"Viewed: {movie['title']}", key=f"browse_{movie['title']}"):
                            viewed_movies.append(movie['title'])
        
        if st.button("Analyze Browsing Session"):
            st.markdown("""
            <div class="success-box">
            <h4>Browsing Session Analyzed!</h4>
            <p>Based on your browsing behavior, we've updated your interest profile.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.subheader("Impact on Recommendations")
            
            st.write(f"You browsed {len(viewed_movies)} movies in the {genre_for_browsing} genre.")
            
            if len(viewed_movies) >= 3:
                st.write(f"👍 Strong interest in {genre_for_browsing} detected")
                st.write(f"✅ More {genre_for_browsing} movies will be recommended")
                
                # Show some recommended movies in this genre
                other_genre_movies = [m for m in movies if genre_for_browsing in m['genre'] and m['title'] not in viewed_movies]
                other_genre_movies = sorted(other_genre_movies, key=lambda x: x['rating'], reverse=True)[:3]
                
                st.subheader(f"Recommended {genre_for_browsing} Movies")
                for movie in other_genre_movies:
                    st.markdown(f"""
                    <div class="movie-card">
                    <p class="movie-title">{movie['title']}</p>
                    <p class="movie-details">
                    <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
                    <b>Release Year:</b> {movie['release_year']}<br>
                    <b>Recommended because:</b> You showed interest in {genre_for_browsing} movies
                    </p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("👎 Not enough browsing activity to detect strong preferences")
                st.write("✅ Minor adjustment to your interest profile")
    
    elif activity_type == "Time-based preferences":
        st.markdown("""
        <div class="info-box">
        <h4>How Time-Based Activity Affects Recommendations</h4>
        <p>What you watch on weekends vs. weekdays, or during different seasons, 
        can reveal patterns in your preferences. Recommendation systems can adapt to these patterns.</p>
        </div>
        """, unsafe_allow_html=True)
        
        time_scenario = st.selectbox(
            "Choose a time scenario:",
            ["Weekend evening", "Weekday morning", "Holiday season", "Summer vacation"]
        )
        
        st.subheader(f"Recommendations for: {time_scenario}")
        
        if time_scenario == "Weekend evening":
            st.write("Weekend evenings often favor relaxing, entertaining content")
            recommended_genres = ["Action", "Comedy", "Sci-Fi"]
            
        elif time_scenario == "Weekday morning":
            st.write("Weekday mornings might favor shorter, lighter content")
            recommended_genres = ["Drama", "Documentary"]
            
        elif time_scenario == "Holiday season":
            st.write("Holiday seasons often see increased interest in family and festive content")
            recommended_genres = ["Drama", "Romance"]
            
        else:  # Summer vacation
            st.write("Summer vacation periods might favor adventurous, blockbuster content")
            recommended_genres = ["Action", "Sci-Fi", "Adventure"]
        
        # Show some recommendations based on the time scenario
        time_recommendations = []
        for movie in movies:
            if any(genre in movie['genre'] for genre in recommended_genres):
                time_recommendations.append(movie)
        
        time_recommendations = sorted(time_recommendations, key=lambda x: x['rating'], reverse=True)[:3]
        
        for movie in time_recommendations:
            matching_genres = [g for g in movie['genre'] if g in recommended_genres]
            st.markdown(f"""
            <div class="movie-card">
            <p class="movie-title">{movie['title']}</p>
            <p class="movie-details">
            <b>Genre:</b> {', '.join(movie['genre'])}<br>
            <b>Rating:</b> {'⭐' * int(movie['rating']//2)} ({movie['rating']})<br>
            <b>Recommended because:</b> {', '.join(matching_genres)} movies are popular during {time_scenario.lower()}
            </p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>Continuous Learning</h4>
    <p>Modern recommendation systems continuously update their models based on user activity.
    The more you interact with the system, the better it gets at predicting what you'll enjoy.</p>
    </div>
    """, unsafe_allow_html=True) 