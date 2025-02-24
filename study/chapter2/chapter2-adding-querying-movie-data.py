# Chapter 2: Adding and Querying Movie Data

# %%
bladerunnerID = movie_graph.value(None, 'name', 'Blade Runner')
print(bladerunnerID)

# %%
# List comprehension to get all the actors in the movie
bladerunnerActorIDs = [actorID for _, _, actorID in movie_graph.triples(bladerunnerID, 'starring', None)]

# Traditional for loop to get all the actors in the movie
bladerunnerActorIDs = []
for _, _, actorID in movie_graph.triples(bladerunnerID, 'starring', None):
    bladerunnerActorIDs.append(actorID)

# %%
# Print the actors
print(bladerunnerActorIDs)

# %%
# Get the names of the actors
bladerunnerActors = [movie_graph.value(actorID, 'name', None) for actorID in bladerunnerActorIDs]
print(bladerunnerActors)

# %%
# Get the name of a specific actor
movie_graph.value('/guid/9202a8c04000641f800000000042a461', 'name', None)

# %%
# ID of Harrison Ford
harrisonFordID = movie_graph.value(None, 'name', 'Harrison Ford')
print(harrisonFordID)

# %%
# List comprehension to get all the movies Harrison Ford acted in
harrisonFordMovieIDs = [movie_graph.value(movieID,'name', None) for movieID, _, _, in movie_graph.triples(None, 'starring', harrisonFordID)]
print(harrisonFordMovieIDs)

# %%
# Spielberg ID
spielbergID = movie_graph.value(None, 'name', 'Steven Spielberg')
print(spielbergID)

# %%
# Movies directed by Spielberg 
spielbergMovieIDs = [movie_graph.value(movieID, 'name', None) for movieID, _, _, in movie_graph.triples(None, 'directed_by', spielbergID)]
print(spielbergMovieIDs)

# %%

# Movies directed by Spielberg and starring Harrison Ford
spielbergFordMovieIDs = [movie_graph.value(movieID, 'name', None) for movieID, _, _, in movie_graph.triples(None, 'directed_by', spielbergID) if (movieID, 'starring', harrisonFordID) in movie_graph.triples(None, 'starring', harrisonFordID)]
print(spielbergFordMovieIDs)

# %%
# Test new query function: Movies with Harrison Ford
movie_graph.query([('?movie', 'starring', '/en/harrison_ford')])

# %%
movie_graph.value(None, 'starring', '/en/harrison_ford')

# %%
# Movies with Harrison Ford, directed by Steven Spielberg
movie_graph.query([ ('?movie', 'starring',      '/en/harrison_ford'), 
                    ('?movie', 'directed_by',   '/en/steven_spielberg')])
# %%