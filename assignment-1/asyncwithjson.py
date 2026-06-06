import asyncio
import json

async def read_user_data():
    with open("user.json", "r") as file:
        data = json.load(file)

    print("\nUser Information")
    print("-" * 20)
    print(f"Name    : {data['name']}")
    print(f"Email   : {data['email']}")
    print(f"Phone   : {data['phone']}")
    print(f"Address : {data['address']}")

asyncio.run(read_user_data())
# if user.json file is like this format:
#{
#    "name": "Shabarish",
#    "email": "shabarish@example.com",
#    "phone": "9876543210",
#    "address": "Hyderabad, India"
#}