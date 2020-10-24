## HOW MUCH INSERANCE

import sys
import time
import random

# -------------------- PROGRESS BAR CODE ------------------------
def updt(total, progress):

    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "■" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()

random_num = random.randint(10,60)
runs = random_num # -------------------- TIME SELECT ---------------------------


user_input = float(input("How much would it cost to re-build your house? -->"))
calc = user_input * 0.80

#  ---------------------- PROGRESS BAR -----------------------
for run_num in range(runs):
    time.sleep(.1)
    updt(runs, run_num + 1)

print("Here is your recommended insurance amount -->",calc)
