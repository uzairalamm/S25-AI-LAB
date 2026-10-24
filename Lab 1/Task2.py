def checkScholarship(score, documentsComplete,
                     attendancePercent, enrollmentVerified):

    if score < 70:
        return "Hold", "Score is below 70"

    if not documentsComplete:
        return "Hold", "Documents are incomplete"

    if attendancePercent < 75:
        return "Hold", "Attendance is below 75%"

    if not enrollmentVerified:
        return "Hold", "Enrollment is not verified"

    return "Review", "All conditions are satisfied"


testCases = [
    {
        "name": "Case 1: All conditions pass",
        "score": 80,
        "documentsComplete": True,
        "attendancePercent": 85,
        "enrollmentVerified": True,
        "expected": "Review"
    },
    {
        "name": "Case 2: Attendance failure",
        "score": 80,
        "documentsComplete": True,
        "attendancePercent": 60,
        "enrollmentVerified": True,
        "expected": "Hold"
    },
    {
        "name": "Case 3: Enrollment failure",
        "score": 80,
        "documentsComplete": True,
        "attendancePercent": 85,
        "enrollmentVerified": False,
        "expected": "Hold"
    },
    {
        "name": "Case 4: Score boundary",
        "score": 70,
        "documentsComplete": True,
        "attendancePercent": 75,
        "enrollmentVerified": True,
        "expected": "Review"
    }
]


for test in testCases:
    actual, reason = checkScholarship(
        test["score"],
        test["documentsComplete"],
        test["attendancePercent"],
        test["enrollmentVerified"]
    )
    print("\n", test["name"])
    print("Input:", 
          test["score"], 
          test["documentsComplete"],
          test["attendancePercent"], 
          test["enrollmentVerified"])
    print("Expected:", test["expected"])
    print("Actual:", actual)
    print("Reason:", reason)