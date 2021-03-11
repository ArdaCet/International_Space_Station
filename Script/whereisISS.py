import time
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import urllib.request, json

# Retreive coordinates from this API
ISS_url = "http://api.open-notify.org/iss-now.json"

while True:
	# Create world map
    m = Basemap(projection='mill', resolution = 'l')
    m.fillcontinents()
    m.drawcoastlines(color="white")
	
	# Arrange a plot title
    plt.title("International Space Station real-time Position")
    
	# Parse the UPI
    with urllib.request.urlopen(ISS_url)as url:
        data = json.loads(url.read().decode())

    ISS_latitude = data["iss_position"]["latitude"]
    ISS_longitude = data["iss_position"]["longitude"]

    url.close()
    
    # ISS coordinates
    lonx = float(ISS_longitude)
    laty = float(ISS_latitude)

    # Test Coordinates of known location: Istanbul
    #ist_lon_x = 28.5859
    #ist_lat_y = 41.0016
	
	# Plot the coordinates on world map
    m.plot(lonx, laty, 'co', markersize=4, latlon=True)
	
	# To run the script in full size
    plt.get_current_fig_manager().window.state('zoomed')
	
	# Project the plots to the sscreen
    plt.draw()
    plt.pause(1)
