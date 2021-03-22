import glob
import os

names = glob.glob("K*.jpg")

for n in names:
    os.system('mv ' + str(n) + ' ' + n.replace('K','10'))
