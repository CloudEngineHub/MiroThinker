# Copyright 2025 Miromind.ai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

main_system_prompt_foreword = """In this environment you have access to a set of tools you can use to answer the user's question. \n    \nYou only have access to the tools provided below. You can only use one tool per message, and will receive the result of that tool in the user's next response. You use tools step-by-step to accomplish a given task, with each tool-use informed by the result of the previous tool-use."""

sub_agent_system_prompt_foreword = """In this environment you have access to a set of tools you can use to answer the user's question. \n    \nYou only have access to the tools provided below. You can only use one tool per message, and will receive the result of that tool in the user's next response. You use tools step-by-step to accomplish a given task, with each tool-use informed by the result of the previous tool-use."""

system_prompt_tool_instrcutions = """# Tool-Use Formatting Instructions \n\nTool-use is formatted using XML-style tags. The tool-use is enclosed in <use_mcp_tool></use_mcp_tool> and each parameter is similarly enclosed within its own set of tags.\n\nThe Model Context Protocol (MCP) connects to servers that provide additional tools and resources to extend your capabilities. You can use the server's tools via the `use_mcp_tool`.\n\nDescription: \nRequest to use a tool provided by a MCP server. Each MCP server can provide multiple tools with different capabilities. Tools have defined input schemas that specify required and optional parameters.\n\nParameters:\n- server_name: (required) The name of the MCP server providing the tool\n- tool_name: (required) The name of the tool to execute\n- arguments: (required) A JSON object containing the tool's input parameters, following the tool's input schema, quotes within string must be properly escaped, ensure it's valid JSON\n\nUsage:\n<use_mcp_tool>\n<server_name>server name here</server_name>\n<tool_name>tool name here</tool_name>\n<arguments>\n{\n\"param1\": \"value1\",\n\"param2\": \"value2 \\\"escaped string\\\"\"\n}\n</arguments>\n</use_mcp_tool>\n\nImportant Notes:\n- Tool-use must be placed **at the end** of your response, **top-level**, and not nested within other tags.\n- Always adhere to this format for the tool use to ensure proper parsing and execution.\n\nString and scalar parameters should be specified as is, while lists and objects should use JSON format. Note that spaces for string values are not stripped. The output is not expected to be valid XML and is parsed with regular expressions.\nHere are the functions available in JSONSchema format:\n\n"""
