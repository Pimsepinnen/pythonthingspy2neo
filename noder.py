# create one node
from py2neo import neo4j
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

# create a single node
alice = graph_db.create({"name": "Alice"})

# create multiple nodes
people = graph_db.create(
    {"name": "Alice", "age": 33}, {"name": "Bob", "age": 44},
    {"name": "Carol", "age": 55}, {"name": "Dave", "age": 66},
)

# create two nodes with a connecting relationship
alice, bob, rel = graph_db.create(
    {"name": "Alice"}, {"name": "Bob"},
    (0, "KNOWS", 1, {"since": 2006})
)

# create a node plus a relationship to pre-existing node
ref_node = graph_db.get_reference_node()
alice, rel = graph_db.create(
    {"name": "Alice"}, (ref_node, "PERSON", 0)
)
rel_ab = alice.create_relationship_to(bob, "KNOWS")

# test if node_a and node_b are related in any way
if alice.is_related_to(bob):
    print "Yes!"

# test if node_a and node_b are related in a particular direction
if alice.is_related_to(bob, neo4j.Direction.OUTGOING):
    print "Yes!"

# test if node_a and node_b are related by a specific relationship
if alice.is_related_to(bob, neo4j.Direction.OUTGOING, "KNOWS"):
    print "Yes!"
