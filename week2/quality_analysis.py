import matplotlib.pyplot as plt
import numpy as np

# Data from your Comparative sheet
labels = [
    'Functional Suitability', 'Performance Efficiency', 'Compatibility', 
    'Usability', 'Reliability', 'Security', 'Maintainability', 'Portability'
]

# Your actual values from the image
spotify_ratings = [4, 4, 4.75, 3, 4, 5, 4, 5]
yt_music_ratings = [3, 2, 4, 3, 4, 4, 3, 4]

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop"
# by appending the start value to the end.
spotify_ratings += spotify_ratings[:1]
yt_music_ratings += yt_music_ratings[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], labels)

# Plot Spotify data
ax.plot(angles, spotify_ratings, color='green', linewidth=2, label='Spotify')
ax.fill(angles, spotify_ratings, color='green', alpha=0.25)

# Plot YouTube Music data
ax.plot(angles, yt_music_ratings, color='red', linewidth=2, label='YouTube Music')
ax.fill(angles, yt_music_ratings, color='red', alpha=0.25)

# Add Legend and Title
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title('ISO 25010 Quality Comparison: Spotify vs YouTube Music')

# Save the chart as required
file_name = "quality_radar_Spotify_YouTubeMusic.png"
plt.savefig(file_name)
print(f"Success! Chart saved as {file_name}")
plt.show()