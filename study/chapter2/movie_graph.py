# Import class
from simplegraph import SimpleGraph

# Create instance
movie_graph = SimpleGraph()

# Add triples
movie_graph.add('blade_runner', 'name', 'Blade Runner')
movie_graph.add('blade_runner', 'directed_by', 'ridley_scott')
movie_graph.add('ridley_scott', 'name', 'Ridley Scott')
movie_graph.add('george_lucas', 'name', 'George Lucas')
movie_graph.add('star_wars', 'directed_by', 'george_lucas')
movie_graph.add('star_wars', 'name', 'Star Wars')


# Query the knowledge graph
list(movie_graph.triples(None, None, None))
list(movie_graph.triples('blade_runner', 'directed_by', None))
list(movie_graph.triples(None, 'name', None))

movie_graph.value('blade_runner', 'directed_by', None)
movie_graph.value('ridley_scott', 'name', None)

movie_graph.value('ridley_scott', None, 'Ridley Scott')
movie_graph.value('blade_runner', None, 'ridley_scott')

movie_graph.value(None, 'directed_by', 'ridley_scott')
movie_graph.value(None, 'name', 'Ridley Scott')

movie_graph.value(None, 'name', 'Blade Runner')

# Save data to file
movie_graph.save('movie_graph_data.csv')

# Load data from file
movie_graph.load('movie_graph_data.csv')
movie_graph.load('star-wars.csv')
movie_graph.load('movie-directors.csv')
movie_graph.load('movies.csv')

# Date and time
from datetime import datetime

# current dateTime
now = datetime.now()

# convert to string
date_time_str = now.strftime("%Y-%m-%d_%H-%M")
print('DateTime String:', date_time_str)

dt = datetime.now().strftime("%Y-%m-%d_%H-%M")
print('Datetime:', dt)

# Output 2021-07-20 16:26:24