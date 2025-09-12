movie={
    "name":"hhvm",
    "director":"krish",
    "realese-date":"25/07/2025",
    "budget":"150cr"

}
print(movie)
#addding value
movie['genre']='action'

#adding multiple values 
movie['actors']=['pk','nidhi']
print(movie)

#adding multiple values as properties inside we are using dictionary
movie['remuneration']={'pk-rem':'50cr','nidhi-rem':'10cr','dir-rem':'25cr'}
print(movie)
#accesing the values
print(movie['remuneration']['pk-rem'])

print(f'{movie["actors"][0]} is charging {movie["remuneration"]["pk-rem"]} is charging for acting {movie["name"]}')

#delete property from dictionary
del movie['genre']
print(movie)

movienames=['HHVM','WAR2','COOLIE','KINGDOM']

#to access last element from the list
print(movienames[len(movienames)-1])

#want to add value/element at the last index of the list
op=movienames+['OG']
print(op)



raj=frozenset()
print(type(raj))