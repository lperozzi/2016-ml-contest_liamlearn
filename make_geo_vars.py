import pandas as pd
import numpy as np

def make_rolling_marine_ratio_vars(wells_df, windows):

    grouped = wells_df.groupby(['Well Name'])
    new_var = pd.DataFrame()
    for key in grouped.groups.keys():

        depth = grouped.get_group(key)['Depth']
        temp_df = pd.DataFrame()
        temp_df['Depth'] = depth
        NM_M = grouped.get_group(key)['NM_M']

        for window in windows:

            temp_df['Depth'] = grouped.get_group(key)['Depth']
            temp_df['Well Name'] = [key for _ in range(len(NM_M))]
            temp_df['NM_M'] = grouped.get_group(key)['NM_M']
            #We initialize a new variable
            temp_df['Marine_ratio_' + str(window) + '_centered'] = pd.rolling_mean(arg=temp_df['NM_M'], window=window, min_periods=1, center=True)

        temp_df['Well Name'] = [key for _ in range(len(temp_df['Depth']))]
        new_var = new_var.append(temp_df)


    new_var = new_var.sort_index()
    new_var =new_var.drop(['Well Name','Depth','NM_M'],axis=1)
    return pd.concat([wells_df, new_var],axis=1)

def make_distance_to_M_up_vars(wells_df):
    grouped = wells_df.groupby(['Well Name'])
    new_var = pd.DataFrame()

    for key in grouped.groups.keys():

        NM_M = grouped.get_group(key)['NM_M'].values

        #We create a temporary dataframe that we reset for every well
        temp_df = pd.DataFrame()
        temp_df['Depth'] = grouped.get_group(key)['Depth']
        temp_df['Well Name'] = [key for _ in range(len(NM_M))]
        #We initialize a new variable
        dist_mar_up = np.zeros(len(NM_M))

        # A variable counting the interval from the ipper marine deposit
        # We initialize it to -99999 since we do not know what's abpve the first log
        count = -99999

        for i in range(len(NM_M)):

            if ((NM_M[i] == 1) & (count>-99999)):

                count+=0.5
                dist_mar_up[i] += count

            elif NM_M[i] == 2:

                count=0

            else:
                dist_mar_up[i] = count

        temp_df['dist_M_up'] = dist_mar_up

        # We append each well variable to a larger dataframe
        # We use a dataframe to preserve the index
        new_var = new_var.append(temp_df)

    new_var = new_var.sort_index()
    new_var =new_var.drop(['Well Name','Depth'],axis=1)
    return pd.concat([wells_df, new_var],axis=1)

def make_distance_to_M_down_vars(wells_df):
    grouped = wells_df.groupby(['Well Name'])
    new_var = pd.DataFrame()

    for key in grouped.groups.keys():

        NM_M = grouped.get_group(key)['NM_M'].values

        temp_df = pd.DataFrame()
        temp_df['Depth'] = grouped.get_group(key)['Depth']
        temp_df['Well Name'] = [key for _ in range(len(NM_M))]

        dist_mar_down = np.zeros(len(NM_M))
        count = -99999

        for i in range(len(NM_M)-1,-1,-1):

            if ((NM_M[i] == 1) & (count>-99999)):

                count+=0.5
                dist_mar_down[i] += count

            elif NM_M[i] == 2:
                count=0

            else:
                dist_mar_down[i] = count

        temp_df['dist_M_down'] = dist_mar_down

        new_var = new_var.append(temp_df)

    new_var = new_var.sort_index()
    new_var =new_var.drop(['Well Name','Depth'],axis=1)
    return pd.concat([wells_df, new_var],axis=1)

def make_distance_to_NM_up_vars(wells_df):
    grouped = wells_df.groupby(['Well Name'])
    new_var = pd.DataFrame()

    for key in grouped.groups.keys():

        NM_M = grouped.get_group(key)['NM_M'].values

        #We create a temporary dataframe that we reset for every well
        temp_df = pd.DataFrame()
        temp_df['Depth'] = grouped.get_group(key)['Depth']
        temp_df['Well Name'] = [key for _ in range(len(NM_M))]
        #We initialize a new variable
        dist_mar_up = np.zeros(len(NM_M))

        # A variable counting the interval from the ipper marine deposit
        # We initialize it to -99999 since we do not know what's abpve the first log
        count = -99999

        for i in range(len(NM_M)):

            if ((NM_M[i] == 2) & (count>-99999)):

                count+=0.5
                dist_mar_up[i] += count

            elif NM_M[i] == 1:

                count=0

            else:
                dist_mar_up[i] = count

        temp_df['dist_NM_up'] = dist_mar_up

        # We append each well variable to a larger dataframe
        # We use a dataframe to preserve the index
        new_var = new_var.append(temp_df)

    new_var = new_var.sort_index()
    new_var =new_var.drop(['Well Name','Depth'],axis=1)
    return pd.concat([wells_df, new_var],axis=1)

def make_distance_to_NM_down_vars(wells_df):
    grouped = wells_df.groupby(['Well Name'])
    new_var = pd.DataFrame()

    for key in grouped.groups.keys():

        NM_M = grouped.get_group(key)['NM_M'].values

        temp_df = pd.DataFrame()
        temp_df['Depth'] = grouped.get_group(key)['Depth']
        temp_df['Well Name'] = [key for _ in range(len(NM_M))]

        dist_mar_down = np.zeros(len(NM_M))
        count = -99999

        for i in range(len(NM_M)-1,-1,-1):

            if ((NM_M[i] == 2) & (count>-99999)):

                count+=0.5
                dist_mar_down[i] += count

            elif NM_M[i] == 1:
                count=0

            else:
                dist_mar_down[i] = count

        temp_df['dist_NM_down'] = dist_mar_down

        new_var = new_var.append(temp_df)

    new_var = new_var.sort_index()
    new_var =new_var.drop(['Well Name','Depth'],axis=1)
    return pd.concat([wells_df, new_var],axis=1)
