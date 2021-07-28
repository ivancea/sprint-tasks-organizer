from classes import IssuesInput
import random

""" Example input JSON
{
    "users": {
        "ivancea": 5,
        "user2": 7
    },
    "issues": [
        {
            "name": "ISSUE 1",
            "users": {
                "ivancea": 2,
                "user2": 5
            }
        },
        {
            "name": "ISSUE 2",
            "users": {
                "user2": 3
            }
        },
        {
            "name": "ISSUE 3",
            "users": {
                "ivancea": 4,
                "user2": 4
            }
        }
    ]
}
"""

def random_normal_int(start, end):
    """ Generates a random integer between start and end, both inclusive, with a normal distribution """
    value = random.gauss(start+(end-start)/2, (end-start)/3)
    if value < start:
        value = start
    elif value > end:
        value = end
    return round(value)


def generate_input(min_users=1, max_users=8, min_issues=5, max_issues=30, average_user_points=random.randint(5, 20)):
    """ Generates a random IssuesInput """
    input = IssuesInput()

    for i in range(random_normal_int(min_users, max_users)):
        user = "user" + str(i)
        input.users[user] = random_normal_int(average_user_points/2, average_user_points*1.5)

    for i in range(random.randint(min_issues, max_issues)):
        issue = {
            "name": "issue" + str(i),
            "users": {}
        }
        
        average_issue_points = random.randint(1, average_user_points + 5)

        for user in random.choices(list(input.users.keys()), k=random_normal_int(0, len(input.users))):
            issue["users"][user] = random_normal_int(min(average_issue_points - 4, 1), average_issue_points + 4)

        input.issues.append(issue)

    
    return input