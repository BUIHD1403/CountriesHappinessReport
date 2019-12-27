import pandas as pd
import numpy as np

def main():
                #Read then combine happiness data for 2015, 2016, 2017
                #Read Happiness data for 2015
        happiness2015=pd.read_csv('Happiness2015.csv')
        happiness2015['Year'] = 2015
        happiness2015= happiness2015[['Country', 'Happiness Score','Trust (Government Corruption)','Year']]
                #Rename column name for union purpose
        happiness2015['Government Trust']=happiness2015['Trust (Government Corruption)']
        del happiness2015['Trust (Government Corruption)']
                #Re-order column name for merging purpose
        happiness2015= happiness2015[['Country', 'Happiness Score','Government Trust','Year']]

                #Read Happiness data for 2016
        happiness2016=pd.read_csv('Happiness2016.csv')
        happiness2016['Year'] = 2016
        happiness2016= happiness2016[['Country', 'Happiness Score','Trust (Government Corruption)','Year']]
                #Rename column name for union purpose
        happiness2016['Government Trust']=happiness2016['Trust (Government Corruption)']
        del happiness2016['Trust (Government Corruption)']
                #Re-order column name for merging purpose
        happiness2016= happiness2016[['Country', 'Happiness Score','Government Trust','Year']]

                #Read Happiness data for 2017
        happiness2017=pd.read_csv('Happiness2017.csv')
        happiness2017['Year'] = 2017
        happiness2017= happiness2017[['Country', 'Happiness.Score','Trust..Government.Corruption.','Year']]
                #Rename column name for union purpose
        happiness2017['Happiness Score']=happiness2017['Happiness.Score']
        happiness2017['Government Trust']=happiness2017['Trust..Government.Corruption.']
        del happiness2017['Trust..Government.Corruption.']
        del happiness2017['Happiness.Score']
                #Re-order column name for merging purpose
        happiness2017= happiness2017[['Country', 'Happiness Score','Government Trust','Year']]

                #Read United Nations data: Health, Education, HDI, GINI
                # Read csv file but skip the first row which is the header
        healthExpense=pd.read_csv("Current health expenditure (% of GDP).csv", skiprows=1, encoding='iso-8859-1')
        educationExpense=pd.read_csv("Government expenditure on education (% of GDP).csv", skiprows=1, encoding='iso-8859-1')
        hdi=pd.read_csv("Human Development Index (HDI).csv", skiprows=1, encoding='iso-8859-1')
        gini=pd.read_csv("Income inequality, Gini coefficient.csv", skiprows=1, encoding='iso-8859-1')
        secondaryEducation=pd.read_csv("Population with at least some secondary education (% ages 25 and older).csv", skiprows=1, encoding='iso-8859-1')

                #Removce Unamed (empty) column
        healthExpense = healthExpense.loc[:, ~healthExpense.columns.str.contains('^Unnamed')]
        educationExpense = educationExpense.loc[:, ~educationExpense.columns.str.contains('^Unnamed')]
        hdi = hdi.loc[:, ~hdi.columns.str.contains('^Unnamed')]
        gini = gini.loc[:, ~gini.columns.str.contains('^Unnamed')]
        secondaryEducation = secondaryEducation.loc[:, ~secondaryEducation.columns.str.contains('^Unnamed')]

                #Exclude rows for labelling
        healthExpense = healthExpense[healthExpense['HDI Rank'].str.contains('^[0-9]+$', na=False)]
        educationExpense = educationExpense[educationExpense['HDI Rank'].str.contains('^[0-9]+$', na=False)]
        gini = gini[gini['HDI Rank'].str.contains('^[0-9]+$', na=False)]
        secondaryEducation = secondaryEducation[secondaryEducation['HDI Rank'].str.contains('^[0-9]+$', na=False)]

                #Exclude rows which has 'HDI Rank' as Nan
        hdi = hdi[np.isfinite(hdi['HDI Rank'])]

        #print(hdi.dtypes)
        #hdi['HDI Rank'] = hdi['HDI Rank'].astype(object)
        #hdi = hdi[hdi['HDI Rank'].str.contains('^[0-9]+$', na=False)]

        print("Done")

if __name__ == '__main__':
    main()