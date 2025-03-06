from dash import html

def create_footer():
    return html.Footer(
        [
            html.Hr(),
            html.P(
                "📊DataSalaries Dashboard designed to provide salary trends and insights across various data-related roles by visualizing salary based on job title, experience level, and employment details!",
                style={'font-size': '14px'}
            ),
            html.P(
                "👨‍💻Created by Group 19 - Jessie Zhang, Tianjiao Jiang, Rashid Mammadov, Karlygash Zhakupbayeva | ",
                style={'font-size': '14px', 'display': 'inline'}
            ),
            html.A("🔗GitHub Repo", href="https://github.com/UBC-MDS/DSCI-532-2025-19-DataSalaries", target="_blank",
                   style={'font-size': '14px', 'color': 'blue', 'display': 'inline'}),
            html.P(" | 📅Last updated: March 5, 2025", style={'font-size': '14px', 'display': 'inline'}),
        ],
        style={
            'text-align': 'center',
            'padding': '10px',
            'background-color': '#f8f9fa',
            'border-top': '1px solid #ddd',
            'margin-top': '20px'
        }
    )