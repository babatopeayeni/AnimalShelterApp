from animal_shelter import AnimalShelter

# Define your credentials and the Apporto host/port
username = "aacuser"
password = "SNHU12345"
host = "nv-desktop-services.apporto.com"  # Apporto remote host
port = 33049  # Apporto port where MongoDB is running

# Create an instance of AnimalShelter with the updated connection info
shelter = AnimalShelter(username, password, host=host, port=port)

# Test CREATE
doc_to_insert = {"animal_id": "TEST001", "name": "Buddy"}
created = shelter.create(doc_to_insert)
print("CREATE result:", created)

# Test READ
found_docs = shelter.read({"animal_id": "TEST001"})
print("READ result:", found_docs)

# Test UPDATE
update_result = shelter.update(
    {"animal_id": "TEST001"},
    {"$set": {"name": "BuddyUpdated"}}
)
print("UPDATE modified count:", update_result)

# Confirm the update
updated_docs = shelter.read({"animal_id": "TEST001"})
print("After UPDATE:", updated_docs)

# Test DELETE
deleted_count = shelter.delete({"animal_id": "TEST001"})
print("DELETE removed count:", deleted_count)

# Confirm the delete
post_delete = shelter.read({"animal_id": "TEST001"})
print("After DELETE:", post_delete)
