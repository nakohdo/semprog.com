# Chapter 2: Adding and Querying Movie Data

bladerunnerID = movie_graph.value(None, 'name', 'Blade Runner')
print(bladerunnerID)

# List comprehension to get all the actors in the movie
bladerunnerActorIDs = [actorID for _, _, actorID in movie_graph.triples(bladerunnerID, 'starring', None)]

# Traditional for loop to get all the actors in the movie
bladerunnerActorIDs = []
for _, _, actorID in movie_graph.triples(bladerunnerID, 'starring', None):
    bladerunnerActorIDs.append(actorID)

# Print the actors
print(bladerunnerActorIDs)

# Get the names of the actors
bladerunnerActors = [movie_graph.value('/guid/9202a8c04000641f800000000042a461', 'name', None) for actorID in bladerunnerActorIDs]
print(bladerunnerActors)

# Get the name of a specific actor
movie_graph.value('/guid/9202a8c04000641f800000000042a461', 'name', None)