import streamlit as st


st.title('Projects')
col1,col2=st.columns(2,gap='medium',vertical_alignment='center')

with col1:
    st.subheader('Mobile Apps:')
    st.image(["./assets/app1.png","./assets/app2.png","./assets/app3.png","./assets/app4.png","./assets/app5.png"]
             ,[ st.write('Ecommerce Store app built with Flutter and Firebase (app is for developpement only) <a href="https://www.mediafire.com/file/3smhjneupk5qrec/shoes-release.apk/file">get it here</a>',unsafe_allow_html=True)],width=300,clamp=True)
    # st.image(["./assets/realproject2.png"],[ st.write(' <a href="https://allopsy.ma/">Allopsy </a>',unsafe_allow_html=True)],width=300,clamp=True)
    
    st.subheader('My start ups:')
    st.image(["./assets/startup1.png"],[ st.write('An AI chatbot for generating cooking recipes <a href="https://myaichef.pages.dev/">MyAiChef </a>',unsafe_allow_html=True)],width=300,clamp=True)
    # st.image(["./assets/realproject2.png"],[ st.write(' <a href="https://allopsy.ma/">Allopsy </a>',unsafe_allow_html=True)],width=300,clamp=True)

    st.subheader('Made for clients:')
    st.image(["./assets/realproject1.png"],[ st.write('a Platforms serving as phonebook for Moroccan Psychologues check it <a href="https://psychologue.link/">here </a>',unsafe_allow_html=True)],width=300,clamp=True)
    st.image(["./assets/realproject2.png"],[ st.write(' <a href="https://allopsy.ma/">Allopsy </a>',unsafe_allow_html=True)],width=300,clamp=True)

    
    st.subheader('Side Projects  I made for fun :stuck_out_tongue_closed_eyes: :')

    st.image(["./assets/p1.png"],[  st.write('Cups and Ball made with React you can play it <a href="https://cups-nball.vercel.app/">here </a>',unsafe_allow_html=True)],width=200,clamp=True)
    st.image(["./assets/p2.png"],[ st.write('1bit Space fighter made with Html5 canvas ')],width=200,clamp=True)
     


