import streamlit as st
import random 
import string

def genrate_password(length, use_digits, use_special):
    characters = string.ascii_letters  #ascii_letters provide upper& lower letters

    if use_digits:
        characters += string.digits 

    if use_special:
        characters += string.punctuation # add special  characters(!, @, #, $, %, ^, &, *) 
        return ''.join(random.choice(characters) for _ in range (length))

st.title("Password Generator")
st.write("------------------------------------")
length = st.slider('Select Password Lenght', min_value = 6, max_value = 32, value = 12 )
use_digits = st.checkbox("Inculde Digits")
use_special= st.checkbox("Include Special Characters")

if st.button ("Generate password"):
    password = genrate_password (length, use_digits, use_special)
    st.write(f'Generated Password: `{password}`')

st.write("------------------------------------")
st.write('Create by Zennerha-Rauf')
