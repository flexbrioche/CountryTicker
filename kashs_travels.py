from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = dict(type = 'choropleth',
            locations = ['spain', 'croatia', 'switzerland', 'britain', 'portugal', 'greece', 'bosnia', 'italy',
            'thailand', 'USA', 'indonesia'],
            locationmode = 'country names',
            colorscale= 'Portland',
            text=['SPN', 'CRA', 'SWZ', 'ENG', 'POR', 'GRC', 'BOS', 'ITA', 'THA', 'USA','INA'],
            z=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0],
            colorbar = {'title': 'Country Colours',
            'len':200, 'lenmode':'pixels'})

my_layout = Layout(title="Kash's Travels")

fig = {'data': data, 'layout': my_layout} 
offline.plot(fig, filename='kash_travels.html')
