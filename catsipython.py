from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

def extract_cat(results):
	return results[0].cat

def extract_city(results):
	return results[0].city

#create cypher statements
query = neo4j.CypherQuery(graph_db, "MERGE (cat:Cat {name: {name}, color: {color}, nationality: {nationality}, like: {like}, hate: {hate}}) RETURN cat")
query2 = neo4j.CypherQuery(graph_db, "MERGE (city:City {name: {name}}) RETURN city")
query3 = neo4j.CypherQuery(graph_db, "CREATE INDEX on :Cat(name)") 
query4 = neo4j.CypherQuery(graph_db, "CREATE INDEX on :City(name)") 

#create index
index_cats = query3.execute()
index_cities = query4.execute()

#cats
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




cities = [

extract_city(query2.execute(name="Malmo")),
extract_city(query2.execute(name="Toronto")),
extract_city(query2.execute(name="Paris")),
extract_city(query2.execute(name="Hong Kong"))

]

print [cat['name'] for cat in cats], [city['name'] for city in cities]

#relationships
relate_cat_to_city = neo4j.CypherQuery(graph_db, 
	"MATCH (a), (b) WHERE a.name = {cat_name} and b.name = {city_name} CREATE (a)-[:LIVES_IN]->(b)")

# gustav-[:LIVES_IN]->malmo,
# sixten-[:LIVES_IN]->malmo,
# peanut-[:LIVES_IN]->malmo,
# angel-[:LIVES_IN]->toronto,
# angel-[:COUSIN_TO]->peanut,
# luna-[:LIVES_IN]->toronto,
# leo-[:LIVES_IN]->toronto,
# leo-[:BORN_IN]->paris,
# jean-[:BROTHER_OF]->ilsa,
# ilsa-[:LIVES_IN]->paris,
# mao-[:LIVES_IN]->hong_kong
# mao-[:FATHER_OF]->luna

#RETURN neo4j.CypherQuery("cats"), ("cities") 


