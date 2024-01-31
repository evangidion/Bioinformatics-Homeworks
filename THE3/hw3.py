import math
import sys
import glob

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))

if __name__ == '__main__':
    pdb = sys.argv[1]
    d = sys.argv[2]
    s = sys.argv[3]
    flag = 'A'
    lines = []
    with open(pdb) as pdr:
        lines = pdr.readlines()
    for i in range(0,len(lines)):
        for j in range(i+1,len(lines)):
            if lines[i][0:6] == lines[j][0:6] == "ATOM  " and lines[i][21] == lines[j][21] and lines[i][13:15] == lines[j][13:15] == "CA":
                if lines[i][21] == flag:
                    a = lines[i][22:26].strip()
                    b = lines[j][22:26].strip()
                    if int(b) - int(a) >= int(s):
                        x1 = float(lines[i][30:38].strip())
                        y1 = float(lines[i][38:46].strip())
                        z1 = float(lines[i][46:54].strip())
                        x2 = float(lines[j][30:38].strip())
                        y2 = float(lines[j][38:46].strip())
                        z2 = float(lines[j][46:54].strip())
                        euc = distance(x1, y1, z1, x2, y2, z2)
                        if euc <= float(d):
                            print("Chain:", flag, "-->", lines[i][17:20] + '(' + a + ')', '-', lines[j][17:20] + '(' + b + ')', ':', "{:.3f}".format(euc), "Angstroms")
                else:
                    flag = lines[i][21]
                    a = lines[i][22:26].strip()
                    b = lines[j][22:26].strip()
                    if int(b) - int(a) >= int(s):
                        x1 = float(lines[i][30:38].strip())
                        y1 = float(lines[i][38:46].strip())
                        z1 = float(lines[i][46:54].strip())
                        x2 = float(lines[j][30:38].strip())
                        y2 = float(lines[j][38:46].strip())
                        z2 = float(lines[j][46:54].strip())
                        euc = distance(x1, y1, z1, x2, y2, z2)
                        if euc <= float(d):
                            print("Chain:", flag, "-->", lines[i][17:20] + '(' + a + ')', '-', lines[j][17:20] + '(' + b + ')', ':', "{:.3f}".format(euc), "Angstroms")





