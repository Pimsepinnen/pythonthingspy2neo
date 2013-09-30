from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

def extract_cat(results):
	return results[0].cat


query = neo4j.CypherQuery(graph_db, "CREATE (cat {name: {name}, color: {color}, nationality: {nationality}, like: {like}, hate: {hate}}) RETURN cat")


cats = [
	extract_cat(query.execute(name="Gustav", color="yellow", nationality="swede", like='lasagna', hate='dogs')),
	extract_cat(query.execute(name= "Sixten", color="stripted", nationality="", like='to play', hate= 'being inside')),
	extract_cat(query.execute(name='Peanut', color="grey", nationality="canadian", like="to sleep", hate= 'flowers')),
	extract_cat(query.execute(name="Angel", color="calio", nationality="canadian", like="a ball of thread", hate="being inside")),
	extract_cat(query.execute(name="Luna", color="white", nationality="canadian", like="paperbags", hate="water")),
	extract_cat(query.execute(name="Leo", color="yellow", nationality="french", like="cheese", hate="flowers")),
	extract_cat(query.execute(name="Ilsa", color="white", nationality="french", like="wine", hate="boats")),
	extract_cat(query.execute(name="Jean", color="grey&white", nationality="french", like="bread", hate="water")),
	extract_cat(query.execute(name="Mao", color="black", nationality="chinese", like="to fight", hate="water" ))




	]

print cats[0..]['name']



#results = query.execute(name= "Sixten", color="stripted", nationality="", like='to play', hate= 'being inside')
						# name='Peanut', color="grey", nationality="canadian", like="to sleep", hate= 'flowers',)
						# name="Angel", color="calio", nationality="canadian", like="a ball of thread", hate="being inside",
						# name="Luna", color="white", nationality="canadian", like="paperbags", hate="water",
						# name="Leo", color="yellow", nationality="french", like="cheese", hate="flowers",
						# name="Ilsa", color="white", nationality="french", like="wine", hate="boats",
						# name="Jean", color="grey&white", nationality="french", like="bread", hate="water",
						# name="Mao", color="black", nationality="chinese", like="to fight", hate="water" ,)


#print query



#print(graph_db.neo4j_version)

#cats = graph_db.create

#CREATE CATS

#(gustav {name: "Gustav", color: "yellow", natinoality: "swede", like: "lasange", hate: "dogs" }),
#(sixten {name: "Sixten", color: "stripted", natinoality: "", "like": to play, "hate": being inside }),
#(peanut {name: "Peanut", color: "grey", natinoality: "canadian", "like": to sleep, "hate": flowers }),
#(angel {name: "Angel", color: "calio", natinoality: "canadian", like: "a ball of thread", hate: "being inside" }),
#(luna {name: "Luna", color: "white", natinoality: "canadian", like: "paperbags", hate: "water" }),
#(leo {name: "Leo", color: "yellow", natinoality: "french", like: "cheese", hate: "flowers" }),
#(ilsa {name: "Ilsa", color: "white", natinoality: "french", like: "wine", hate: "boats" }),
#(jean {name: "Jean", color: ":grey&white", natinoality: "french", like: "bread", hate: "water" }),
#(mao {name: "Mao", color: "black", natinoality: "chinese", like: "to fight", hate: "water" }),

#cities
#(malmo {name: "Malmo"}),
#(toronto {name: "Toronto"}),
#(paris {name: "Paris"}),
#(hong_kong {name: "Hong Kong"}),

#relationships

#gustav-[:LIVES_IN]->malmo,
#sixten-[:LIVES_IN]->malmo,
#peanut-[:LIVES_IN]->malmo,
#angel-[:LIVES_IN]->toronto,
#angel-[:COUSIN_TO]->peanut,
#luna-[:LIVES_IN]->toronto,
#leo-[:LIVES_IN]->toronto,
#leo-[:BORN_IN]->paris,
#jean-[:BROTHER_OF]->ilsa,
#ilsa-[:LIVES_IN]->paris,
#mao-[:LIVES_IN]->hong_kong
#mao-[:FATHER_OF]->luna

#RETURN neo4j.CypherQuery("cats"), ("cities") 


