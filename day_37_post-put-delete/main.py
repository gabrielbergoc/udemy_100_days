import decouple
from pixela import Pixela
from datetime import date

USERNAME = decouple.config("USERNAME")
TOKEN = decouple.config("TOKEN")
TODAY = date.today().strftime("%Y%m%d")

user = Pixela(USERNAME, TOKEN)

user.create_graph(graph_id="graph3", name="Canto", unit="minutes", data_type="int", color="ajisai")

user.post_pixel(graph_id="graph3", pixel_date=TODAY, quantity="")