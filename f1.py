from dash import Dash, html, Input, Output, dcc
import plotly.express as px
# load dataset
df=px.data.iris()
# create dash application
app = Dash(__name__)
# define layout
app.layout=html.Div([
    html.H1("Iris Flower Analysis Dashboard"),
    html.Label("Select Flower Speies"),
    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label":"Setosa", "value":"setosa"},
            {"label":"Virginica", "value":"virginica"},
            {"label":"Versicolor", "value":"versicolor"},
        ],
        value="setosa",
        clearable=False,
    ),
    dcc.Graph(id="iris_graph"),
])
# create callback
@app.callback(
      Output("iris_graph", "figure"),
     Input("species_dropdown", "value")
)
def update_graph(selected_species):
    #filter dataset
    filtered_df = df[df["species"]==selected_species]
    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title=f"Iris Analysis:{selected_species}"
    )
    return fig
# run application
if __name__=="__main__":
    app.run(debug=True)
