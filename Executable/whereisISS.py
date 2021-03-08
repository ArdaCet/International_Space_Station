import time
from IPython.display import clear_output
import pandas as pd
import plotly.express as plt


ISS_url = "http://api.open-notify.org/iss-now.json"

while True:
  
  readJson = pd.read_json(ISS_url)

  readJson["Longtitude"] = readJson.loc["longitude", "iss_position"]
  readJson["Latitude"] = readJson.loc["latitude", "iss_position"]

  readJson.reset_index(inplace=True)

  readJson = readJson.drop(["iss_position", "message", "index"], axis = 1)

  ISS_df = readJson.reindex(columns=["Longtitude", "Latitude", "timestamp"])

  fig = plt.scatter_geo(data_frame = ISS_df, lat = "Latitude", lon = "Longtitude", labels = {"Latitude": "X", "Longtitude" : "Y"}, opacity = 0.9)
     
  ISS_geo = fig.show()

  time.sleep(5)

  clear_output(wait=True)
  print(ISS_geo, flush=True)
