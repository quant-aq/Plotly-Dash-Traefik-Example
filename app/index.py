import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0"
        }
    ],

    # Include custom stylesheets here
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ],

    # Include custom js here
    external_scripts=[],
    suppress_callback_exceptions=True
)


# Build a dataframe with test data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Build a figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.layout = html.Div(
    [
        html.H1("Hello Dash"),

        html.Div("Dash: A web application framework for python"),

        dcc.Graph(id='example-graph', figure=fig)
    ], 
)


if __name__ == "__main__":
    app.run_server(host='0.0.0.0', debug=True, port=8000)