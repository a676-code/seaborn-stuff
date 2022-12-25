import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import median

# Alternate way of reading in a csv ###################################
# import csv
# with open('bad-drivers.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar="|")
#     for row in reader:
#         print(', '.join(row[3:]))
#     sns.countplot(x=State)
#     plt.show()

df = pd.read_csv('bad-drivers.csv')
print(df.head())

# sns.countplot(x="Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", data=df)
# sns.scatterplot(x="State", y = "Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", data=df, hue="State")

df1 = pd.read_csv('US_births_1994-2003_CDC_NCHS.csv')
df2 = pd.read_csv('US_births_2000-2014_SSA.csv')

# sns.countplot(x="births", data = df1)

# Show fewer births on weekends #######################################
# sns.scatterplot(x = "day_of_week", y = "births", data = df1, hue="births")
# sns.relplot(x = "births", y = "day_of_week", data = df1, kind="scatter")
# sns.relplot(x = "births", y = "day_of_week", data = df2, kind="scatter")

# Histograms ##########################################################
# df1['births'].plot.hist()
# plt.clf() # clears the figure
sns.set(color_codes=True)
# sns.displot(df1['births'], color='m')

# Compare bright with colorblind
# for p in ['bright', 'colorblind']:
#     sns.set_palette(p)
#     sns.displot(df1['births'])
#     plt.show()

# sns.set() # seaborn's default style
# sns.displot(df1['births'], bins=30)
# sns.displot(df1['births'], kind = 'kde', rug = True, fill = True) # smooth

# Interesting spreads ###################################################
# sns.relplot(x = "Number of drivers involved in fatal collisions per billion miles", y = "Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted", data = df, kind="scatter")
# sns.relplot(x = "Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted", y = "Car Insurance Premiums ($)", data = df, kind="scatter", size="Losses incurred by insurance companies for collisions per insured driver ($)", hue = "Losses incurred by insurance companies for collisions per insured driver ($)")
# sns.relplot(x = "Percentage Of Drivers Involved In Fatal Collisions Who Had Not Been Involved In Any Previous Accidents", y = "Car Insurance Premiums ($)", data = df, kind="scatter")
# sns.relplot(x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", data = df, kind="scatter")
# sns.relplot(x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", data = df, kind="line")
# h = sns.lineplot(x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", data = df)
    # h.set_title("TITLE")
    # h.set(xlabel = "X AXIS", ylabel = "Y AXIS")
# sns.catplot(x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", data = df, kind="point", estimator=median)
# sns.catplot(x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", data = df, kind="point", join = False)

# Regression plots "best fits" #######################################
sns.regplot(data = df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)")
# sns.lmplot(data = df, x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)")
# sns.lmplot(data = df, x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", hue = "State") # doesn't print lines
# sns.lmplot(data = df, x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", row = "State") # too dense

# plt.show()
# plt.clf()

# sns.regplot(data = df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", x_bins = 8)

# plt.show()
# plt.clf()

# sns.regplot(data = df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", x_bins = 5, order=2)

# sns.despine() # removes top and right spines?

# scatter plot
# sns.regplot(data = df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", fit_reg=False)

dfbr = pd.read_csv('elements-by-episode.csv')

sns.set_style("whitegrid") # whitegrid, darkgrid
sns.set_palette("RdBu") # ["<hex>", "<hex>"]
# sns.set_context("paper") # paper, notebook, talk, poster

# Bar plots ##########################################################
# sns.catplot(x="BARN", data=dfbr, kind="count")
# sns.catplot(x="MOON", data=dfbr, kind="count")
# sns.catplot(y="SNOW", data=dfbr, kind="count", col="BUSHES")

# sns.catplot(x = "MOUNTAINS", y="BUSHES", data=dfbr, kind="bar")

dfc = pd.read_csv('country_stats_1993_appendix2.csv')

# can't read names, rotate x-tick labels ###############################
# sns.catplot(x = "Country", y = "Number of Incidents", data=dfc, kind = "bar")

# Box plots #########################################################
# sns.catplot(x = "day_of_week", y = "births", data=df1, kind = "box")
# sns.catplot(x = "day_of_week", y = "births", data=df1, kind = "box", whis=0.5)
# sns.catplot(x = "day_of_week", y = "births", data=df1, kind = "box", whis=[5,95])
# g = sns.catplot(x = "day_of_week", y = "births", data=df1, kind = "box", whis=[0,100])

# type_of_g = type(g)
# print(type_of_g)

# g.fig.suptitle("Day of Week vs Births")

# too dense when done horizontally
# sns.boxplot(data = df1, x = "day_of_week", y = "births")

# Color palettes #####################################################
# sns.palplot(sns.color_palette("Purples", 8))
# sns.palplot(sns.color_palette("Reds", 16))
# sns.palplot(sns.color_palette("husl", 10))
# sns.palplot(sns.color_palette('coolwarm', 6))

