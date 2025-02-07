import streamlit as st
from google_integration import get_google_cloud_credentials, fetch_prompts, update_prompt_by_name
import pandas as pd 

def set_up_credentials():
    if 'credentials' not in st.session_state:
        jstr = st.secrets.get('GOOGLE_KEY')
        credentials = get_google_cloud_credentials(jstr)
        st.session_state['credentials']=credentials
    return st.session_state['credentials']

def show_all(creds):
    s1=fetch_prompts(creds)
    df=pd.DataFrame(s1)
    st.dataframe(df, hide_index=True)

def update_one(creds):
    prompt_name=st.text_input("Prompt name")
    prompt_value=st.text_area("Prompt text")
    if st.button("Upsert"):
        s=update_prompt_by_name(creds, prompt_name,prompt_value)
        st.write(s)

def main():
    creds=set_up_credentials()
    col1,col2=st.tabs(['Review','Upsert'])
    with col1:
        show_all(creds)
    with col2:
        update_one(creds)



main()
