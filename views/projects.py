import streamlit as st


st.title('Projects')
col1,col2=st.columns(2,gap='medium',vertical_alignment='center')

with col1:
    st.subheader('Made for clients:')
    st.image(["./assets/realproject1.png"],[ st.write('a Platforms serving as phonebook for Moroccan Psychologues check it <a href="https://psychologue.link/">here </a>',unsafe_allow_html=True)],width=300,clamp=True)
    st.image(["./assets/realproject2.png"],[ st.write(' <a href="https://allopsy.ma/">Allopsy </a>',unsafe_allow_html=True)],width=300,clamp=True)

    
    st.subheader('Side Projects  I made for fun :stuck_out_tongue_closed_eyes: :')

    st.image(["./assets/p1.png"],[  st.write('Cups and Ball made with React you can play it <a href="https://cups-nball.vercel.app/">here </a>',unsafe_allow_html=True)],width=200,clamp=True)
    st.image(["./assets/p2.png"],[ st.write('1bit Space fighter made with Html5 canvas ')],width=200,clamp=True)
     


