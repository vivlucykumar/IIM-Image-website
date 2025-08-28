# app.py
import streamlit as st
import os
import math

# Set the page configuration for a wider layout
st.set_page_config(
    page_title="IIMA Journey",
    page_icon="�",
    layout="wide"
)

# --- App Title and Description ---
st.title("Our IIMA Journey 🎓")
st.markdown(
    """
    **A collection of memories from Our time at the Indian Institute of Management Ahmedabad.**
    
    This page displays your photos in a multi-column grid for easy browsing.
    """
)

# --- Get Images from the assets folder ---
image_folder = "assets"

# Check if the assets folder exists
if not os.path.isdir(image_folder):
    st.error("The 'assets' folder was not found. Please create it and add your images.")
else:
    # Get a list of all image files in the assets folder
    # We filter for common image file extensions
    image_files = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.endswith(('.png', '.JPG', '.jpeg', '.gif', '.bmp', '.tiff'))
    ]

    # Check if any images were found
    if not image_files:
        st.warning("No images found in the 'assets' folder. Please add your pictures to start the gallery!")
    else:
        st.subheader("Photo Gallery")
        st.write(f"Displaying **{len(image_files)}** photos from your journey.")

        # Display the images in a grid format
        # You can adjust the number of columns and items per page
        COLS_PER_ROW = 4
        IMAGES_PER_PAGE = 20

        # Create pagination
        total_pages = math.ceil(len(image_files) / IMAGES_PER_PAGE)
        page_number = st.number_input(
            "Select a page:", 
            min_value=1, 
            max_value=total_pages, 
            value=1, 
            step=1
        )

        start_index = (page_number - 1) * IMAGES_PER_PAGE
        end_index = start_index + IMAGES_PER_PAGE
        images_on_page = image_files[start_index:end_index]

        # Use st.columns to create the grid
        for i, image_path in enumerate(images_on_page):
            if i % COLS_PER_ROW == 0:
                cols = st.columns(COLS_PER_ROW)
            with cols[i % COLS_PER_ROW]:
                st.image(image_path, use_container_width=True)
                st.caption(os.path.basename(image_path))


