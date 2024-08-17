import streamlit as st
import re
import os
import requests
form=""
import json
import uuid

class renderForm:
       def __init__(self) -> None:
            self.email_error=False
            self.email=st.text_input('email',args=['email'],key='email')
            self.subject=st.text_input('Subject',key='subject')
            self.message=st.text_area('message',key='message')
            self.submitButton=st.button('Send',on_click=self.submit_form)

        
       def submit_form(self):
            global form
              
            error=st.markdown("")
            match = re.match(r"(\w+)@(\w+)\.(\w{1,5})$", self.email)


            self.email_error=False if  bool(match) else True
            if self.email_error:
                # st.error('Please provide a valid email')
                error.markdown("<span style='color:red'>Please provide a valid email  </span>",unsafe_allow_html=True)
            
            elif self.email=="" or self.subject=="" or self.message=="":
                error.markdown("<span style='color:red'>Please fill out all fields  </span>",unsafe_allow_html=True)

            else :
                st.success('Your form was submitted,Thank you!')
                error.markdown("",unsafe_allow_html=True)
                sendFormToWebhook(self.email,self.subject,self.message)
            
                # st.toast(f'submitted {self.email} {self.subject} {self.message}')
                st.session_state.email=""
                st.session_state.subject=""
                st.session_state.message=""
                


st.title('Contact',anchor=False)
st.write('Do you have a project Idea,Business Inquiry,Or need professional consulting ! write me about it ')


form=renderForm()


def sendFormToWebhook(email,subject,message):
        payload={
             
        }
        payload["email"]=email
        payload["subject"]=subject
        payload["message"]=message
        
        Myheaders = {
            'Authorization': 'Bearer ' + st.secrets["APPLICATION_SECRET"],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
                }

        json_data = {
            'application_id':  st.secrets["APP_ID"],
            'event_id': str(uuid.uuid4()),
            'event_type': 'contacts.action.created',
            'metadata': {},
            'labels': {
                'all': 'yes',
            },
            'occurred_at': '2022-11-04T16:12:58Z',
            'payload_content_type': 'application/json',
            'payload': json.dumps(payload),
        }
        # print(json_data)
        # print(headers)

        response = requests.post('https://app.hook0.com/api/v1/event/', headers=Myheaders, json=json_data)


               

                