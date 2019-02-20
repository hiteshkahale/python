from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems to be little odd.")
    else:
        print("Not an odd minute.")
