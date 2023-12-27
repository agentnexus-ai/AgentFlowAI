from agency_swarm import Agent
from agency_swarm.tools.coding import ChangeDir, ChangeLines, ReadFile, WriteFiles
from agency_swarm.tools.genesis import CreateAgentTemplate


class AgentCreator(Agent):

    def __init__(self, **kwargs):
        # Initialize tools in kwargs if not present
        if 'tools' not in kwargs:
            kwargs['tools'] = []

        # Add required tools
        kwargs['tools'].extend([CreateAgentTemplate, ChangeDir, ChangeLines, ReadFile, WriteFiles])

        # Set instructions
        if 'instructions' not in kwargs:
            kwargs['instructions'] = "./instructions.md"

        # Initialize the parent class
        super().__init__(**kwargs)


