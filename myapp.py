import streamlit as st



about_page=st.Page(page="./views/about.py",title='About Me',
                   icon=":material/person:",default=True)

projects_page=st.Page(page="./views/projects.py",title='Projects',
                   icon=":material/workspaces:")

contact_page=st.Page(page="./views/contact.py",title='Contact',
                   icon=":material/email:")

home=st.navigation(pages=[about_page,projects_page,contact_page])
home.run()
