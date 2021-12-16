import dash
from dash import dcc, html
from jupyter_dash import JupyterDash

app = JupyterDash(__name__)

# Dash app layout section
app.layout = html.Div([

    html.H1(children='My first Dash app'),
    html.H3(children='ISW workshop - December 2021'),

])

if __name__ == '__main__':
    app.run_server(mode="jupyterlab")
    
# https://thinkinfi.com/make-interactive-dashboard-using-dash-with-python/