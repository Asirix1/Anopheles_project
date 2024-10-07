import pandas as pd
import numpy as np
import os 
tsv=pd.read_csv('/data/aapopov/Projects/Anopheles/fimo.tsv', sep='\t', header=None, usecols=[2,3,4,5])
plus=[]
minus=[]
def orientation_divide(data):
    if data[5] == '+':
        plus.append(np.array(data[:3]))
    else:
        minus.append(np.array(data[:3]))
tsv.apply(orientation_divide,axis=1)

plus=pd.DataFrame(plus)
minus=pd.DataFrame(minus)
f_chr = plus[0].values
f_start = plus[1].values
f_end = plus[2].values

r_chr = minus[0].values
r_start = minus[1].values
r_end = minus[2].values
print(r_start)
print(r_end)
chr1=[]
start1=[]
end1=[]
chr2=[]
start2=[]
end2=[]
for p in range(len(f_chr)):
    spaceStart = int(f_end[p]) + (5*1000)
    spaceEnd = int(f_end[p]) + (20*100*100)
    for m in range(len(r_chr)):
        if f_chr[p] == r_chr[m]:
              if spaceStart <= r_start[m] and r_end[m] <= spaceEnd:
                chr1.append(f_chr[p])
                start1.append(f_start[p])
                end1.append(f_end[p])
                chr2.append(r_chr[m])
                start2.append(r_start[m])
                end2.append(r_end[m])
pairs_dict={'chr1':chr1, 'start1':start1,'end1':end1, 'chr2':chr2, 'start2':start2, 'end2':end2}
pairs=pd.DataFrame(pairs_dict)
pairs.to_csv('/data/aapopov/Projects/Anopheles/pairs_CTCF.bedpe', header=None,sep='\t',index=False)