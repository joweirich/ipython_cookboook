import numpy as np
import pandas as pd

data={'A':['A' for idx in range(3)],'B':np.random.randint(1,10,3),'C':np.linspace(0,10,3)} 

df_data=pd.DataFrame(data)
print('Hello')
print('This is for testing of git')
print('Another change from local')