# Figure, axes, subplots ################################################
# fig, ax = plt.subplots()
# sns.histplot(df1['births'], ax = ax)
# ax.set(xlabel="Births 1994-2003")

# fig, ax = plt.subplots()
# sns.histplot(df1['births'], ax = ax)
# ax.set(xlabel="Births 1994-2003", xlim=(6000, 15000), title="Births from 1994-2003")

# Don't work? #######################################################
# ax.axvline(x=median, color='m', label='Median', linestyle='--', linewidth=2)
# ax.axvline(x=mean, color='b', label='Mean', linestyle='-', linewidth=2)
# ax.legend()

# Strip plots ######################################################
# sns.stripplot(data = df, x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", jitter = True)

dfcomma = pd.read_csv('comma-survey.csv')

# Swarm plots ######################################################
# sns.swarmplot(data=dfc, x="Number of Incidents", y="Country", hue="Number US Killed") # too dense, need a better data set

# Violin plots ####################################################
# sns.violinplot(data=dfc, x="Number of Incidents", y="Country", palette="husl") # too dense, need a better data set
# sns.violinplot(data=df1, x="day_of_week", y="births", palette="husl") # looks bad with variables switched

# Boxen plots #####################################################
# sns.boxenplot(data=df1, x="day_of_week", y="births", palette="Paired") # looks bad with variables switched

# Point plots ####################################################
# sns.pointplot(data=df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)") # same thing as above, still not showing error bars? 

# Bar plots ######################################################
# sns.barplot(data=df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)")

# Residual plots #################################################
# sns.residplot(data = df, x = "Car Insurance Premiums ($)", y = "Losses incurred by insurance companies for collisions per insured driver ($)", color='g')

dfmajors = pd.read_csv('all-ages.csv')

# Heatmaps ################################
# pd_crosstab = pd.crosstab(df1["month"], df1["year"])
# print(pd_crosstab)

# sns.heatmap(pd_crosstab)

# plt.xticks(rotation = 90)
# plt.yticks(rotation = 0)
# plt.show()
# plt.clf()

# sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=.3)

# FacetGrid #############################
# g2 = sns.FacetGrid(dfmajors, row="Major_category") # not the best, hard to read

# g2.map(sns.pointplot, 'Total') # not sure if Total is a good thing to pass

# sns.catplot(data=dfmajors, x="Total", kind = 'box', row="Major_category") # still a lot

# sns.catplot(data=dfmajors, x = "Total", kind = 'point', row="Major_category") # row_order=[...]

# works, but messy
# g3 = sns.FacetGrid(dfmajors, col="Major_category") # not the best, hard to read

# g3.map(plt.scatter, 'Major', 'Total') # not sure if Total is a good thing to pass

# sns.lmplot(data=dfmajors, x = 'Employed', y = 'Total', col="Major_category")

# PairGrids ############################################################
# g = sns.PairGrid(df, vars=["Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", "Car Insurance Premiums ($)"])
# g2 = g.map(sns.scatterplot)

# g2 = g.map_diag(sns.histplot)
# g3 = g2.map_offdiag(sns.scatterplot)

# pairplots #########################################################
# sns.pairplot(data=df, vars=["Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", "Car Insurance Premiums ($)"], kind='scatter')

# should be displaying distribution on off diagonals
# sns.pairplot(data=df, vars=["Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", "Car Insurance Premiums ($)"], kind='scatter', hue='Losses incurred by insurance companies for collisions per insured driver ($)', palette='RdBu', diag_kws={'alpha':.5})

# sns.pairplot(data=df, x_vars=["Percentage Of Drivers Involved In Fatal Collisions Who Were Speeding", "Percentage Of Drivers Involved In Fatal Collisions Who Were Alcohol-Impaired"], y_vars = ["Car Insurance Premiums ($)", 'Losses incurred by insurance companies for collisions per insured driver ($)'], kind='scatter', hue="Percentage Of Drivers Involved In Fatal Collisions Who Had Not Been Involved In Any Previous Accidents", palette="husl")

# sns.pairplot(data=df, vars=["Losses incurred by insurance companies for collisions per insured driver ($)", "Car Insurance Premiums ($)"], kind='reg', palette = 'BrBG', diag_kind='kde', hue="Percentage Of Drivers Involved In Fatal Collisions Who Had Not Been Involved In Any Previous Accidents")

# JointGrids #####################################################
# sns.set_style("whitegrid")
# g = sns.JointGrid(x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", data = df, xlim =(50, 200))

# g.plot(sns.regplot, sns.histplot)

# jointplots ###################################################
# sns.jointplot(x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", kind='reg', data = df)

# sns.jointplot(x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", kind='reg', data = df, order = 2, xlim=(50, 200))

# sns.jointplot(x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", kind='resid', data = df, order = 2)

g = sns.jointplot(x = "Losses incurred by insurance companies for collisions per insured driver ($)", y = "Car Insurance Premiums ($)", kind='scatter', data = df, marginal_kws = dict(bins=10))
g.plot_joint(sns.kdeplot)

plt.show()