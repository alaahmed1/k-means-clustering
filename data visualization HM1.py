import random
import math
import matplotlib.pyplot as plt # for visualization
import time  # used to pause printing


# Calculate Euclidean distance between two points
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2) #√((x2-x1)^2 + (y2-y1)^2)


# Ask user for number of clusters
def ask_k():
    while True:
        val = input("Enter number of clusters (q to quit): ")
        if val.lower() == 'q':              # quit option
            print("Program exited.")
            exit()
        if val.isdigit() and int(val) > 0:  # valid positive integer
            return int(val)
        print("Enter a valid positive number.")


def manual_input(min_points): # for manual point entry
    points = []
    print(f"\nEnter points as x y (minimum {min_points}). Type 'done' to finish.")

    while True:
        entry = input("Point: ")
        if entry.lower() == 'done':          # stop input
            if len(points) < min_points:    # ensure enough points
                print("Not enough points.")
                continue
            return points
        try:
            x, y = map(float, entry.split())  # convert input to floats and split the add to the list
            points.append([x, y])
        except:
            print("Invalid format.")


def random_input(n): # Random point generation (prints points one by one with pause)
    points = []
    print("\nGenerated points:")

    for _ in range(n): #looping depends on no. of requested points
        p = [random.uniform(0, 100), random.uniform(0, 100)] #choosing random x and y
        points.append(p)  # storing points in the list
        print(p)          # print one point
        time.sleep(0.5)   # pause between prints

    return points


def get_points(min_points):
    while True:# Choice of input method that user prefers
        choice = input("1) Random points  2) Manual input: ")
        if choice == '1':
            try:
                n = int(input(f"Number of points (>= {min_points}): "))
                if n >= min_points:
                    return random_input(n)
            except:
                pass
            print("Invalid number.")
        elif choice == '2':
            return manual_input(min_points)
        else:
            print("Choose 1 or 2.")


# Select initial centroids randomly from points
def select_centroids(points, k):
    return random.sample(points, k)


# Assign each point to the nearest centroid
def assign(points, centroids):
    clusters = [[] for _ in centroids]        # empty clusters
    for p in points: #go through each data point
        dists = [distance(p, c) for c in centroids] #calculate distance between each point to every centroid
        clusters[dists.index(min(dists))].append(p) #store in the the list "dists"
    return clusters


# Recalculate centroids as mean of clusters
def recenter(clusters, points):
    centroids = [] # empty list to store new centroids
    for cluster in clusters:
        if not cluster:                       # empty cluster case
            centroids.append(random.choice(points))
        else: #compute average of points and add to centroid list
            x = sum(p[0] for p in cluster) / len(cluster)
            y = sum(p[1] for p in cluster) / len(cluster)
            centroids.append([x, y])
    return centroids

def draw(clusters, centroids, it):  # visualizing current iteration
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'orange']  # colors for clusters
    plt.clf()  # clear previous plot

    for i, cluster in enumerate(clusters):  # loop through each cluster
        col = colors[i % len(colors)]  # select color for current cluster

        if cluster:  # check cluster is not empty
            xs = [p[0] for p in cluster]  # separate x values
            ys = [p[1] for p in cluster]  # separate y values
            plt.scatter(xs, ys, color=col, edgecolor='k',
                        alpha=0.6, label=f"Cluster {i+1}")  # plot cluster points

        plt.scatter(centroids[i][0], centroids[i][1],  # plot centroid
                    marker='X', s=200, color=col, edgecolor='k')

    plt.scatter([], [], marker='X', color='black', s=200,
                label='Centroids')  # add centroid to legend

    plt.title(f"K-means Clustering - Iteration {it}")  # set plot title
    plt.xlabel("X")  # label x-axis
    plt.ylabel("Y")  # label y-axis
    plt.grid(True)  # add grid lines

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # show legend on the side
    plt.pause(1)  # pause for visualization


# Main K-means function
def run_kmeans():
    print("=== K-Means Clustering ===")

    k = ask_k() # number of clusters
    points = get_points(k) # get data points
    centroids = select_centroids(points, k) # initial centroids
    iteration = 1

    plt.ion() # interactive plotting
    plt.figure(figsize=(10, 6)) #opens graph window of medium size

    while True:
        clusters = assign(points, centroids)     # expectation step
        new_centroids = recenter(clusters, points)  # maximization step

        print(f"\nIteration {iteration}") #print current iteration
        for i, c in enumerate(clusters): #loops through clusters and prints all points assigned to each cluster
            print(f"Cluster {i+1}: {c}")
        print("Centroids:", new_centroids) # prints updated centroid positions

        draw(clusters, new_centroids, iteration) #viualize points and centroids using matplotlib

        # check convergence
        if all(distance(c, n) < 1e-4 for c, n in zip(centroids, new_centroids)):
            print("\nConverged!")
            break #stopping the loop after convergence

        centroids = new_centroids #update centroid
        iteration += 1 #move to the next iteration

    plt.ioff() #turn off matplotlib interactive mode
    plt.show() #display final plot window

    print("\nFinal centroids:", centroids) #prints final centroid positions after convergence

# Run program
run_kmeans()