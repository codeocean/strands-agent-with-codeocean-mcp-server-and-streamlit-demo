# code/agent.py

from strands import Agent
from strands.session.file_session_manager import FileSessionManager
from strands.agent.conversation_manager import SlidingWindowConversationManager
import uuid
from pathlib import Path
from mcps import codeocean_tools
from model import model

scratch = Path(__file__).parents[1] / "scratch"
scratch.mkdir(exist_ok=True)

# Session manager: manages the agent's session state, with local files (can be changed to a DB)
session_manager = FileSessionManager(
    session_id="aqua_agent_session",
    storage_dir=str(scratch),
)

conversation_manager = SlidingWindowConversationManager(
    window_size=10,
)


def get_agent():
    """Create a new agent with a fresh session"""
    fresh_session_manager = FileSessionManager(
        session_id=f"aqua_agent_session_{uuid.uuid4().hex[:8]}",
        storage_dir=str(scratch),
    )

    agent = Agent(
        model=model,
        system_prompt="""You are Aqua, a helpful and knowledgeable assistant specialized in Code Ocean platform management. 

You have powerful tools to help users work with Code Ocean's computational research platform, including:

🔬 **Capsules**: Search, run, and manage computational capsules that contain code and environments
📊 **Data Assets**: Create, search, and manage datasets, results, and combined data assets  
⚙️ **Computations**: Execute capsules, monitor progress, and retrieve results
🔍 **Search & Discovery**: Find capsules and data assets across the platform
📁 **File Management**: List, download, and work with files within data assets and computation results

I can help you:
- Search for existing capsules and data assets
- Run computational workflows and monitor their progress  
- Create new data assets from various sources (S3, computations, etc.)
- Download and analyze results from completed computations
- Manage metadata and organize your computational resources

Feel free to ask me about your Code Ocean environment, and I'll use the appropriate tools to assist you efficiently and accurately.""",
        tools=codeocean_tools,
        callback_handler=None,
        session_manager=fresh_session_manager,
        conversation_manager=conversation_manager,
    )
    return agent


if __name__ == "__main__":
    agent = get_agent()
    print(agent("List your tools"))
