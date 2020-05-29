# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
better_event=data['Better_Event'].value_counts().index[0]



# --------------
#Code starts here
def top_ten(top_countries,cname):
    country_list=[]
    t=top_countries.nlargest(10,cname)
    country_list.extend(t['Country_Name'])
    return country_list

top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(index=len(top_countries)-1,axis=0,inplace=True)
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
plt.figure(figsize=[14,8])
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.figure(figsize=[14,8])
plt.bar(summer_df['Country_Name'],winter_df['Total_Summer'])
plt.figure(figsize=[14,8])
plt.bar(summer_df['Country_Name'],top_df['Total_Summer'])


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].values[0]


# --------------
#Code starts here
data_1=data.drop(index=len(data)-1,axis=0)
data_1['Total_Points']=3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']
most_points=max(data_1['Total_Points'])
best_country=data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True,rot=45)
plt.xlabel('United States')
plt.ylabel('Medals Tally')


