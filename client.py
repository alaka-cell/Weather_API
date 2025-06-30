from mcp import MCPClient

def main():
    client = MCPClient("http://localhost:8000")  
    
    city = input("Enter city: ")
    response = client.call_tool("weather", city)
    print("Response:", response)

if __name__ == "__main__":
    main()
