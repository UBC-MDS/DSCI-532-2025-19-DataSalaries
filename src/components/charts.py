import dash_vega_components as dvc

# Trend line graph
salary_trend = dvc.Vega(
    id='salary-trend',
    opt={'actions': False},
    style={'width': '100%'},
)

# Bar chart for average salary by experience level 
salary_by_experience_level = dvc.Vega(
    id='salary-by-experience-level',
    opt={'actions': False},
    style={'width': '100%'}
)

# Pie chart for average salary by company size
salary_by_company_size = dvc.Vega(
    id='salary-by-company-size',
    opt={'actions': False},
    style={'width': '50%', 'margin-left': '50px'}
)

# Pie chart for average salary by remote type
salary_by_remote_type = dvc.Vega(
    id='salary-by-remote-type',
    opt={'actions': False},
    style={'width': '50%', 'margin-left': '50px'}
)