import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# Example list of locations (latitude, longitude)
# locations = [
#     (37.7749, -122.4194),  # San Francisco
#     (34.0522, -118.2437),  # Los Angeles
#     (40.7128, -74.0060),   # New York
#     (47.6062, -122.3321),  # Seattle
#     (51.5074, -0.1278),    # London
#     # Add more locations
# ]

# locations = [
#     (37.881166,-4.7877388), # Calleja de las Flores (street)
#     (37.8808937,-4.8159205), # Restaurante Celia Jiménez
#     (37.8808937,-4.8159205), # Casa Pepe de La Judería (restaurant)
#     (37.879929,-4.7946084), # Bodegas Mezquita (restaurant)
#     (37.8802255,-4.798802), # Templo Romano (landmark)
#     (37.8795918,-4.7851984), # Capilla Mudéjar de San Bartolomé
#     (37.8756881,-4.7792184), # Torre De Calarhorra
#     (37.8766847,-4.7791214), # Roman Bridge of Cordoba
#     (37.8789098,-4.7819672) # Mosque-Cathedral of Córdoba

# ]

locations = [
    {"name": "Calleja de las Flores", "coord": (37.881166, -4.7877388)},
    {"name": "Restaurante Celia Jiménez", "coord": (37.8808937, -4.8159205)},
    {"name": "Casa Pepe de La Judería", "coord": (37.8808937, -4.8159205)},
    {"name": "Bodegas Mezquita", "coord": (37.879929, -4.7946084)},
    {"name": "Templo Romano", "coord": (37.8802255, -4.798802)},
    {"name": "Capilla Mudéjar de San Bartolomé", "coord": (37.8795918, -4.7851984)},
    {"name": "Torre De Calarhorra", "coord": (37.8756881, -4.7792184)},
    {"name": "Roman Bridge of Cordoba", "coord": (37.8766847, -4.7791214)},
    {"name": "Mosque-Cathedral of Córdoba", "coord": (37.8789098, -4.7819672)}
]


coords = [location["coord"] for location in locations]
loc_names = [location["name"] for location in locations]

# Convert locations to numpy array
coordinates = np.array(coords)

# Standardize the coordinates (important for distance-based algorithms)
scaler = StandardScaler()
coordinates_scaled = scaler.fit_transform(coordinates)

# Define DBSCAN parameters
epsilon = 0.5  # Distance threshold (e.g., 0.5 units, adjust as necessary)
min_samples = 2  # Minimum number of points to form a cluster

# Perform DBSCAN clustering
db = DBSCAN(eps=epsilon, min_samples=min_samples, metric='euclidean')
db.fit(coordinates_scaled)

# Extract labels and cluster information
labels = db.labels_
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)

print(f'Number of clusters: {num_clusters}')
for cluster in range(num_clusters):
    print(f'Cluster {cluster}:')
    for i, (point, label) in enumerate(zip(coords, labels)):
        if label == cluster:
            print(f'  {point}, {loc_names[i]}')

# Print noise points
noise_points = [locations[i] for i in range(len(labels)) if labels[i] == -1]
if noise_points:
    print(f'Noise points: {noise_points}')
else:
    print('No noise points')
