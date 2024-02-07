from dash import Dash, html, dcc, callback, Output, Input
import dash_mantine_components as dmc
import dash_leaflet as dl

app = Dash(
    __name__, 
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ]
)

app.layout = dmc.Container(
    children=[
        dmc.Title(f"Bioinformatics Postgraduate Degree Finder", order=1, align="center"),
        dmc.Text("A map for Masters and PhD Programs Information", size="xl", py=10),
        dl.Map(dl.TileLayer(), center=[32,0], zoom=2, style={'height':'75vh'})
    ], size="xl"
)

if __name__ == '__main__':
    app.run(debug=True)