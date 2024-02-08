import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import requests
import json
from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image



selected = option_menu(
    menu_title = None,
    options = ["Home", "Info","Projects"],
    orientation = "horizontal",
    default_index=0,
    icons=["house-door-fill","book-half","chat-left-text-fill"],
    styles={
        "container": {"padding": "0!important", "background-color": "#4257fc"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#aba7a7",
        },
        "nav-link-selected": {"background-color": "green"},
    },
)

if selected == "Home" :
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.title(f'Movie Recommender System')


    def fetch_poster(movie_id):
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=4dc02b6c0dcd9b5e3507b886df563677&language=en-US'.format(
                movie_id))
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


    def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies = []
        recommended_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id

            recommend_movies.append(movies.iloc[i[0]].title)
            # fetch poster from  API
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommend_movies, recommended_movies_poster


    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # st.title('Movie Recommender System')

    selected_movies_name = st.selectbox(
        'Type your movie name or select form the list',
        movies['title'].values,

    )

    if st.button('Recommend'):

        names, posters = recommend(selected_movies_name)
        # for i in recommendations:
        # st.write(i)

        col1, col2, col3, col4, col5, = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])

# ------------------------------------------ Info Page ---------------------------------------

if selected == "Info":
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


    col1, col2 = st.columns(2)
    with col1:

        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)


        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        lottie_info = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_bdsthrsj.json")

        # st.title("")
        st_lottie(
            lottie_info,
            speed=1,
            # reverse=False,
            loop=True,
            quality="medium",
            height=140,
            width=290,
        )

    with col2:
        st.subheader("About Project")
        st.write("This project is based on the Data Analytics, Machine Learning. The dataset is picked from the Kaggle, origanaly from the TMDB Dataset. In this dataset there were 5000 Movies names in one dataset and in other dataset it had names of cast, crew. In this project we used the vectorization method to give the identity to the movies.")



    st.write("#")
    st.header("About Me")
    st.write("---")
    st.write("#")



    # ------ General Settings ---------


    NAME = "Aayushman Sharma"
    PAGE_ICON = "random"
    DESCRIPTION = """
    I am a 2nd Year Student pursuing B.Tech CSE ( Artificial Intelligence and Machine learning) @Galgotias University.
    I am intrested in Web Development, AI and ML.
    """
    EMAIL = "Contact Me - aayushman230@email.com"
    SOCIAL_MEDIA = {
        "GitHub": "https://github.com/Aayushman028",
        "LinkedIn": "https://www.linkedin.com/in/aayushman-sharma-9a29a621a/",
        "Instagram": "https://www.instagram.com/aayushman_12/"

    }


    # ------ Load CSS ------
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    # ------ Main Section ------

    col1, col2 = st.columns(2, gap="small")
    with col1:
        #st.image(profile_pic,width=230)
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)


        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        #lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_iv4dsx3q.json")
        lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")

        #st.title("")
        st_lottie(
            lottie_hello,
            speed=1,
            #reverse=False,
            loop=True,
            quality="medium",
            height=280,
            width=320,
        )

        #st_lottie(lottie_hello, key="hello")

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write(EMAIL)

    # ------- Social Media ---------

    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    #--------- Skills -------

    st.write("#")
    st.header("Skills")

    st.write(
        """
    - Programming: Python
    - Data Visulization: Teblu , MS Excel
    - Databses: Learning
    - Forntend: HTML , CSS
    - Other: Graphic Designing , Digital Marketing
    """
    )

if selected == "Projects":
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.title("My Projects")
        st.write("You can check my projects on GitHub, links are given below.")


    with col2:

        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)


        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_iv4dsx3q.json")
        st_lottie(
            lottie_coding,
            speed=1,
            # reverse=False,
            loop=True,
            quality="medium",
            height=280,
            # width=None,
        )

    st.write("#")

    PROJECT_1 = {
        "Electronic Website - Website Based on Electronic equipments": "https://github.com/Aayushman028/ElectronicWeb"
    }

    st.subheader("Projects & Accomplishments")
    st.write("---")

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # st.image(profile_pic,width=230)
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_project = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_eeuhulsy.json")
        st_lottie(
            lottie_project,
            speed=1,
            # reverse=False,
            loop=True,
            quality="medium",
            height=150,
            # width=None,
        )
        #lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_iv4dsx3q.json")

    with col2:
        for project, link in PROJECT_1.items():
            st.write(f"[{project}]({link})")

    st.write("#")
    PROJECT_2 = {
        "Players Prediction - This project is based on the football players performance prediction using AIML": "https://github.com/Aayushman028/football-players-predicitons"
    }

    col1, col2= st.columns(2, gap="small")
    with col1:
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)


        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 150:
                return None
            return r.json()


        lottie_prediction = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_LmW6VioIWc.json")
        st_lottie(
            lottie_prediction,
            speed=1,
            # reverse=False,
            loop=True,
            quality="medium",
            height=100,
            #width=None,
        )
    with col2:
        for project, link in PROJECT_2.items():
            st.write(f"[{project}]({link})")


    st.write("#")
    PROJECT_3 = {
        "Match Prediction - This project is based on the Football Match Winners prediction using AIML": "https://github.com/Aayushman028/football-players-predicitons"
    }

    col1, col2 = st.columns(2, gap="small")
    with col1:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 150:
                return None
            return r.json()


        lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_PC6oezZ3Yk.json")
        #st_lottie(
            #lottie_football,
            #speed=1,
            # reverse=False,
            #loop=True,
            #quality="medium",
            #height=100,
            # width=None,
        #)

    with col2:
        for project, link in PROJECT_3.items():
            st.write(f"[{project}]({link})")




