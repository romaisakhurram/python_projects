# password strength

import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Start with letters (a-z, A-Z)
    
    if use_digits:
        characters += string.digits  # Add numbers (0-9)
    
    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&*()_+ etc)
    
    return ''.join(random.choice(characters) for _ in range(length))  # Properly indented

# Streamlit UI
st.title("Password Strength Checker")  # Fixed typo in st.title
length = st.slider("Select the length of the password", min_value=8, max_value=20, value=12)
use_digits = st.checkbox("Include digits (0-9)")
use_special = st.checkbox("Include special characters (!@#$%^&*()_+)")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")
    st.write(".....................................")