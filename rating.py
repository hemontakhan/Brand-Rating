import plotly.figure_factory as ff
import pandas as pd
import csv

observer = pd.read_csv('brand.csv')

diagram = ff.create_distplot([observer['Avg Rating'].tolist()],['Avg Rating'],show_hist=False)
diagram.show()