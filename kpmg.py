import pandas as pd
df0 = pd.read_excel('KPMG.xlsx')
df0 #as there are other sheets also so output is NAN to get the specific sheet , we need to mention name of the sheet
df = pd.read_excel('KPMG.xlsx',sheet_name="Transactions")
df
df.head(6) #used to get the first n rows
df.info() #concise summary of a DataFrame
df['product_first_sold_date'] = pd.to_datetime(df['product_first_sold_date'])
df.head(6)
df['product_first_sold_date'] = pd.to_datetime(df['product_first_sold_date']).dt.date
df.head(5)
df.describe()
#checking for any null values
df.isnull()
df.isnull().sum()
df.columns
df['online_order']
df['online_order'].value_counts()
df.duplicated().sum()
df1 = pd.read_excel('KPMG.xlsx', sheet_name='NewCustomerList')
df1
df1.info()
#everything seems good for now except unnamed columns
cols = ['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']
df1=df1.drop(cols,axis=1)
df1.info()
df1.head(10)
df1.describe()
df1.isnull().sum()
df1.duplicated().sum()
df1.columns
df1['gender'].value_counts()
df1['gender']=df1['gender'].replace('U','Unspecified')
df1['gender'].value_counts()
custo=pd.read_excel('KPMG.xlsx',sheet_name='CustomerDemographic')
custo.head()
custo['default']
custo=custo.drop('default',axis=1)
custo.head()
custo.describe()
custo.isnull().sum()
custo.duplicated().sum()
custo['gender'].value_counts()
custo['gender']=custo['gender'].replace('F','Female').replace('M','Male').replace('Femal','Female').replace('U','Unspecified')
custo['gender'].value_counts()
df.head()
df1.head()
custo.head()
add=pd.read_excel('KPMG.xlsx',sheet_name='CustomerAddress')
add.head()
add.columns
add.isnull().sum()
add.duplicated().sum()
add.describe()
df.isnull().sum()
df1.isnull().sum()
custo.isnull().sum()
