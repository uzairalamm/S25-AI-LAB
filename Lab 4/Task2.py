graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("D", 2)],
    "C": [("E", 3)],
    "D": [("C", 2), ("E", 4)],
    "E": [("G", 7)],
    "G": []
}

givenHeuristic = {"A": 20, "B": 4, "C": 3, "D": 5, "E": 10, "G": 0}
zeroHeuristic = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "G": 0}


def findPathCost(pathList):
    totalCost = 0
    for position in range(len(pathList) - 1):
        for nextNode, edgeCost in graph[pathList[position]]:
            if nextNode == pathList[position + 1]:
                totalCost = totalCost + edgeCost
    return totalCost


def runSearch(heuristicValues, searchName):
    print("-----", searchName, "-----")
    waitingList = [(heuristicValues["A"], 0, 0, "A", ["A"])]
    expandedNodes = []
    entryNumber = 0

    while len(waitingList) > 0:
        currentEntry = min(waitingList)
        waitingList.remove(currentEntry)
        totalScore, oldEntryNumber, costSoFar, currentNode, pathSoFar = currentEntry

        if currentNode in expandedNodes:
            continue

        expandedNodes.append(currentNode)
        print("Expanded:", currentNode, "g =", costSoFar,
              "h =", heuristicValues[currentNode], "f =", totalScore)

        if currentNode == "G":
            print("Path:", pathSoFar)
            print("Cost:", costSoFar, "| summed again:", findPathCost(pathSoFar))
            print("Nodes expanded:", len(expandedNodes), expandedNodes)
            print()
            return

        for nextNode, edgeCost in graph[currentNode]:
            if nextNode not in expandedNodes:
                entryNumber = entryNumber + 1
                newCostSoFar = costSoFar + edgeCost
                newTotalScore = newCostSoFar + heuristicValues[nextNode]
                waitingList.append((newTotalScore, entryNumber, newCostSoFar,
                                    nextNode, pathSoFar + [nextNode]))


runSearch(givenHeuristic, "A* (given heuristic)")
runSearch(zeroHeuristic, "UCS (zero heuristic)")

changedHeuristic = dict(givenHeuristic)
changedHeuristic["C"] = 15
runSearch(changedHeuristic, "After Changing Heuristic Value")