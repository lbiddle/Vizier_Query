from astroquery.vizier import Vizier
import pandas as pd
from tabulate import tabulate


def get_data(fileloc,filename):
    df_data = pd.read_csv(fileloc+filename)
    targets = df_data['Target']

    return targets
fileloc = './'
filename = 'RVStandards.csv'
targets = get_data(fileloc,filename)

possible_heads = ['Vsini','vsini','v_sini','V_sini','vsin_i','Vsin_i','v_sin_i','V_sin_i','vsin(i)','Vsin(i)']

for j,target in enumerate(targets):

    print '\n------------------'+target+'------------------\n'

    results = Vizier.query_object(target)

    for i,table in enumerate(results):
        for head in possible_heads:
            if head in table.keys():
                string = results.keys()[i].encode('ascii', 'ignore')
                split_str = string.split('/')
                search_str = '/'.join(split_str[:-1])

                cat = Vizier.find_catalogs(search_str)
                cat_dict = ({k: v.description for k, v in cat.items()})
                #print({k: v.description for k, v in cat.items()})

                #print results[results.keys()[i]]

                f = open(target+'.txt', 'a+')
                f.write(string+'\n')
                #f.write(cat_dict.keys()[0].encode('ascii', 'ignore')+'\n')
                f.write(cat_dict[cat_dict.keys()[0]].encode('ascii', 'ignore')+'\n')
                f.write(tabulate(results[results.keys()[i]],headers=table.keys()))
                f.write('\n\n\n')
                f.close()

                # print ' '
                # print ' '

    print ' '
    print '------------------------------------------'
    print ' '

