import numpy as np
import plotly.graph_objects as go

def animate(x, y):
    ### animate takes in N x 2 numpy arrays of data. x tracks the path of the predator (red), and y tracks the path of the prey (blue) ###

    fig = go.Figure(
        # initial data (
        data=[go.Scatter(x=x[:, 0], y=x[:, 1], marker=dict(color="rgba(255, 0, 0, 0.5)")),
              go.Scatter(x=y[:, 0], y=y[:, 1], marker=dict(color="rgba(0,0,255, 0.5)"))
              ],

        #layout of axes
        layout=go.Layout(
            xaxis=dict(range=[-10, 10],autorange=False, zeroline=False),
            yaxis=dict(range=[-10, 10],autorange=False, zeroline=False),
            title="test",

            #initialize animation menu
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play",
                              method="animate",
                              args=[None]
                )]
            )]
        ),

        #frame data
        frames=[go.Frame(
            data=[
                go.Scatter(
                    x=[x[k, 0]],
                    y=[x[k, 1]],
                    mode="markers",
                    marker_symbol=202,
                    marker=dict(color="red", size=10)
                ),
                go.Scatter(
                    x=[y[k, 0]],
                    y=[y[k, 1]],
                    mode="markers",
                    marker_symbol=200,
                    marker=dict(color="blue", size=10)
                )]
        ) for k in range(n)]
    )

    fig.show()
