# K-Means Clustering – Built from Scratch

A K-Means clustering algorithm implemented from scratch in Python using only standard libraries. No scikit-learn. The algorithm runs iteratively, visualizes each step in real time, and stops automatically when it converges.

Built as part of the Data Visualization and Analysis course at the German University of Technology in Oman (GUtech).

---

## What It Does

- Asks the user to choose the number of clusters (K)
- Accepts either randomly generated points or manually entered coordinates
- Runs the K-Means loop: assign points to nearest centroid, recalculate centroids, repeat
- Visualizes each iteration live using matplotlib
- Stops when centroids no longer move (convergence)

---

## How It Works

The algorithm follows the standard K-Means steps:

1. **Initialize** – Select K random points as starting centroids
2. **Assign** – Each point is assigned to the nearest centroid using Euclidean distance
3. **Recenter** – Centroids are recalculated as the mean of all points in their cluster
4. **Repeat** – Steps 2 and 3 repeat until centroids converge (movement < 0.0001)

Euclidean distance formula used:

```
d = √((x2 - x1)² + (y2 - y1)²)
```

---

## Tools & Libraries

| Library | Purpose |
|---|---|
| `math` | Euclidean distance calculation |
| `random` | Random point generation and centroid initialization |
| `matplotlib` | Real-time cluster visualization |
| `time` | Pause between printed points for readability |

No external ML libraries used.

---

## How to Run

1. Clone the repository
```bash
git clone https://github.com/alaahmed1/kmeans-clustering.git
```

2. Make sure Python is installed (3.7+) and matplotlib is available
```bash
pip install matplotlib
```

3. Run the script
```bash
python data_visualization_HM1.py
```

4. Follow the prompts:
   - Enter number of clusters
   - Choose random or manual point input
   - Watch the algorithm visualize each iteration

---

## Input Options

**Random points** – You specify how many points to generate. The program places them randomly in a 0–100 coordinate space and prints each one as it is created.

**Manual input** – You type each point as `x y` (e.g. `30 45`). Type `done` when finished. Minimum points required equals the number of clusters chosen.

---

## Example Output

```
=== K-Means Clustering ===
Enter number of clusters (q to quit): 3
1) Random points  2) Manual input: 1
Number of points (>= 3): 20

Iteration 1
Cluster 1: [[12.4, 55.1], [18.9, 60.2], ...]
Cluster 2: [[80.3, 22.1], [75.6, 18.4], ...]
Cluster 3: [[45.1, 90.3], [50.2, 85.7], ...]
Centroids: [[16.2, 58.4], [77.9, 20.1], [47.8, 88.3]]

...

Converged!
Final centroids: [[15.8, 57.9], [78.1, 19.8], [48.2, 87.6]]
```

---

## Author

**Alaa Ahmed Alrashdi**  
Computer Science Student, German University of Technology in Oman  
[LinkedIn](https://www.linkedin.com/in/alaa-ahmed-55b7a7295) | [GitHub](https://github.com/alaahmed1)
