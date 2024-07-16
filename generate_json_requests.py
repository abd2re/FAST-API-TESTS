import json
from uuid import uuid1
from random import randint

max_queries: int = 100

for i in range(max_queries):
    request: dict[str, str] = {
        "id": str(uuid1()),
        "ip_source": f"{randint(0,256)}.{randint(0,256)}.{randint(0,256)}.{randint(0,256)}",
        "ip_destination": f"{randint(0,256)}.{randint(0,256)}.{randint(0,256)}.{randint(0,256)}",
    }
    with open(f"json_requests/{i}.json", "w") as file:
        file.write(json.dumps(request))
        
