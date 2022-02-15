# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

false = False
true = True

fig = {
    "data":[{
        "x": [0, 1],
        "y": [0, 1.414],
        "text": ["Hx+yH", "H\\sqrt{2}H"],
        "mode": "text+markers",
        "name": "$E^2=m^2c^4+p^2c^2$"
    }, {
        "x": [0, 1],
        "y": [1.4, 0.1],
        "text": ["H1.400 \\pm 0.023H", "H0.100 \\pm 0.002H"],
        "type": "bar",
        "name": "$x=\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$"
    }, {
        "type": "pie",
        "values": [1, 9],
        "labels": ["$\\frac{1}{10}=10\\%$", "$\\frac{9}{10}=90\\%$"],
        "textinfo": "label",
        "domain": {"x": [0.3, 0.75], "y": [0.55, 1]}
    }, {
        "type": "heatmap",
        "z": [[1,2],[3,4]],
        "xaxis": "x2",
        "yaxis": "y2",
        "colorbar": {"title": {"text": "He^{i\\pi}=-1H"}, "y": 0.225, "len": 0.45}
    }],
    "layout": {
        "yaxis":{"domain": [0, 0.45], "title": {"text": "$y=\\sin{2 \\theta}$"}},
        "xaxis":{
            "domain": [0, 0.45],
            "title": {"text": "$x=\\int_0^a a^2+1$"},
            "tickvals": [0, 1],
            "ticktext": ["$\\frac{0}{100}$", "$\\frac{100}{100}$"]
        },
        "xaxis2": {"domain": [0.85, 1], "anchor": "y2"},
        "yaxis2": {
            "domain": [0, 0.45],
            "anchor": "x2",
            "tickvals": [0, 1],
            "ticktext": ["Ha+b+c+dH", "He+f+g+hH"],
            "title": {"text": "$(||01\\rangle+|10\\rangle)/\\sqrt2$"}
        },
        "height":500,
        "width":800,
        "margin": {"r": 250},
        "title": {"text": "$i\\hbar\\frac{d\\Psi}{dt}=-[V-\\frac{-\\hbar^2}{2m}\\nabla^2]\\Psi$"},
        "annotations":[
            {
                "text": "H is substituted for $<br>where we would like<br>math but do not yet<br>fully support it",
                "xref": "paper", "yref": "paper",
                "x": 1.2, "xanchor": "left", "y": 0, "yanchor": "bottom",
                "showarrow": false
            },
            {
                "text":"$(top,left)$","showarrow":false,"xref":"paper","yref":"paper",
                "xanchor":"left","yanchor":"top","x":0,"y":1,"textangle":10,
                "bordercolor":"#0c0","borderpad":3,"bgcolor":"#dfd"
            },
            {
                "text":"$(right,bottom)$","xref":"paper","yref":"paper",
                "xanchor":"right","yanchor":"bottom","x":0.2,"y":0.7,"ax":-20,"ay":-20,
                "textangle":-30,"bordercolor":"#0c0","borderpad":3,"bgcolor":"#dfd",
                "opacity":0.5
            },
            {"text":"$not-visible$", "visible": false},
            {
                "text":"$^{29}Si$","x":0.7,"y":0.7,"showarrow":false,
                "xanchor":"right","yanchor":"top"
            },
            {
                "text":"$^{17}O$","x":0.7,"y":0.7,"ax":15,"ay":-15,
                "xanchor":"left","yanchor":"bottom"
            }
        ]
    }
}

app.layout = html.Div(children=[

    html.H1(children='Apple: $2, Orange: $3'),

    # dcc.Markdown('## This is an <h2> tag with MathJax: $E=mc^2$', mathjax=True),

    dcc.Graph(
        mathjax=True,
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
