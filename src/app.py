from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from .components import sidebar, footer, title, collapse_button, collapse_section, layout
from .components.charts import (
    salary_trend, salary_by_experience_level, salary_by_company_size,
    salary_by_remote_type, salary_by_location)
from .callbacks import update_charts, update_button
from .data import load_clean_data
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