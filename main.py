import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

import numpy as np
import math

Path = mpath.Path

background_color = '#dcd5c5'
foreground_color = '#5c5e77'

x_max = 1410
y_max = 1000
fig = plt.figure(figsize=(x_max / 50, y_max / 50))
ax = fig.add_subplot(1, 1, 1, facecolor=background_color)
plt.axis('equal')
plt.axis([-x_max, x_max, -y_max, y_max])


def transformed(data, c, r=1., t=0., rx=False, ry=False):
    (x, y) = c
    rx = rx and -1 or 1
    ry = ry and -1 or 1
    if isinstance(data, list):
        return [(x + rx * d[0] * r * math.cos(t) - ry * d[1] * r * math.sin(t),
                 y + rx * d[0] * r * math.sin(t) + ry * d[1] * r * math.cos(t))
                for d in data]
    else:
        d = data
        return (x + rx * d[0] * r * math.cos(t) - ry * d[1] * r * math.sin(t),
                y + rx * d[0] * r * math.sin(t) + ry * d[1] * r * math.cos(t))


def draw_corner(ax, center, ratio=1.):
    circ = mpatches.Circle(transformed((0, 0), center),
                           radius=80 * ratio,
                           color=foreground_color)
    ax.add_patch(circ)

    for i in range(4):
        pp = mpatches.PathPatch(Path(transformed(
            [(15, 15), (35, 35), (0, 30),
             (-35, 35), (-15, 15), (15, 15)],
            center, ratio, np.pi * i / 2),
            [Path.MOVETO, Path.LINETO, Path.CURVE3,
             Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]),
            facecolor=background_color, edgecolor=background_color)
        ax.add_patch(pp)

    for i in range(4):
        for j in (False, True):
            pp = mpatches.PathPatch(Path(transformed(
                [(0, 8), (18, 7), (18, 22),
                 (12, 45), (0, 55), (0, 10)],
                center, ratio, np.pi * i / 2, rx=j),
                [Path.MOVETO, Path.CURVE3, Path.CURVE3,
                 Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
                facecolor=background_color, edgecolor=background_color)
            ax.add_patch(pp)

    for i in (False, True):
        for j in (False, True):
            pp = mpatches.PathPatch(Path(transformed(
                [(8, 0), (7, 18), (22, 18),
                 (45, 12), (55, 0)],
                center, ratio, ry=i, rx=j),
                [Path.MOVETO, Path.CURVE3, Path.CURVE3,
                 Path.CURVE3, Path.CURVE3]),
                edgecolor=foreground_color, facecolor="none",
                linewidth=2 * ratio)
            ax.add_patch(pp)
            pp = mpatches.PathPatch(Path(transformed(
                [(19, 19), (12, 45), (0, 55)],
                center, ratio, ry=i, rx=j),
                [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                edgecolor=foreground_color, facecolor="none",
                linewidth=2 * ratio)
            ax.add_patch(pp)


def draw_text_serif(ax, x, y, s, fontsize):
    ax.text(x, y, s,
            fontsize=fontsize, fontname='freeserif', fontweight='bold',
            color=foreground_color,
            horizontalalignment='center',
            verticalalignment='center')


def draw_text_ligature(ax, x, y, s, fontsize):
    ax.text(x, y, s,
            fontsize=fontsize, fontname='Asiyah Script',
            color=foreground_color,
            horizontalalignment='center',
            verticalalignment='center')


for i in (-1, 1):
    for j in (-1, 1):
        draw_corner(ax, ((x_max - 180) * i, (y_max - 180) * j), 1.8)

draw_text_serif(ax, 0, 350, 'Certificate of Competition', 100)
draw_text_serif(ax, 0, -50, 'The second prize', 90)
draw_text_serif(ax, 0, -250, 'Liu Yihao, Qian Minjia', 60)

draw_text_ligature(ax, 0, 100, 'UMJI-SJTU Joint Institute presents the', 55)
draw_text_ligature(ax, 0, -140, 'to', 55)
draw_text_ligature(ax, 0, -350, 'In recognition of your outstanding '
                                'performance in mix double table tennis', 55)

plt.savefig('fig.png')
plt.show()
