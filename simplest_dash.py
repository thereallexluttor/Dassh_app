import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H2('The World Bank'),
dbc.Tabs([
    dbc.Tab([
        html.Ul([
            # same code to define the unordered list
        ]),
    ], label='Key Facts'),
    dbc.Tab([
        html.Ul([
            html.Br(),
            html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
            html.Li(['GitHub repo: ',
                     html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                            href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')])
        ])
    ], label='Project Info')
])

if __name__ == '__main__':
    app.run_server(debug=True)
