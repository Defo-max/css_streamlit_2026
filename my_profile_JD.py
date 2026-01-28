# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:53:49 2026

@author: Joel
"""

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. Joel Defo"
field = "Human Genetics"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

# Add a section for publications
st.header("Publications")

# Direct clickable link 
pubmed_url = "https://pubmed.ncbi.nlm.nih.gov/?term=Joel+Defo" 
#st.markdown(f"[Click here to view Joel Defo's publications on PubMed]({pubmed_url})")
st.markdown(f"To see publications list of {name}, check [here]({pubmed_url})")


# Add a contact section
st.header("Contact Information")
email = "joel.defo@uct.ac.za"
st.write(f"You can reach {name} at {email}.")