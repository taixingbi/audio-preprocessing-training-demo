import pandas as pd 
import glob
import numpy as np
from sklearn.model_selection import train_test_split


def collect_data(path, label, n= False):
    print("\n---------------", path, label,"---------------")
    filenames= glob.glob(path + '*.csv')
    l=[]
    for filename in filenames:
        df= pd.read_csv(filename) 
        l.append(df.to_numpy())
    x = np.array(l)

    #select ramdon n sets
    if n:
        idx = np.random.randint(len(x), size=n)
        # print(idx)
        x= x[idx,:]

    #norm
    x = x / np.linalg.norm(x)
    
    #float32 to float16
    x= x.astype(np.float16)

    # label
    y=  np.array( len(x)* [label])
    # print(x.shape, len(x))

    return x, y

def load_data():
    path= '../data/1-308_AUDIO/spectrograms/' 
    x_1, y_1= collect_data(path, 1)

    path= '../data/0-300_AUDIO/spectrograms/' 
    x_0, y_0= collect_data(path, 0, 16)

    x= np.concatenate((x_1, x_0))
    y= np.concatenate((y_1, y_0))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

    print("x_train.shape", x_train.shape)
    print("y_train.shape", y_train.shape)
    print("x_test.shape", x_test.shape)
    print("y_test.shape", y_test.shape)

    return (x_train, y_train), (x_test, y_test)

if __name__=="__main__":
    (x_train, y_train), (x_test, y_test)= load_data()
    print("done")
