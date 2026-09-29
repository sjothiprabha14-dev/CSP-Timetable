subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

def is_valid(subject, slot, assignment):
    for s1, s2 in constraints:
        if subject == s1 and s2 in assignment:
            if assignment[s2] == slot:
                return False

        if subject == s2 and s1 in assignment:
            if assignment[s1] == slot:
                return False

    return True


def backtrack(assignment):
    if len(assignment) == len(subjects):
        return assignment

    subject = next(s for s in subjects if s not in assignment)

    for slot in time_slots:
        if is_valid(subject, slot, assignment):
            assignment[subject] = slot

            result = backtrack(assignment)

            if result is not None:
                return result

            del assignment[subject]

    return None


solution = backtrack({})

print("Final Timetable")
print("--------------------------")

for subject in subjects:
    print(f"{subject:8} -> {solution[subject]}")

print("--------------------------")
print("All constraints are satisfied.")