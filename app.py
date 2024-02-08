from dash import Dash, html, dcc, callback, Output, Input
import dash_mantine_components as dmc
import dash_leaflet as dl
import pandas as pd

df = pd.read_excel('data.xlsx')

def popUpText(index):
    return dmc.List([
        dmc.ListItem(dmc.Anchor(df['University'][index], href=df['Website'][index], underline=False)),
        dmc.ListItem([dmc.Text("Program: ", weight=700), df['Program'][index]]),
        dmc.ListItem([dmc.Text("Deadline: ", weight=700), df['Deadline'][index]]),
        dmc.ListItem([dmc.Text("App Fee: ", weight=700), df['App Fee'][index]]),
        dmc.ListItem([dmc.Text("State: ", weight=700), df['Location'][index]]),
        dmc.ListItem([dmc.Text("Ranking: ", weight=700), df['US News Ranking (2018)'][index]]),
    ])

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
        dl.Map([
            dl.TileLayer(),
            *[dl.Marker(
                title=df['University'][ind],
                position={"lat": df['Latitude'][ind], "lng": df['Longitude'][ind]},
                children=[dl.Popup(children=popUpText(ind))]
            ) for ind in df.index],
        ], center=[32,0], zoom=2, style={'height':'75vh'})
    ], size="xl"
)

if __name__ == '__main__':
    app.run(debug=True)