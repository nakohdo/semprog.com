#!/usr/bin/env python3
# Chapter 3: Using Semantic Data, p. 42

# %%
from simplegraph import SimpleGraph
bg = SimpleGraph()
bg.load('../chapter3/business_triples.csv')

# %%
bg.query([('?company', 'name', 'Google')])

# %%
bg.query([('?company', 'name', '?name')])
# %%
bg.query([('?company', 'headquarters', '?location')])
# %%
