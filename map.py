import streamlit as st

def render_html():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Highlighted Points in India Map</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <style>
            html, body, #map {
                height: 100%;
                margin: 0;
                padding: 0;
            }

            .leaflet-popup-content-wrapper {
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
                padding: 10px;
            }

            .leaflet-popup-content h3 {
                margin: 0 0 5px;
                font-size: 16px;
                color: #333;
            }

            .leaflet-popup-content p {
                margin: 0;
                font-size: 14px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div id="map"></div>

        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <script>
            var map = L.map('map', {
                maxZoom: 18 // Set maximum zoom level
            }).setView([20.5937, 78.9629], 5); // Centered on India

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
            }).addTo(map);

            var locations = [
                {lat: 28.6139, lng: 77.2090, name: 'New Delhi', description: 'Capital of India'},
                {lat: 18.9750, lng: 72.8258, name: 'Mumbai', description: 'Financial capital of India'},
                {lat: 12.9716, lng: 77.5946, name: 'Bengaluru', description: 'IT hub of India'},
                // Add more locations as needed
            ];

            locations.forEach(function(location) {
                var marker = L.marker([location.lat, location.lng], {
                    icon: L.icon({
                        iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
                        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.3.1/images/marker-shadow.png',
                        iconSize: [25, 41],
                        iconAnchor: [12, 41],
                        popupAnchor: [1, -34],
                        shadowSize: [41, 41]
                    })
                }).addTo(map);
                marker.bindPopup('<h3>' + location.name + '</h3><p>' + location.description + '</p>');

                marker.on('click', function() {
                    map.setView([location.lat, location.lng], map.getMaxZoom()); // Zoom to maximum zoom level
                });
            });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(html_code, width=800, height=600)

def main():
    st.title("Highlighted Points in India Map")
    render_html()

if __name__ == "__main__":
    main()
