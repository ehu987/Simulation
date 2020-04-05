import PredatorPrey as PP
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import plotly.graph_objects as go


def animate(x, y, n):
    fig = go.Figure(
        # initial data
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


r = PP.Rabbit(0.5)
f = PP.Fox(0.5)
r.born()
f.born()
n = 10
f_loc = np.empty([n, 2])
r_loc = np.empty([n, 2])
for i in range(n):
    if r.alive:
        f.move()
        f.target(r)
        r.move()
        f.status(i)
        PP.interact(f, r)
    f_loc[i, 0] = f.x
    f_loc[i, 1] = f.y
    r_loc[i, 0] = r.x
    r_loc[i, 1] = r.y

animate(f_loc, r_loc, n)


