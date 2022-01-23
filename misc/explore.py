# """
# Explore Dataset and Report Stats  [MS]
# """


import pandas as pd
from scipy import stats
import numpy as np



def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    # Read Datasets (Step 1)
    df_charges = pd.read_csv(charges_data_path)
    df_personal = pd.read_csv(personal_data_path)
    df_plan = pd.read_csv(plan_data_path)

    # Find Avg. Trimmed Mean as Imputing Value and Fill NAs (Step 2)
    monthly_charges_mean = int(round(stats.trim_mean(df_charges['monthlyCharges'], 0.1, axis=0)))
    total_charges_mean = int(round(stats.trim_mean(df_charges['totalCharges'], 0.1, axis=0)))
    df_charges['monthlyCharges'] = df_charges['monthlyCharges'].fillna(value=monthly_charges_mean)
    df_charges['totalCharges'] = df_charges['totalCharges'].fillna(value=total_charges_mean)

    # Bin Tenure (Step 3)
    df_charges['tenureBinned'] = pd.cut(df_charges['tenure'], [0, 24, 48, 60, np.inf], labels=['group1', 'group2', 'group3', 'group4'], right=True)

    # Calculate Churn Rate Percentage (Step 4)
    churn_pct = int(round(100 * df_charges['churn'].value_counts()['Yes'] / df_charges.shape[0]))

    # Merge Datasets (Step 5)
    df_merged = df_charges.set_index('customerID').join(df_personal.set_index('customerID'), how='inner')
    df_merged = df_merged.join(df_plan.set_index('customerID'), how='left')
    # df_merged.reset_index(inplace=True)


    # Find Customer Age Percentage (Step 6)
    pct_age = int(round(100 * df_merged.query('age>60').shape[0] / df_merged.shape[0]))

    # Count Unique Values (Step 7)
    dict_internet = df_merged['internetService'].value_counts().to_dict()

    print(dict_internet)

    results = {
        'monthly_charges_mean': monthly_charges_mean,
        'charges_data_updated': df_charges,
        'churn_pct': churn_pct,
        'data_merged': df_merged,
        'pct_age_above_60': pct_age,
        'internet_service_counts': dict_internet
    }
    return results


# ================================================================================
#   Tests
# ================================================================================
from os.path import abspath, join, dirname
folder_data = abspath(join(dirname(__file__), '..', 'data'))

explanatory_analysis(
    pd.read_csv(join(folder_data, 'charges_data.csv')),
    pd.read_csv(join(folder_data, 'personal_data.csv')),
    pd.read_csv(join(folder_data, 'plan_data.csv'))
)


