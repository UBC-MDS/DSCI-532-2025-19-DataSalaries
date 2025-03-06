from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from data import load_clean_data
from components import create_sidebar, create_footer, title
from components.charts import salary_trend, salary_by_experience_level, salary_by_company_size, salary_by_remote_type
import callbacks.update_charts

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

df = load_clean_data()

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(title)),
    dbc.Row([
        create_sidebar(df),
        dbc.Col([
            dbc.Row([
                dbc.Col(salary_trend, md=7),
                dbc.Col(salary_by_company_size, md=3)
            ]), 
            dbc.Row([
                dbc.Col(salary_by_experience_level, md=7),
                dbc.Col(salary_by_remote_type, md=3)
            ]),
        ])
    ]),
    create_footer()
])

if __name__ == '__main__':
    app.run_server(debug=True)