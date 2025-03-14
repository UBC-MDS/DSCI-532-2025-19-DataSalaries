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
        This dashboard provides a comprehensive view of salary trends, analyzing variations across job titles, experience levels, locations, and company characteristics over time. Use the filters to dynamically explore salary distributions and gain insights into evolving compensation patterns across different regions and roles!"""),
    id="collapse",
    className="collapse-ct"
)


