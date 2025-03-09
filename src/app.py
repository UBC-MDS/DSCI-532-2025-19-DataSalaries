from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from .components import sidebar, footer, title
from .components.charts import salary_trend, salary_by_experience_level, salary_by_company_size, salary_by_remote_type, salary_by_location
from .callbacks import update_charts

# Initialize Dash app
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    assets_folder="assets"
)

server = app.server

app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),

    dbc.Row([
        sidebar, 
        dbc.Col([
            # First row: Salary Trend (Full Width)
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Salary Trend Over Time, USD", className="card-header"),
                        dbc.CardBody(salary_trend, className="chart-card-body")
                    ], className="mb-4"), md=12
                )
            ]),

            # Second row: Map (Full Width)
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Average Salary by Location, USD", className="card-header"),
                        dbc.CardBody(salary_by_location, className="chart-card-body")
                    ], className="mb-4"), md=12
                )
            ]),

            # Third row: Experience Level (Bar Chart)
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Average Salary by Experience Level, USD", className="card-header"),
                        dbc.CardBody(salary_by_experience_level, className="chart-card-body")
                    ], className="mb-4"), md=12
                )
            ]),

            # Fourth row: Two Donut Charts (Company Size & Remote Type)
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Average Salary by Company Size, USD", className="card-header"),
                        dbc.CardBody(salary_by_company_size, className="chart-card-body")
                    ], className="mb-4"), md=6
                ),
                dbc.Col(
                    dbc.Card([
                        dbc.CardHeader("Average Salary by Remote Type, USD", className="card-header"),
                        dbc.CardBody(salary_by_remote_type, className="chart-card-body")
                    ], className="mb-4"), md=6
                )
            ])
        ], md=9)
    ]),
    footer
])


if __name__ == '__main__':
    app.run_server(debug=False)