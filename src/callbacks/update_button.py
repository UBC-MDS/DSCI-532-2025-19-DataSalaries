from dash import Output, Input, State, callback

@callback(
    Output("collapse", "is_open"),
    Input("collapse-button", "n_clicks"),
    State("collapse", "is_open")
)

def toggle_collapse(n, is_open):
    print(n)
    print(is_open) 
    return not is_open if n else is_open