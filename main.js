import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Maze.io - Interactive Landing Page", layout="wide")

# HTML content for the landing page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maze.io - Interactive Landing Page</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            background: url('https://example.com/rick_and_morty_background.jpg') no-repeat center center;
            background-size: cover;
        }
        #keyhole {
            width: 200px;
            height: 400px;
            background: url('https://example.com/keyhole.png') no-repeat center center;
            background-size: contain;
            cursor: pointer;
            animation: glow 1.5s infinite alternate;
        }
        @keyframes glow {
            from {
                box-shadow: 0 0 10px #fff;
            }
            to {
                box-shadow: 0 0 20px #fff;
            }
        }
    </style>
</head>
<body>
    <div id="keyhole"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Create the scene
        const scene = new THREE.Scene();

        // Create a camera
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 5;

        // Create a renderer
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Create a more complex object (e.g., a torus knot)
        const geometry = new THREE.TorusKnotGeometry(1, 0.4, 100, 16);
        const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
        const torusKnot = new THREE.Mesh(geometry, material);
        scene.add(torusKnot);

        // Add lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);

        const pointLight = new THREE.PointLight(0xffffff, 1);
        pointLight.position.set(5, 5, 5);
        scene.add(pointLight);

        // Animation loop
        function animate() {
            requestAnimation
