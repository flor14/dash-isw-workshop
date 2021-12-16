import dash
from dash import dcc, html


app = dash.Dash(__name__)
# Dash app layout section
app.layout = html.Div([

    html.H1(children='A Plotly plot in Dash a App'),
    html.H3(children='ISW workshop - December 2021'),

])

if __name__ == '__main__':
    app.run_server(port=8999,debug=False)
    
# https://thinkinfi.com/make-interactive-dashboard-using-dash-with-python/