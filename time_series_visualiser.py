import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Import data and clean
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Remove the top 2.5% and bottom 2.5% of data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

# 2. Line Plot
def draw_line_plot():
    # Create a line plot
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)

    # Title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save the figure
    fig.savefig('line_plot.png')
    return fig


# 3. Bar Plot
def draw_bar_plot():
    # Prepare the data for bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group data by year and month to get the average page views
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(15, 10)).figure

    # Title, labels, and legend
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save the figure
    fig.savefig('bar_plot.png')
    return fig


# 4. Box Plots
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box['year'] = [d.year for d in df_box.index]
    df_box['month'] = [d.strftime('%b') for d in df_box.index]
    df_box['month_num'] = df_box.index.month
    df_box = df_box.sort_values('month_num')

    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save the figure
    fig.savefig('box_plot.png')
    return fig


# Testing the functions
if __name__ == '__main__':
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
