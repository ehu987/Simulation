import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def animate(x, y, title):
    ### animate takes in N x 2 numpy arrays of data. x tracks the path of the predator (red), and y tracks the path of the prey (blue) ###
    n = np.size(x, 0)

    fig = go.Figure(
        # initial data
        data=[go.Scatter(x=x[:, 0], y=x[:, 1], marker=dict(color="rgba(255, 0, 0, 0.5)")),
              go.Scatter(x=y[:, 0], y=y[:, 1], marker=dict(color="rgba(0,0,255, 0.5)")),
              go.Scatter(x=x[:, 0], y=x[:, 1], marker=dict(color="rgba(255, 0, 0, 0.5)")),
              go.Scatter(x=y[:, 0], y=y[:, 1], marker=dict(color="rgba(0,0,255, 0.5)"))
              ],
        # config axes
        layout=go.Layout(
            xaxis=dict(range=[-10, 10],autorange=False, zeroline=False),
            yaxis=dict(range=[-10, 10],autorange=False, zeroline=False),
            title=title,
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play", method="animate", args=[None])]
            )]
        ),
        # config frames
        frames=[go.Frame(
            data=[
                go.Scatter( # predator data
                    x=[x[k, 0]], y=[x[k, 1]],
                    mode="markers", marker_symbol=202,
                    marker=dict(color="red", size=10)
                ),
                go.Scatter(
                    x=[y[k, 0]], y=[y[k, 1]], # prey data
                    mode="markers", marker_symbol=200,
                    marker=dict(color="blue", size=10)
                ),
                go.Scatter(
                    x=x[:, 0], y=x[:, 1],  # predator trace
                    mode="lines",
                    line=dict(color="rgba(255,0,0,0.5)", width=1)
                ),
                go.Scatter(
                    x=y[:, 0], y=y[:, 1],  # prey trace
                    mode="lines",
                    line=dict(color="rgba(0,0,255,0.5)", width=1)
                )
            ], traces=[0,1,2,3]
        ) for k in range(n)]
    )

    fig.show()


def make_layout():
    return [dict(
                type="buttons",
                buttons=[dict(label="Play", method="animate", args=[None])]
            )]


def make_frames(data1, data2):
    n = np.size(data1, 0)
    return [dict(
        data=[go.Scatter(x=[data1[k, 0]], y=[data1[k, 1]],
                         mode="markers", marker_symbol=202,
                         marker=dict(color="red", size=10)),
              go.Scatter(x=[data2[k, 0]], y=[data2[k, 1]],
                         mode="markers", marker_symbol=200,
                         marker=dict(color="blue", size=10)),
              go.Scatter(x=data1[:, 0], y=data1[:, 1],
                         mode="lines",
                         line=dict(color="rgba(255,0,0,0.5)", width=1)),
              go.Scatter(x=data2[:, 0], y=data2[:, 1],
                         mode="lines",
                         line=dict(color="rgba(0,0,255,0.5)", width=1)),
              go.Heatmap(z=[[1, 2],
                            [2, 1]],
                         x=['fast action', 'slow action'],
                         y=['unaware state', 'aware state'])
              ],
        traces=[0,1,2,3,4]
    ) for k in range(n)]


def animate2(data1, data2):
    fig = make_subplots(rows=1, cols=2, subplot_titles=('World', 'Fox Brain'))
    fig.add_scatter(x=data1[:, 0], y=data1[:, 1], mode="lines", line=dict(color="red"), row=1, col=1)
    fig.add_scatter(x=data2[:, 0], y=data2[:, 1], mode="lines", line=dict(color="blue"), row=1, col=1)
    fig.add_scatter(x=data1[:, 0], y=data1[:, 1], mode="lines", line=dict(color="red"), row=1, col=1)
    fig.add_scatter(x=data2[:, 0], y=data2[:, 1], mode="lines", line=dict(color="blue"), row=1, col=1)
    fig.add_heatmap(z=[[1,2],
                       [1,2]],
                    x=['fast action', 'slow action'],
                    y=['unaware state', 'aware state'],
                    row=1, col=2
                    )
    fig.update(frames=make_frames(data1, data2))
    fig.update_layout(updatemenus=make_layout())
    fig.update_xaxes(range=[-5, 5], autorange=False, row=1, col=1)
    fig.update_yaxes(range=[-5, 5], autorange=False, row=1, col=1)
    fig.show()
