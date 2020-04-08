import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def animate(x, y, title, xlim, ylim):
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
            xaxis=dict(range=[-xlim, xlim],autorange=False, zeroline=False),
            yaxis=dict(range=[-ylim, ylim],autorange=False, zeroline=False),
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

def multi_animate(x, y, title):
    ### animate takes in N x 2 numpy arrays of data. x tracks the path of the predator (red), and y tracks the path of the prey (blue) ###
    n = len(x)
    sizes = [len(x[k]) for k in range(10)]
    x_all = np.vstack(x)
    y_all = np.vstack(y)
    xlim = np.max(x_all) + 5
    ylim = np.max(y_all) + 5
    fig = go.Figure(
        # initial data
        data=[go.Scatter(x=x_all[:, 0], y=x_all[:, 1], marker=dict(color="rgba(255, 0, 0, 0.5)")),
              go.Scatter(x=y_all[:, 0], y=y_all[:, 1], marker=dict(color="rgba(0,0,255, 0.5)")),
              go.Scatter(x=x_all[:, 0], y=x_all[:, 1], marker=dict(color="rgba(255, 0, 0, 0.5)")),
              go.Scatter(x=y_all[:, 0], y=y_all[:, 1], marker=dict(color="rgba(0,0,255, 0.5)"))
              ],
        # config axes
        layout=go.Layout(
            xaxis=dict(range=[-xlim, xlim], autorange=False, zeroline=False),
            yaxis=dict(range=[-ylim, ylim], autorange=False, zeroline=False),
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
                    x=[x[j][k, 0]], y=[x[j][k, 1]],
                    mode="markers", marker_symbol=202,
                    marker=dict(color="red", size=10)
                ),
                go.Scatter(
                    x=[y[j][k, 0]], y=[y[j][k, 1]], # prey data
                    mode="markers", marker_symbol=200,
                    marker=dict(color="blue", size=10)
                ),
                go.Scatter(
                    x=x[j][:, 0], y=x[j][:, 1],  # predator trace
                    mode="lines",
                    line=dict(color="rgba(255,0,0,0.5)", width=1)
                ),
                go.Scatter(
                    x=y[j][:, 0], y=y[j][:, 1],  # prey trace
                    mode="lines",
                    line=dict(color="rgba(0,0,255,0.5)", width=1)
                )
            ], traces=[0, 1, 2, 3]
        ) for j in range(n) for k in range(sizes[j])]
    )
    fig.show()

