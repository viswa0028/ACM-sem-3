
import streamlit as st #importing necessry libraries
import google.generativeai as genai

# configuring the API
genai.configure(api_key="[Your API Key]") #intializing the API key 
genrative_config = {"temperature": 0.9, "top_p": 1, "top_k": 1} #setting the temp,topk and topp for more creative results

# Initialize the model
model = genai.GenerativeModel("gemini-pro", generation_config=genrative_config)
if "page" not in st.session_state: # creating a multipage GUI
    st.session_state.page = "main"

def main_page(): #In the title section we are also adding sign in and login buttons
    col1, col2, col3, col4 = st.columns([5, 1, 1, 1])  # Adjust the ratio for proper spacing
    with col1:
        st.title("GPT")

    # Sign In button in the second column
    with col2:
        if st.button("Sign In"):
            st.session_state.page = "sign_in" #This will move to different page called signin
    with col3:
        if st.button("Log In"):
            st.session_state.page = "log_in" #This will also move to a different page called login

    # setting session state for question and answer
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "answer" not in st.session_state:
        st.session_state.answer = ""

    # Input space for asking quesiton
    st.session_state.question = st.text_input("Ask your question:", value=st.session_state.question)

    col1, col2 = st.columns([1, 8.5])

    # Enter button to generate the response
    with col1:
        if st.button("Enter"):
                # Generate the answer
                response = model.generate_content(st.session_state.question)
                st.session_state.answer = response.text
                st.write(f"**Answer:** {st.session_state.answer}")
    # Clear button to reset the input
    with col2:
        if st.button("Clear"):
            st.session_state.question = ""
            st.session_state.answer = ""
            st.rerun()  
def sign_in_page():
    st.title("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        # Signin logic
        if len(username)<8: 
            st.text("incorrect username")   
        else:
            st.success("Sign In successful!")  #Gives a message successful signin
            st.session_state.page = "main"  # Return to the main page after sign-in
def log_in_page():
    st.title("Log In")
    username = st.text_input("GPT username") 
    password = st.text_input("password",type= 'password')
    if st.button("Submit"): 
        #login logic
        if len(username)<8:
            st.text("incorrect username")   
        else:
            st.success("Logged IN") #Gives a message successful login
            st.session_state.page = 'main' # Return to the main page after sign-in
# this is to move to the different pages.
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "sign_in":
    sign_in_page()
elif st.session_state.page == 'log_in':
    log_in_page()
