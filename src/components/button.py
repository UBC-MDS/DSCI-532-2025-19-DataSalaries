import dash_bootstrap_components as dbc
from dash import html

collapse_button = dbc.Button(
    "About",
    id="collapse-button",
    outline=False,
    className="collapse-btn"
)

collapse_section = dbc.Collapse(
    html.P("""
        This dashboard provides insights into salary trends across industries, locations, and experience levels. Use the filters to explore salaries by company, region, and job category."""),
    id="collapse",
    className="collapse-ct"
)


