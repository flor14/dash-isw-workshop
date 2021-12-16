import plotly.express as px

# Import irish dataset
df = px.data.iris()
# Create plotly plot
plotly_fig = px.scatter(df,
                        x="sepal_width", 
                        y="sepal_length",
                        color="species",
                        size='petal_length',
                        hover_data=['petal_width'])
plotly_fig.show()