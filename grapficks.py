import time

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import random
import datetime

current_time = datetime.datetime.now().time()
print(current_time)
# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
   [
      html.H2("Live Graph"),
      dcc.Graph(id="live-graph", animate=True),
      dcc.Interval(id="graph-update", interval=1*1000, n_intervals=10),
   ]
)

# Callback function to update the graph
@app.callback(Output("live-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph(n):
   # Generate random data
   x_data = list(range(100))
   y_data = [random.randint(0, 100) for _ in range(50)]

   # Create the graph trace
   trace = go.Scatter(
      x=x_data,
      y=y_data,
      mode="lines+markers",
      name="Data",
      line={"color": "rgb(0, 255, 0)"},
      marker={"color": "rgb(0, 255, 0)", "size": 8},
   )

   # Create the graph layout
   layout = go.Layout(
      title="Live Graph",
      xaxis=dict(range=[min(x_data), max(x_data)]),
      yaxis=dict(range=[min(y_data), max(y_data)]),
   )

   # Return the graph figure
   return {"data": [trace], "layout": layout}

if __name__ == "__main__":
   app.run(debug=True, port=8050)