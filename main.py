import dash

app = dash.Dash(__name__)
app.layout = dash.html.H1("Hello, world!")

if __name__ == "__main__":
    app.run(debug=False)
