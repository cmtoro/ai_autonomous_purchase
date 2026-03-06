import os
import logging
from langchain_anthropic import ChatAnthropic
# The LangChain API changed in recent versions. `initialize_agent` was removed and
# tools are now constructed differently. We also import `Tool` from
# `langchain_core.tools` since `langchain.tools` no longer exports it.
from langchain.agents import create_agent
from langchain_core.tools import Tool

logger = logging.getLogger(__name__)

# LLM Configuration
logger.info("Initializing ChatAnthropic LLM")
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)
logger.info("LLM initialized")

# Tool definition: Write to file
def write_code_to_file(file_path: str, content: str):
    """Writes or overwrites code into a specific file path."""
    logger.info(f"Writing code to file: {file_path}")
    with open(file_path, "w") as f:
        f.write(content)
    logger.info(f"Successfully updated: {file_path}")
    return f"Success: {file_path} has been updated."

# Tool definition: Read file
def read_repository_file(file_path: str):
    """Reads the content of a file to understand current logic."""
    logger.info(f"Reading file: {file_path}")
    with open(file_path, "r") as f:
        content = f.read()
    logger.info(f"Successfully read {len(content)} characters from {file_path}")
    return content

def list_files(directory: str = "."):
    """Lists the current project structure to provide context to the agent."""
    logger.info(f"Listing files in directory: {directory}")
    file_list = []
    for root, dirs, files in os.walk(directory):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Exclude agent_system folder to prevent self-modification
        if 'agent_system' in dirs:
            dirs.remove('agent_system')
        for name in files:
            if not name.startswith('.'):
                file_list.append(os.path.join(root, name))
    result = "\n".join(file_list)
    logger.info(f"Listed {len(file_list)} files")
    return result

# Create LangChain tools from the helper functions.  In the newer API,
# we can either pass plain callables to `create_agent` or explicitly
# wrap them with `Tool.from_function` to set names and descriptions.
# The previous version used `Tool(name=..., func=...)` which no longer
# exists.
tools = [
    Tool.from_function(
        write_code_to_file,
        name="write_code",
        description="Use this to save code",
    ),
    Tool.from_function(
        read_repository_file,
        name="read_code",
        description="Use this to read current code",
    ),
    Tool.from_function(
        list_files,
        name="list_contents",
        description="List all files in the repository to understand the project structure.",
    ),
]

# System Instruction (Context Awareness)
system_message = (
    "You are a Cloud Software Engineer and an expert Python developer. You have access to a repository "
    "with a Python backend and Angular frontend. Always use 'list_files' "
    "first to understand the project structure before editing any code."
)

# The new entrypoint is `create_agent`.  It accepts a model instance or string,
# a list of tools (callables or Tool objects), and optional prompts/middleware.
logger.info("Creating agent with tools and system prompt")
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_message,
    # `verbose` was removed; use `debug` to enable detailed logs if desired
    debug=True,
)
logger.info("Agent created successfully")
