#locally
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def lowess(x, y, f, iterations):
    n = len(x)
    r = int(np.ceil(f * n))
    h = np.sort(np.abs(x - x[:, None]))[:, r]
    w = np.clip(np.abs((x[:, None] - x[None, :]) / h), 0.0, 1.0)
    w = (1 - w ** 3) ** 3
    yest = np.zeros(n)
    delta = np.ones(n)

    for _ in range(iterations):
        for i in range(n):
            weights = delta * w[:, i]
            b = [np.sum(weights * y), np.sum(weights * y * x)]
            A = [[np.sum(weights), np.sum(weights * x)],[np.sum(weights * x), np.sum(weights * x * x)]]
            beta = linalg.solve(A, b)
            yest[i] = beta[0] + beta[1] * x[i]

        residuals = y - yest
        s = np.median(np.abs(residuals))
        delta = np.clip(residuals / (6.0 * s), -1, 1)
        delta = (1 - delta ** 2) ** 2

    return yest

def main():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x) + 0.3 * np.random.randn(len(x))
    yest = lowess(x, y, f=0.25, iterations=3)

    plt.plot(x, y, "r.", label="Original Data")
    plt.plot(x, yest, "b-", label="Smoothed Data")
    plt.legend()
    plt.show()

main()
