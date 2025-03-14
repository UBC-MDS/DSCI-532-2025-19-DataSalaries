from dash import Dash
import dash_bootstrap_components as dbc
from .components import layout
from .callbacks import update_charts, update_button
from .utils.cache import cache

# Initialize Dash app
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder="assets",
    title="DataSalaries Dashboard"
)

# Configure cache
cache.init_app(
    app.server,
    config={'CACHE_TYPE': 'simple'})

# Deployment server setup
server = app.server 

# App Layout
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)