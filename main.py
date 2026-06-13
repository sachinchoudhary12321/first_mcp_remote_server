from fastmcp import FastMCP
import random
import json

mcp = FastMCP("simple calculator Server")

@mcp.tool
def add(a:int,b:int)->int:
    """add two numbers

    Args:
        a:first number
        b:second number

    return:
        the sum of a and b

    """
    return a+b

@mcp.tool
def random_number(min_val:int=1,max_val:int=100)->int:
    """genrate a number within a range

        Args:
            min_val:minimum value)(default:1)
            max_val:maximum value(default:100)

        return:
            a random integer between min_val and max_val
    """
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info()->str:
    """get information about the server"""
    info= {
        "name":"simple calculator server",
        "version":'1.0.0',
        'description':"a basic MCP server with math tools",
        "tools":['add','random_number'],
        "author":'sachin choudhary'
    }
    return json.dumps(info,indent=2)

    


if __name__ == "__main__":
   # mcp.run() transport is stdio
   mcp.run(transport='http',host='0.0.0.0',port=8000)
