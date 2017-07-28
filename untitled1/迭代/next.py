import pandas as pd

#原路径和保存路径，可以根据自己要求修改
readpath = 'E:/grep/LX/len.txt'
savepath = 'E:/grep/LX/xue.txt'

pd.set_option('expand_frame_repr', False)
data = pd.read_csv(readpath, sep='\t')
for i in range(1,len(data)+1):
    data['sku'].loc[i-1] = data['sku'].loc[i-1] + '-' + str(i)
data.to_csv(savepath,sep = '\t', index=False)
print(data)

