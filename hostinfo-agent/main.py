from mcp.server.fastmcp import FastMCP
import tools

# 初始化MCP
mcp = FastMCP("host info mcp")
# 注册函数
mcp.add_tool(tools.get_host_info)
# 注册函数
@mcp.tool()
def foo():
    return ""

def main():
    # 标准输入输出：MCP和Agent同时运行在本机
    mcp.run("stdio") # sse


if __name__ == "__main__":
    main()
