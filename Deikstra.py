from PIL import Image, ImageDraw, ImageFont
from random import randint

videoDimensions = (1280, 720)
img = Image.new("RGB", videoDimensions, color="white")
imgDrawer = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 24)

N = 16


def weight_edge(N, X, Y):
    W = [0] * N
    for i in range(N):
        W[i] = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N):
            if randint(1, 100) < 30:
                W[i][j] = (((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5)
                W[j][i] = W[i][j]
    return W


color = [0] * N
p = [0] * N
d = [0] * N
fi = [0] * N


def new_coord_1(x, y):
    n = len(x)
    ni = int(n ** 0.5)
    nj = ni + 1
    if ni ** 2 == n:
        nj = ni
    elif ni * nj < n:
        ni = nj + 1

    a = (videoDimensions[0] - 100) // nj
    b = (videoDimensions[1] - 100) // ni

    x = 50
    y = 50
    z = 1
    for i in range(ni):
        for j in range(nj):
            print(z)
            X[z] = randint(x, x + a)
            Y[z] = randint(y, y + b)

            x = (x + a) % (videoDimensions[0] - 100);
            z = z + 1;
            if z >= n:
                return x, y
        y = y + b;


def draw_Graph(a, x, y):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i][j] != 0:
                imgDrawer.line([(x[i], y[i]), (x[j], y[j])], "black", 3)
    for i in range(1, len(x)):
        imgDrawer.ellipse([(x[i] - 20, y[i] - 20), (x[i] + 20, y[i] + 20)], "white", "black", 2);
        imgDrawer.text((x[i] - 4, y[i] - 4), str(i), (0, 0, 0), font)


def Dijkstra(W, N, start, p):
    INF = 10 ** 10
    F = [INF] * N

    F[start] = 0
    V = [True] * N
    while True:
        min_R = INF
        min_v = None
        for i in range(N):
            if V[i] and F[i] < min_R:
                min_R = F[i]
                min_v = i
        if min_v is None:
            break
        for j in range(N):
            if W[min_v][j] != 0 and F[j] > F[min_v] + W[min_v][j]:
                F[j] = F[min_v] + W[min_v][j]
                p[j] = min_v
        V[min_v] = False
    return F


def draw_way(p, finish, x, y):
    i = finish
    while i > 1:
        imgDrawer.line([(x[p[i]], y[p[i]]), (x[i], y[i])], "red", 3)
        i = p[i]
    for i in range(1, len(x)):
        imgDrawer.ellipse([(x[i] - 20, y[i] - 20), (x[i] + 20, y[i] + 20)], "white", "black", 2);
        imgDrawer.text((x[i] - 4, y[i] - 4), str(i), (0, 0, 0), font)


X = [0] * N
Y = [0] * N

new_coord_1(X, Y)
W = weight_edge(N, X, Y)
draw_Graph(W, X, Y)

p = [0] * N
color = [0] * N

FF = Dijkstra(W, N, 1, p)
print(FF)
finish = 8
draw_way(p, finish, X, Y)

img.show()