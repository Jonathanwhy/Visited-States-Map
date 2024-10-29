import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/appmarestaing/image_host/refs/heads/main/visited_states.csv")

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'ylorbr',
    colorbar_title = 'most to least visited states'
))

fig.update_layout(
    geo_scope='usa',
    title_text="Map of visited states"
)

fig.show()