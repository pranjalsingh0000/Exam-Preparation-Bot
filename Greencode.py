<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Green Route Smart Navigator</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&family=Montserrat:wght@600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #4CAF50, #81C784, #A5D6A7);
            color: #333;
            overflow-x: hidden;
        }
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            background: url('https://source.unsplash.com/featured/?nature,green') no-repeat center center/cover;
            position: relative;
            color: white;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1;
        }
        .hero-content {
            z-index: 2;
            animation: fadeInUp 2s ease-out;
        }
        .hero h1 {
            font-family: 'Montserrat', sans-serif;
            font-size: 4rem;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .hero p {
            font-size: 1.5rem;
            margin: 20px 0;
        }
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: #FF5722;
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 700;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }
        .btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
        .features {
            padding: 100px 20px;
            background: white;
            text-align: center;
        }
        .features h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            margin-bottom: 50px;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .feature {
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        .feature:hover {
            transform: translateY(-10px);
        }
        .feature h3 {
            font-size: 1.5rem;
            margin-bottom: 20px;
        }
        .demo {
            padding: 100px 20px;
            background: #F1F8E9;
            text-align: center;
        }
        .demo h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            margin-bottom: 50px;
        }
        #map {
            height: 400px;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .cta {
            padding: 100px 20px;
            background: #4CAF50;
            color: white;
            text-align: center;
        }
        .cta h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        .interactive {
            padding: 50px 20px;
            background: white;
            text-align: center;
        }
        .interactive h2 {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            margin-bottom: 50px;
        }
        input, select {
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        #result {
            margin-top: 20px;
            font-size: 1.2rem;
        }
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            .hero p {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="hero-content">
            <h1>Green Route Smart Navigator</h1>
            <p>Navigate smarter, greener. Choose routes with the lowest carbon footprint or the most tree cover for ultimate comfort.</p>
            <a href="#features" class="btn">Explore Features</a>
        </div>
    </section>

    <section id="features" class="features">
        <h2>Why Green Route?</h2>
        <div class="feature-grid">
            <div class="feature">
                <h3>🌱 Lowest Carbon Footprint</h3>
                <p>Prioritize public transport, walking, or efficient driving to minimize your environmental impact. Powered by real-time emissions data.</p>
            </div>
            <div class="feature">
                <h3>🌳 Most Tree Cover</h3>
                <p>On hot days, find shaded paths with abundant greenery for a cooler, more enjoyable walk. Integrated with city tree cover datasets.</p>
            </div>
            <div class="feature">
                <h3>🌤️ Weather-Aware Routing</h3>
                <p>Uses OpenWeather API to suggest routes based on current weather, ensuring comfort and safety.</p>
            </div>
            <div class="feature">
                <h3>🗺️ Seamless Integration</h3>
                <p>Built on Google Maps API for accurate, real-time navigation with a sustainable twist.</p>
            </div>
        </div>
    </section>

    <section class="interactive">
        <h2>Try It Out!</h2>
        <p>Get weather for a city:</p>
        <input type="text" id="city" placeholder="Enter city, e.g., New York">
        <button class="btn" onclick="getWeather()">Get Weather</button>
        <div id="weather-result"></div>
        
        <p>Get a route suggestion:</p>
        <input type="text" id="start" placeholder="Start location">
        <input type="text" id="end" placeholder="End location">
        <select id="preference">
            <option value="green">Low Carbon</option>
            <option value="shade">Tree Cover</option>
        </select>
        <button class="btn" onclick="getRoute()">Get Route</button>
        <div id="route-result"></div>
    </section>

    <section class="demo">
        <h2>See It in Action</h2>
        <p>Experience a sample route with tree cover optimization. (Note: In a real app, this would integrate live APIs.)</p>
        <div id="map"></div>
    </section>

    <section class="cta">
        <h2>Ready to Go Green?</h2>
        <p>Download the app today and start navigating sustainably.</p>
        <a href="#" class="btn">Download Now</a>
    </section>

    <script src="https://maps.googleapis.com/maps/api/js?key={{ google_maps_api_key }}&callback=initMap" async defer></script>
    <script>
        function initMap() {
            const location = { lat: 40.7829, lng: -73.9654 };
            const map = new google.maps.Map(document.getElementById('map'), {
                zoom: 15,
                center: location,
                styles: [
                    { elementType: 'geometry', stylers: [{ color: '#E8F5E8' }] },
                    { elementType: 'labels.text.stroke', stylers: [{ color: '#4CAF50' }] },
                    { elementType: 'labels.text.fill', stylers: [{ color: '#4CAF50' }] },
                    { featureType: 'poi.park', elementType: 'geometry', stylers: [{ color: '#81C784' }] },
                    { featureType: 'road', elementType: 'geometry', stylers: [{ color: '#FFFFFF' }] },
                    { featureType: 'water', elementType: 'geometry', stylers: [{ color: '#A5D6A7' }] }
                ]
            });
            new google.maps.Marker({
                position: location,
                map: map,
                title: 'Green Route Example'
            });
        }

        function getWeather() {
            const city = document.getElementById('city').value;
            fetch(`/weather?city=${city}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('weather-result').innerHTML = `<p>Error: ${data.error}</p>`;
                    } else {
                        document.getElementById('weather-result').innerHTML = `
                            <p>Temperature: ${data.temperature}°C</p>
                            <p>Description: ${data.description}</p>
                            <p>Humidity: ${data.humidity}%</p>
                        `;
                    }
                });
        }

        function getRoute() {
            const start = document.getElementById('start').value;
            const end = document.getElementById('end').value;
            const preference = document.getElementById('preference').value;
            fetch(`/route?start=${start}&end=${end}&preference=${preference}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('route-result').innerHTML = `<p>${data.route}</p>`;
                });
        }
    </script>
</body>
</html>
