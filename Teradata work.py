import pandas as pd
import numpy as np
import os
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
os.chdir('/Users/nikhilviswanath/Documents/python_data/')

project_categories= pd.read_csv('project_categories.csv')
project_export=pd.read_csv('project_export.csv')
project_inquiries=pd.read_csv('project_inquiries.csv')
project_recomm= pd.read_csv('project_recommendations.csv',low_memory=False)
sessions_data=pd.read_csv('session_export.csv')
conversions=pd.read_csv('conversions.csv')

project_categories= pd.read_csv('project_categories.csv')

project_export.shape
project_export.dtypes
data= project_export[['id','created_at','updated_at','project_category_id','state']]

data.head()

project_export.groupby(['state'])['id'].count().sort_values(ascending=False)

data.groupby(['project_category_id'])['id'].count().sort_values(ascending=False)

data[data['state']=='closed' & data['state']=='completed']

data = data.loc[(data['state'] == 'closed') | (data['state'] == 'completed')]

data.dtypes
data['created_at'] =  pd.to_datetime(data['created_at'])
data['updated_at'] =  pd.to_datetime(data['updated_at'])


data['time']=data['updated_at']-data['created_at']
data['time']= data['time'].astype(int)

data.groupby(['project_category_id'])['time'].median().sort_values(ascending=False)
data.groupby(['project_category_id'])['time'].mean().sort_values(ascending=False)

data.groupby(['project_category_id'])['time'].boxplot

data.boxplot(column='time', by='project_category_id',rot=0)

data[data['time']==1519]

data.describe()
data['time']= data['time'].astype(int)




###############################
#######   Question 2   ########
###############################












