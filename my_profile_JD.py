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
st.header(f"Research Profile of {name}")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)
#This is a playground for you to try Streamlit and have fun. 

#**There's :rainbow[so much] you can build!**
st.header("Biography")
st.markdown(
    """ 
   
    
    Dr. Joel Defo is a **computational population genomics and bioinformatics researcher**. 
    He is based at the University of Cape Town, where he served 
    as Postdoctoral Fellow within the division of Human Genetics.
    He is part of a wide array of International Research Consortiums including the African Society of Human Genetics,
    the Psychiatric Genetic consortium- Africa, and the African Society of Computational Biology and Bioinformatics. 
    This pursuit extends to innovating methodologies and creating tools that disentangle human genomic diversity, aiming to reveal 
    how genetic and environmental influences shape vulnerability and predisposition to both infectious and chronic diseases.
    Dr. Joel Defo completed her PhD in Human Genetics at the University of Cape Town, and his 
    Postdoral Fellowship deals with the elucidation of the gene expression profiles of colorectal - lynch syndrome
    within a South African cohort.
    """
)

st.header("Area of Research")
st.markdown(
    """
    Dr. Joel Defo's research focuses on computational population genomic tools development, psychiatric genetics, suicide biology, and cancer genomics 
    His research has been published in high-impact international journals and presented both at major scientific conferences.
    My passion lies in advancing genomics within healthcare by leveraging computational and 
    analytical approaches to decipher the genetic and environmental framework of complex diseases, as well as variations in therapeutic response.
    I am particularly interested in identifying cross-diseases, cross-ancestry variants and underlying shared mechanisms
    Furthermore, Joel defo's interest lies to the implementation of multimodal methologies to identify HLA-specific alleles involved
    in the early detection and progression of cancer. Such have relevant implication in cancer Immunology.
    I am also interested into disease-relevant biological pathways, brain and immune cell types, neurodevelopmental windows. 
    A central aim of my work is to translate these biological discoveries into practical clinical tools that can improve outcomes for personnalized medecine
    
    """
)

# Add a section for publications
st.header("Publications")

# Direct clickable link 
pubmed_url = "https://pubmed.ncbi.nlm.nih.gov/?term=Joel+Defo" 
github_url = "https://github.com/Defo-max/css_streamlit_2026"
research_lab = "https://health.uct.ac.za/human-genetics"
#st.markdown(f"[Click here to view Joel Defo's publications on PubMed]({pubmed_url})")
st.markdown(f" View {name} publications list on [Pubmed]({pubmed_url})")


# Add a contact section
st.header("Contact Information")
email = "joel.defo@uct.ac.za"
st.write(f"Learn more about Dr. Joel Defo's lab [here]({research_lab})")
st.write(f"My github page can be accessed [here]({github_url})")
st.write(f"You can reach {name} at {email}.")