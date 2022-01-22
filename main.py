# Standard plotly imports
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode

df.iplot(
    x='read_time',	
    y='read_ratio',	
    # Specify the category	
    categories='publication',	
    xTitle='Read Time',	
    yTitle='Reading Percent',	
    title='Reading Percent vs Read Ratio by Publication')