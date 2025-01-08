import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import  stats

class Assumption:
    def linear_relation(self,df):
        p1=round((len(df.columns)-1)/2)
        fig,ax=plt.subplots(p1,2,figsize=(12,18))
        ax=ax.flatten()
        for e,i in enumerate (df.columns[:-1]):
            sns.scatterplot(x=df[i],y=df.iloc[:,-1],ax=ax[e])
            plt.xlabel(i)
            plt.tight_layout
            
    def corr_(self,df):
        sns.heatmap(df.corr(),annot=True,fmt='.2g',cmap='magma')

    def Homoscedasticity(self,y_pred,res):
        plt.scatter(y_pred,res)
        plt.axhline(y=0,color='red',linestyle='--')
    def QQplot(self,res):
        fig, ax = plt.subplots(1,2,figsize=(14,4))
        stats.probplot(res.target,dist='norm',plot=ax[0]);
        ax[0].set_title('Normality of Residuals')
        sns.kdeplot(res,ax=ax[1])
        ax[1].set_title('Normal Distribution')
 

    def normality_features(self,df):
        p1=round((len(df.columns)-1)/2)
        fig,ax=plt.subplots(p1,2,figsize=(12,18))
        ax=ax.flatten()

        for e,i in enumerate (df.columns[:-1]):
            stats.probplot(df[i],dist='norm',plot=ax[e])
            ax[e].set_title(i)
            ax[e].set_xlabel('')
            plt.tight_layout
    def Auto_corelation(self,res):
        plt.plot(res)
    
        