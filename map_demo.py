"""
Quick demo of choropleth mapping and using/manipulating geoJSON data. The output of this file is a Plotly map of
confirmed COVID-19 cases by city in Orange County, CA.
Author: Miles Latham

Learn more about Plotly Express here:
    https://plotly.com/python/plotly-express/
Data on confirmed cases for cities in Orange County, collected here:
    https://occovid19.ochealthinfo.com/coronavirus-in-oc
geoJSON file contaiing town boundaries in orange county downloaded from here:
    http://boundaries.latimes.com/sets/
"""

# imports
import json  # used for reading and writing json/geoJSON files
import pandas as pd  # common library for data manipulation
import plotly.express as px  # this is the high level plotly package for creating quick, easy graphs


"""
This is the function to generate our figure. Python functions are comparable to SAS macros (given an input, they 
produce a specific output). It's not strictly necessary to build this as a function, but if you were to use this same 
mapping style to graph other data it would be helpful. 
"""
def choropleth():

    """
    Step 1: loading our geojson data (this is the shapefile framework which we will 'populate' with data on COVID
    cases). geoJSON files are just regular JSON files that follow a very specific format. The format has to be perfect,
    otherwise everything will break. Read more about the file type here: https://geojson.org/

    The 'with' method below is a good way to load files- the file closes once you're done reading it. We use the JSON
    library imported above to tell Python the file is JSON data, and then load it into a dict. Dicts are one of the
    common data types in python, where data is stored in key value pairs like this- {'key': value} and values are called
    like this- dictionary['key']. Curly brackets are used to differentiate dictionaries from other data types.

    We then change the structure of the towns dictionary a bit. In order for geoJSON data to work correctly with Plotly,
    there needs to be an 'id' variable at the outer level of each different feature in the dataset (In geoJSON talk, a
    'feature' is just a unique location/point/shape in the dataset, which is towns in this case) In this data, there
    isn't an outer-level ID. For the sake of simplicity, here I just pull out the town name from within the data for
    each feature, and use that string as the ID. This is a bad idea- alternate spellings, spacing, or punctuation would make it
    impossible to match on this ID variable, but this is a small enough dataset that it works fine here. The strip()
    command just removes leading and trailing whitespace, which was in the source data.
    """
    with open('towns.geojson') as f:  #
        towns = json.load(f)
    for town in towns['features']:
        town['id'] = town['properties']['name'].strip()
    """
    Step 2: loading our case data. This is just a very small, simple dataset in an xlsx file, with city names and the 
    number of cases for each city. I'm loading it into a dataframe, which is a container from the Pandas library. 
    Dataframes are ubiquitous in python, because they allow for fast, vectorized calculations. Pandas is a really 
    complex library, with tons of features, challenging documentation, and syntax that's different than the rest of
    Python. It's almost worth thinking of pandas as a separate language, although here our use is pretty simple. 
    
    After loading the file into a dataframe, I use the strip() function to again remove leading and trailing white space
    from the city names in the 'id' column. Note the different syntax- for the dictionary I iterated through the 
    dictionary and applied the function in a 'for' loop. This is frowned upon for dataframes because it's really slow, 
    so here I use the pandas apply() method to apply my function as a lambda (this is just a nameless function that you 
    define and then call in place). 
    """
    df = pd.read_excel('cases.xlsx')
    df['id'] = df['id'].apply(lambda x: x.strip())
    """
    Step 3: Creating the figure. Here, we generate the actual map using the Plotly Express choropleth command. This 
    essentially maps the input data onto the geographic containers you want to display on the map, which in this case
    is towns in orange county. Below I've annotated each argument for the function so you know what they're doing. (there are 
    also many more optional arguments I'm excluding). 
    
    The first argument is our input data- the dataframe of confirmed cases by town.
    The geojson argument is telling plotly that the 'base' of the map is our towns geoJSON data. 
    locations="id" tells it that we're matching up our input data to that 'base' using the "id" category in the input data. This 
    is then matched with the city name identifier that we added to the outer scope of the geoJSON file above.
    locationmode tells plotly that's what we're doing- it should be able to infer that without it but doesn't always. 
    color tells it what var from the input data our 'Z' variable is, ie what we want to use as the basis for the map coloration.
    hover_name tells it what information to display when you hover over a given town on the map. 
    color_continuous_scale is just the color scheme- here I'm using a builtin scale from white to dark blue. 
    range_color is the range of coloration for our 'Z' variable- the maximum blue color is set to 150 cases and above.
    """
    fig = px.choropleth(df,
                        geojson=towns,
                        locations="id",
                        locationmode='geojson-id',
                        color="Confirmed Cases",
                        hover_name="id",
                        color_continuous_scale='blues',
                        range_color=[0, 150])

    """
    Step 4: These are (optional) changes to the style/display of the map. update_traces is just changing the boundary
    lines between towns from black to white, decreasing the width of those lines, and slightly decreasing the opacity 
    of the map. This is all just stuff to make it look a bit better.
    
    update_layout is just being used to add a title.
    
    update_geos is telling plotly to bound the map to the specific locations we're inputting, and make everything else
    invisible. 
    
    The return statement ends our choropeth() function, and tells it to return this figure (or rather all the information
    describing the figure and its data). 
    """
    fig.update_traces(marker=dict(
                            line=dict(
                                        color='white',
                                        width=.1),
                            opacity=.9))
    fig.update_layout(title='Confirmed COVID-19 Cases in Orange County (By City)')
    fig.update_geos(fitbounds="locations", visible=False)

    return fig


"""
Step 5: Showing the figure. This simply initializes the above function, sets the outputted figure as the variable 'fig_map', 
and then tells plotly to generate and show the figure. The default is a new window in your browser, but you can also 
output the figure as an HTML file, or take that raw output from the function, put it in an app, and generate it there. 
That's what we do in our dashboard. You can also just put fig.show() in the above function and delete the return line.
 """
fig_map = choropleth()
fig_map.show()
