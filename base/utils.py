

# Takes Marksheet object and return summary of it 
def getMarksheetSummary(marksheet):
    marks = {
        "maths": marksheet.maths,
        "computer_science": marksheet.computer_science,
        "english": marksheet.english,
        "chemistry": marksheet.chemistry,
        "physics": marksheet.physics
    }

    marks_keyPairs = list(marks.items())
    marks_keyPairs.sort(key=lambda mark: mark[1])

    highest = marks_keyPairs[-1][1]
    lowest = marks_keyPairs[0][1]

    bestSubs = list(
        map(
            lambda mark: mark[0],
            filter(
                lambda mark: mark[1] == highest, marks_keyPairs
            )
        )
    )

    worstSubs = list(
        map(
            lambda mark: mark[0],
            filter(
                lambda mark: mark[1] == lowest, marks_keyPairs
            )
        )
    )

    bestSubs = list(map(lambda sub: sub.capitalize() if sub !=
                        "computer_science" else "Computer Science", bestSubs))
    worstSubs = list(map(lambda sub: sub.capitalize() if sub !=
                         "computer_science" else "Computer Science", worstSubs))

    summary = {
        "marksheet": marksheet,
        "avg": (marksheet.maths + marksheet.computer_science + marksheet.english + marksheet.physics + marksheet.chemistry)/5,
        "highest": highest,
        "lowest": lowest,
        "bestSubs": bestSubs,
        "worstSubs": worstSubs
    }

    return summary
