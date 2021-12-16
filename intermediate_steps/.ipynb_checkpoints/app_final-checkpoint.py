import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
import plotly.express as px

# Import irish dataset
df = px.data.iris()

# Create plotly plot
plotly_fig = px.scatter(df,
                        x="sepal_width", 
                        y="sepal_length",
                        color="species",
                        size='petal_length',
                        hover_data=['petal_width'])


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.QUARTZ]) #https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

# Dash app layout section
app.layout = html.Div([

    html.H1(children='My first Dash app'),
    html.H3(children='ISW workshop - December 2021'),

# Insert plotly plot into dash
    dcc.Graph(id='graph', figure=plotly_fig, style={'width': '70vh', 'height': '50vh'})
])

if __name__ == '__main__':
    app.run_server(mode="jupyterlab")
    
# Extracted from: https://thinkinfi.com/make-interactive-dashboard-using-dash-with-python/