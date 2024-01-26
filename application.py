import streamlit as st
import pickle
import pandas as pd
import requests


st.title("Movies Recommandation System")
movies_list=pickle.load(open('movies_for_list.pkl','rb'))
movies_df=pd.DataFrame(movies_list)
movies_list_show=movies_df['original_title'].values


similarity=pickle.load(open('similarity.pkl','rb'))
similarity_movies=pd.DataFrame(similarity)

def fetch_poster(movies_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movies_id}?api_key=a3e30ccebed599c70d60cdcf8cffd930&language=en-US')
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']
    
    



def movies_recommendation(movies):
    
    movies_index=movies_df[movies_df['original_title']==movies].index[0]
    distance=similarity_movies[movies_index]
    movies_list=sorted(list(enumerate(distance)), reverse=True,key=lambda x : x[1])[1:6]
    
  
    recommend_movies=[]
    recommend_movies_poster=[]
    for i in movies_list: 
        index=movies_df.iloc[i[0]].id
        recommend_movies.append(movies_df.iloc[i[0]].original_title)
        recommend_movies_poster.append(fetch_poster(index))
        
    return recommend_movies, recommend_movies_poster

    

option = st.selectbox(
    'How would you like to be contacted?',movies_list_show)

if st.button('Recommend'):
    recommendation_movies, poster=movies_recommendation(option)
    # for i in recommendation:
        
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_movies[0])
        st.image(poster[0])

    with col2:
        st.text(recommendation_movies[1])
        st.image(poster[1])

    with col3:
        st.text(recommendation_movies[2])
        st.image(poster[2])
        
    with col4:
        st.text(recommendation_movies[3])
        st.image(poster[3])
        
    with col5:  
        st.text(recommendation_movies[4])
        st.image(poster[4])