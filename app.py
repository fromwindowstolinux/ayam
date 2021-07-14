import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

data = pd.read_csv("ayam.csv")
# data = data.query("fastfood == 'select' and state == 'select'")
data["Date"] = pd.to_datetime(data["Date"], format = "%Y-%m-%d")
data.sort_values("Date", inplace = True)

app = dash.Dash(__name__)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Your Ciken Data!"

html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children="state", className="menu-title"),
                dcc.Dropdown(
                    id="state-filter",
                    options=[
                        {"label": state, "value": state}
                        for region in np.sort(data.region.unique())
                    ],
                    value="state",
                    clearable=False,
                    className="dropdown",
                ),
            ]
        ),
        html.Div(
            children=[
                html.Div(children="fastfood", className="menu-title"),
                dcc.Dropdown(
                    id="fastfood-filter",
                    options=[
                        {"label": fastfood_type, "value": fastfood_type}
                        for fastfood_type in data.type.unique()
                    ],
                    value="fastfood",
                    clearable=False,
                    searchable=False,
                    className="dropdown",
                ),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children="Date Range",
                    className="menu-title"
                    ),
                dcc.DatePickerRange(
                    id="date-range",
                    min_date_allowed=data.Date.min().date(),
                    max_date_allowed=data.Date.max().date(),
                    start_date=data.Date.min().date(),
                    end_date=data.Date.max().date(),
                ),
            ]
        ),
    ],
    className="menu",
),

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🍗", className="header-emoji"),
                html.H1(
                    children="Ayam Anal", className="header-title"
                ),
                html.P(
                    children="An analysis of the most famous fried chicken",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Total_Sales"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Fried Chicken Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True,},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className = "wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server()