import dash
from dash import html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
iris = data.iris()

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='ycol-widget',
        value='sepalLength',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in iris.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(iris).mark_point().encode(
        y=ycol,
        x='petalWidth',
        tooltip='sepalLength').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
