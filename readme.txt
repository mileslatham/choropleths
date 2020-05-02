If you haven't installed python 3, you can learn how to do that here: 
https://realpython.com/installing-python/

There are two external packages necessary to run this script: pandas and plotly. 

The standard package manager for python is called pip, which you can use to install external libraries. See here for Python's documentation: 
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

For a less technical and somewhat clearer guide to getting started with pip on Windows, work through this super helpful guide:
https://projects.raspberrypi.org/en/projects/using-pip-on-windows

Package management in python can be a challenging process, because high-level package management tools infer where packages should be installed, and sometimes install them in places where your Python setup can't access them. A great alternative is using what's called a virtual environment, which you can also read about in the first link above. The requirements for this python script are simple enough that it shouldn't be necessary, but if you want to try setting one up and have any questions just let me know! Regardless, as you get more familiar with the language, understanding the fundamentals of package management and how to work with the relevant tools in a windows environment will help you save a lot of time down the line. 

Lastly, there are two data files required to run this code. 

'cases.xlsx' is the file containing confirmed cases by town.

'towns.geojson' is the JSON file contianing the coordinate data necessary to render the city boundaries on a map. 

If you make a copy of the python file and move it to another directory, just make sure those two files are also in that directory. 

