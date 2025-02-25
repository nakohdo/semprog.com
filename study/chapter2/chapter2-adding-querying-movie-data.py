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

#%% 
# Get ID of George Lucas
georgeLucasID = movie_graph.value(None, 'name', 'George Lucas')
print(georgeLucasID)

# %%
# Actors in movies directed by Ridley Scott as well as movies directed by George Lucas
movie_graph.query([ ('?mov1', 'directed_by',   '/en/ridley_scott'), 
                    ('?mov2', 'directed_by',   '/en/george_lucas'),
                    ('?mov1', 'starring',      '?actor'),
                    ('?mov2', 'starring',      '?actor')    
                ])
# %%

movie_actors = [{'?mov1': '/en/black_hawk_down',
  '?mov2': '/authority/netflix/movie/70018728',
  '?actor': '/en/ewan_mcgregor'},
 {'?mov1': '/en/black_hawk_down',
  '?mov2': '/authority/netflix/movie/70003791',
  '?actor': '/en/ewan_mcgregor'},
 {'?mov1': '/en/black_hawk_down',
  '?mov2': '/authority/netflix/movie/60001814',
  '?actor': '/en/ewan_mcgregor'},
 {'?mov1': '/authority/imdb/title/tt0320661',
  '?mov2': '/authority/netflix/movie/70003791',
  '?actor': '/en/liam_neeson'},
 {'?mov1': '/en/blade_runner',
  '?mov2': '/en/american_graffiti',
  '?actor': '/en/harrison_ford'},
 {'?mov1': '/en/blade_runner',
  '?mov2': '/authority/netflix/movie/60010932',
  '?actor': '/en/harrison_ford'},
 {'?mov1': '/en/blade_runner',
  '?mov2': '/en/the_star_wars_holiday_special',
  '?actor': '/en/harrison_ford'}]

# %%
# Get the names of the actors
for actor in movie_actors:
    print(movie_graph.value(actor['?actor'], 'name', None) + ': "' 
        + movie_graph.value(actor['?mov1'], 'name', None) + '", "' 
        + movie_graph.value(actor['?mov2'], 'name', None) +'".')
# %%
