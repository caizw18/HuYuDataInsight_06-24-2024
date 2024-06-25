import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

        # For undirected graph, add this line:
        # if to_node not in self.edges:
        #     self.edges[to_node] = []
        # self.edges[to_node].append((from_node, weight))


def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph.edges}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Create a graph instance
graph = Graph()

# Add edges (for an undirected graph, make sure to add both directions)
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

# Run Dijkstra's algorithm from node 'A'
distances = dijkstra(graph, 'A')

# Print the shortest distances from 'A' to all other nodes
print("Shortest distances from 'A':")
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")