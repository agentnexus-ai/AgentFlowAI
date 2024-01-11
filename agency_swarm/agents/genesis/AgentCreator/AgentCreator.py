from agency_swarm import Agent
from agency_swarm.tools.coding import ReadFile
from agency_swarm.tools.genesis import CreateAgentTemplate, ImportAgent, GetAvailableAgents


class AgentCreator(Agent):

    def __init__(self, **kwargs):
        # Initialize tools in kwargs if not present
        if 'tools' not in kwargs:
            kwargs['tools'] = []

        # Add required tools
        kwargs['tools'].extend([CreateAgentTemplate,
                                GetAvailableAgents,
                                ReadFile,
                                ImportAgent])

        # Set instructions
        if 'instructions' not in kwargs:
            kwargs['instructions'] = "./instructions.md"

        # Initialize the parent class
        super().__init__(**kwargs)


