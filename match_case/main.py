# Given grade = "B", write a match-case statement to handle the string values "A", "B", "C", and "F". Print "Excellent", "Good", "Average", and "Fail" respectively.

grade = "B"

match (grade):
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Fail")

# Given command = "start", use match-case with OR patterns (|) so that both "start" and "begin" print "System Starting", while "stop" and "halt" print "System Stopping"

command = "start"

match command:
    case "start" | "begin":
        print("System Starting")
    case "stop" | "halt":
        print("System Stopping")

# Given status_code = 404, write a match-case statement that prints "OK" for 200, "Not Found" for 404, "Server Error" for 500, and "Unknown Status" as the default case using the wildcard _.
status_code = 100

match status_code:
    case 200:
        print("OK")
    case 404:
        print("NOT FOUND")
    case 500:
        print("SERVER ERROR")
    case _:
        print("UNKNOWN STATUS")

