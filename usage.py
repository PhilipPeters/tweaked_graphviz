import tweaked_graphviz
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc






app = dash.Dash(__name__)

initial_dot_source = """
digraph  {
node[style="filled"]
a ->b->d
a->c->d
}
"""

app.layout = dbc.Container(
    [   
        dbc.Row([
        dbc.Col(width = 9, children = [

        html.Div(
            tweaked_graphviz.DashInteractiveGraphviz(dot_source = initial_dot_source, id="gv", transition = 3000),
            style = {'width':'75%'},
        ),


        ]),


        ]),
    ],
    
)

"""
@app.callback(
    [Output("gv", "dot_source"), Output("gv", "engine")],
    [Input("input", "value"), Input("engine", "value")],
)
def display_output(value, engine):
    return value, engine


@app.callback(Output("selected", "children"), [Input("gv", "selected")])
def show_selected(value):
    return html.Div(value)
"""

if __name__ == "__main__":
    app.run_server(debug=True)
