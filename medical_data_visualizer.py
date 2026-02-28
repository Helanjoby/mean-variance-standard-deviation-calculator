import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] / (df['height']/100)**2) > 25).astype(int)

# Normalize data: 0 = good, 1 = bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Function to draw categorical plot
def draw_cat_plot():
    # Melt the dataframe
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    
    # Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    return fig

# Function to draw heatmap
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])]
    df_heat = df_heat[df_heat['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))]
    df_heat = df_heat[df_heat['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975))]
    
    # Calculate correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12,10))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, cmap='coolwarm')
    
    return fig

# Run the functions to display plots
cat_fig = draw_cat_plot()
cat_fig.show()  # Show categorical plot

heat_fig = draw_heat_map()
heat_fig.show()  # Show heatmap