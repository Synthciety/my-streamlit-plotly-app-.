import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI Universe Game",
    page_icon="🤖",
    layout="wide"
)

# Inject custom CSS for claymation theme
st.markdown("""
    <style>
    body {
        background: url('https://example.com/clay-texture.jpg') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #333;
    }
    .block-container {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.4);
    }
    h1, h2, h3 {
        color: #e85d04;
        text-shadow: 2px 2px #000000;
    }
    .stButton button {
        background-color: #f4a261;
        color: #fff;
        font-size: 1.5rem;
        border-radius: 12px;
        padding: 10px 20px;
        border: 3px solid #333;
        box-shadow: 4px 4px 0px #000;
    }
    .stButton button:hover {
        background-color: #e85d04;
        transform: translateY(-2px);
        box-shadow: 6px 6px 0px #000;
    }
    .clay-avatar {
        border-radius: 50%;
        border: 5px solid #333;
        box-shadow: 0px 5px 10px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Homepage Content
st.title("🌟 Welcome to the AI Universe Game! 🌟")
st.header("Explore a Vibrant World of AI Creations")
st.write("Step into a universe of handcrafted AIs, where creativity meets endless possibilities.")

# Claymation-style avatar or character
st.image(
    "https://example.com/clay-avatar.jpg",
    width=200,
    caption="Your AI Guide",
    use_column_width="always",
    output_format="auto"
)

# Interactive Buttons
col1, col2, col3 = st.columns(3)
with col1:
    st.button("🌌 Enter the Universe")
with col2:
    st.button("🛠 Customize Your AI")
with col3:
    st.button("📖 Learn More")

# Footer
st.write("🎨 *Crafted with love to bring a claymation feel to AI exploration.*")
