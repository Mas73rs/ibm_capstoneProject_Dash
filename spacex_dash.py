import dash
from dash import dcc, html
import pandas as pd

# Load dataset
df = pd.read_csv('data/spacex_launch_dash.csv')

print(df.head())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello, Dash!"),
    html.P("This is a basic Dash app."),
])

if __name__ == '__main__':
    app.run_server(debug=True)
