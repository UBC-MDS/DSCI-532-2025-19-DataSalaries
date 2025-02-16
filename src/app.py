from dash import Dash, html


# Initiatlize the app
app = Dash(__name__)

# Layout
app.layout = html.Div('DataSalaries Dashboard')

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)