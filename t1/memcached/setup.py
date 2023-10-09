import json
import memcache

mode = bool(int(input("Select mode: 1 - load, 0 - clear\n")))
client = memcache.Client(['172.17.0.2:11211'])
file_path="./cars.json"
with open(file_path, 'r') as file:
	data = json.load(file)

for item in data:
        key = f"id_{item['id']}"
        value = {
            "make": item["make"],
            "model": item["model"],
            "year": item["year"]
        }
        if mode:
            client.set(key, value)
        else:
            client.delete(key)
print("Done.")

