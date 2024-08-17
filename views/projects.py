import streamlit as st


st.title('Projects')
col1,col2=st.columns(2,gap='medium',vertical_alignment='center')

with col1:
    st.subheader('Made for clients:')
    st.image(["./assets/p1.png"],[  st.write('Cups and Ball made with React ')],width=200,clamp=True)
    st.image(["./assets/p2.png"],[ st.write('1bit Space fighter made with Html5 canvas ')],width=200,clamp=True)

     


