

import re
fname='E:\lsu\data\DTI\\test.txt'
file=open(fname, 'r+', encoding='utf-8')
x = re.findall("\{fips:(.*?)\}", file.read())
print(x)


import pandas as pd
import re
fname='E:\lsu\data\DTI\hd_county_map1.txt'
file=open(fname, 'r+', encoding='utf-8')
x = re.findall("\{fips:(.*?)\}", file.read())
print(x)
a={"fipsvalue":x}
data=pd.DataFrame(a, columns=['fipsvalue'])

type(data.fipsvalue)
data2=data['fipsvalue'].str.split(',value:', expand=True)
#print(list(data2))
#data2[0].str.split('"', expand=True)
#del data3
data2.to_stata('hd_county_map.dta')