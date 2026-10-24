roads = {
    "A": {"B": 2, "C": 4},
    "B": {"D": 2},
    "C": {"E": 3},
    "D": {"C": 2, "E": 4},
    "E": {"G": 7},
    "G": {}
}

heuristic = {
    "A": 20, "B": 4, "C": 3, "D": 5, "E": 10, "G": 0
}


def findRoute(h, method):
    options = [("A", 0, ["A"])]
    cheapest = {"A": 0}
    checked = []

    print("\n---", method, "---")

    while options:
        options.sort(key=lambda item: item[1] + h[item[0]])
        place, cost, route = options.pop(0)

        if cost != cheapest[place]:
            continue
        checked.append(place)
        print("Checking:", place, "| Cost:", cost, "| Priority:", cost + h[place])

        if place == "G":
            print("Route: ", " -> ".join(route))
            print("Total Cost: ", cost)
            print("Visited order: ", checked)
            print("Nodes checked: ", len(checked))
            return

        for nextPlace, distance in roads[place].items():
            newCost = cost + distance

            if newCost < cheapest.get(nextPlace, float("inf")):
                cheapest[nextPlace] = newCost
                options.append((nextPlace, newCost, route + [nextPlace]))


findRoute(heuristic, "A* Search")

noHeuristic = {node: 0 for node in roads}
findRoute(noHeuristic, "Uniform Cost Search")

modified = heuristic.copy()
modified["C"] = 15
findRoute(modified, "Modified A* search")