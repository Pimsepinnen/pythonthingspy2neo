from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

def extract_cat(results):
	return results[0].cat

def extract_city(results):
	return results[0].city

def extract_relationship(results):
	return results[0].relationship

#create cypher statements
#cats
query = neo4j.CypherQuery(graph_db, "MERGE (cat:Cat {name: {name}, color: {color}, nationality: {nationality}, like: {like}, hate: {hate}}) RETURN cat")
#city
query2 = neo4j.CypherQuery(graph_db, "MERGE (city:City {name: {name}}) RETURN city")
#index labels
query3 = neo4j.CypherQuery(graph_db, "CREATE INDEX on :Cat(name)") 
query4 = neo4j.CypherQuery(graph_db, "CREATE INDEX on :City(name)") 
#relationships
query5 = neo4j.CypherQuery(graph_db, "MATCH (cat), (city) WHERE cat.name = {cat_name} AND city.name = {city_name} MERGE (cat)-[relationship:LIVES_IN]->(city) RETURN relationship")
query6 = neo4j.CypherQuery(graph_db, "MATCH (cat), (cat2) WHERE cat.name = {cat_name} AND cat2.name = {cat2_name} MERGE (cat)-[relationship:COUSIN_TO]->(cat2) RETURN relationship")
query7 = neo4j.CypherQuery(graph_db, "MATCH (cat), (cat2) WHERE cat.name = {cat_name} AND cat2.name = {cat2_name} MERGE (cat)-[relationship:FATHER_OF]->(cat2) RETURN relationship")
query8 = neo4j.CypherQuery(graph_db, "MATCH (cat), (cat2) WHERE cat.name = {cat_name} AND cat2.name = {cat2_name} MERGE (cat)-[relationship:BROTHER_OF]->(cat2) RETURN relationship")
query9 = neo4j.CypherQuery(graph_db, "MATCH (cat), (city) WHERE cat.name = {cat_name} and city.name = {city_name} MERGE (cat)-[relationship:BORN_IN]->(city) RETURN relationship")


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



#relationships

#LIVES_IN
relationship = [

extract_relationship(query5.execute(cat_name="Gustav", city_name="Malmo")),
extract_relationship(query5.execute(cat_name="Sixten", city_name="Malmo")),
extract_relationship(query5.execute(cat_name="Peanut", city_name="Malmo")),
extract_relationship(query5.execute(cat_name="Angel", city_name="Toronto")),
extract_relationship(query5.execute(cat_name="Leo", city_name="Toronto")),
extract_relationship(query5.execute(cat_name="Ilsa", city_name="Paris")),
extract_relationship(query5.execute(cat_name="Luna", city_name="Toronto")),
extract_relationship(query5.execute(cat_name="Mao", city_name="Hong Kong")),

#COUSIN_TO query6
extract_relationship(query6.execute(cat_name="Angel", cat2_name="Peanut")),
#BORN_IN query9
extract_relationship(query9.execute(cat_name="Leo", city_name="Paris")),
#BROTHER_OF query8
extract_relationship(query8.execute(cat_name="Jean", cat2_name="Ilsa")),
#FATHER_OF query7
extract_relationship(query7.execute(cat_name="Mao", cat2_name="Luna"))

]
 


#RETURN neo4j.CypherQuery("cats"), ("cities") 

print [cat['name'] for cat in cats], [city['name'] for city in cities]
