from dash import Dash , html

#create dashboard application
app =Dash(__name__)

#define dashboard layout
app.layout = html.Div([
    html.H1("Welcome to python Dash"),
    html.P("My first Interactive Dashboard"),
    html.H2("Learning Dash Framework")
])

#step 3 : Run application
if __name__ == "__main__":
   app.run(debug=True)
