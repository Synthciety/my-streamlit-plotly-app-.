import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Universe", layout="wide")

# Custom CSS for Claymation Style
st.markdown("""
    <style>
        body {
            background: linear-gradient(145deg, #e0aaff, #ffbdbd);
            font-family: 'Comic Sans MS', cursive, sans-serif;
            overflow: hidden;
        }
        .container {
            text-align: center;
            margin-top: 50px;
        }
        .title {
            font-size: 4rem;
            color: #ff4500;
            text-shadow: 3px 3px 0px #ffeb99, -3px -3px 0px #ffeb99;
            transform: rotate(-1deg);
            display: inline-block;
            font-weight: bold;
        }
        .subtitle {
            font-size: 1.5rem;
            color: #4d4d4d;
            margin-top: 10px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }
        .clay-button {
            background: #ff5733;
            color: white;
            font-size: 1.2rem;
            border: none;
            padding: 15px 30px;
            border-radius: 15px;
            box-shadow: 5px 5px 0px #d94a27, -5px -5px 0px #ff725e;
            cursor: pointer;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .clay-button:hover {
            transform: scale(1.1);
            box-shadow: 7px 7px 0px #d94a27, -7px -7px 0px #ff725e;
        }
        .footer {
            margin-top: 50px;
            font-size: 1rem;
            color: #8d8d8d;
        }
    </style>
""", unsafe_allow_html=True)

# Main Container
st.markdown("""
    <div class="container">
        <div class="header">
            <h1 class="title">AI Universe</h1>
            <p class="subtitle">Create, evolve, and explore your AI in a handcrafted cosmos!</p>
        </div>
        <div class="button-container">
            <button class="clay-button" onclick="startGame()">Start Game</button>
            <button class="clay-button" onclick="aboutPage()">About</button>
            <button class="clay-button" onclick="universeMap()">Universe Map</button>
        </div>
        <div class="footer">
            <p>A world crafted by you. Let the adventure begin!</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Placeholder Functions (Streamlit doesn't support direct JavaScript events)
st.write("🚀 **Coming Soon:** Fully interactive universe exploration!")
