<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexora AI | Next-Gen Generation</title>
    <style>
        :root {
            --primary: #ffffff;
            --accent: #6366f1;
            --bg: #0a0a0a;
            --card: #161616;
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--primary);
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        /* Header / Navbar */
        nav {
            width: 100%;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #333;
            box-sizing: border-box;
        }

        .logo {
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 2px;
            background: linear-gradient(to right, #fff, #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .auth-btn {
            background: var(--accent);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: 0.3s;
        }

        .auth-btn:hover { opacity: 0.8; }

        /* Main Section */
        .container {
            max-width: 900px;
            width: 90%;
            margin-top: 50px;
            text-align: center;
        }

        .prompt-box {
            background: var(--card);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid #333;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        textarea {
            width: 100%;
            background: transparent;
            border: 1px solid #444;
            border-radius: 10px;
            color: white;
            padding: 15px;
            font-size: 16px;
            resize: none;
            box-sizing: border-box;
            margin-bottom: 20px;
        }

        .generate-btn {
            width: 100%;
            padding: 15px;
            background: white;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            font-size: 18px;
        }

        /* Result Area */
        #result-container {
            margin-top: 40px;
            width: 100%;
            border-radius: 15px;
            overflow: hidden;
            display: none;
        }

        #result-image {
            width: 100%;
            height: auto;
            border: 1px solid #333;
        }

        .loader {
            display: none;
            margin: 20px auto;
            border: 4px solid #333;
            border-top: 4px solid var(--accent);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
        }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>

    <nav>
        <div class="logo">NEXORA</div>
        <button class="auth-btn" onclick="connectPollinations()">Connect Account</button>
    </nav>

    <div class="container">
        <h1>Imagine anything.</h1>
        <p style="color: #888;">Generative AI built for the next generation of creators.</p>

        <div class="prompt-box">
            <textarea id="userPrompt" rows="4" placeholder="Describe what you want to create in Nexora..."></textarea>
            <button class="generate-btn" onclick="generateContent()">Generate Now</button>
            <div class="loader" id="loader"></div>
        </div>

        <div id="result-container">
            <h3>Nexora Output:</h3>
            <img id="result-image" src="" alt="Generated Content">
        </div>
    </div>

    <script>
        const CLIENT_ID = 'nexora_ai_portal'; // Nexora identification

        // 1. Authentication Flow
        function connectPollinations() {
            const redirectUri = window.location.href;
            window.location.href = `https://pollinations.ai/auth?client_id=${CLIENT_ID}&response_type=token&redirect_uri=${redirectUri}`;
        }

        // 2. Handle API Key from URL on Page Load
        window.onload = () => {
            if (window.location.hash.includes('api_key=')) {
                const params = new URLSearchParams(window.location.hash.substring(1));
                const apiKey = params.get('api_key');
                if (apiKey) {
                    localStorage.setItem('nexora_key', apiKey);
                    window.location.hash = ""; 
                    alert("Nexora: Account Linked Successfully!");
                }
            }
        };

        // 3. Generate Logic
        async function generateContent() {
            const prompt = document.getElementById('userPrompt').value;
            const key = localStorage.getItem('nexora_key');
            const loader = document.getElementById('loader');
            const resultImg = document.getElementById('result-image');
            const resultContainer = document.getElementById('result-container');

            if (!prompt) return alert("Please enter a prompt!");
            if (!key) return alert("Please Connect Account first!");

            loader.style.display = 'block';
            resultContainer.style.display = 'none';

            try {
                // Pollinations image generation URL format
                const imageUrl = `https://pollinations.ai/p/${encodeURIComponent(prompt)}?width=1024&height=1024&nologo=true&seed=${Math.floor(Math.random() * 100000)}`;
                
                // Simulating process time like Runway
                setTimeout(() => {
                    resultImg.src = imageUrl;
                    resultContainer.style.display = 'block';
                    loader.style.display = 'none';
                }, 2000);

            } catch (error) {
                alert("Nexora Error: Something went wrong.");
                loader.style.display = 'none';
            }
        }
    </script>
</body>
</html>
