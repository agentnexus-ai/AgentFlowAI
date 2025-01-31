# AgentFlow AI

![Framework](https://github.com/user-attachments/assets/02583035-ac4c-4022-9052-589dd4e14c7b)

## Overview

AgentFlow AI aims to develop a framework to streamline the creation of AI agents, allowing anyone to build collaborative swarms of agents (Agencies) with distinct roles and capabilities. By conceptualizing automation through real-world entities like agencies and specialized agent roles, we make the process more intuitive for both users and the agents themselves.

### Key Features

- **Customizable Agent Roles**: Define and tailor roles such as CEO, virtual assistant, or developer, adjusting their functionalities using the [Assistants API](https://platform.openai.com/docs/assistants/overview).  
- **Complete Prompt Control**: Fully customize prompts without the limitations of predefined structures, ensuring flexibility.  
- **Tool Development**: Create tools within AgentFlow AI using [Instructor](https://github.com/jxnl/instructor), offering a seamless interface and automatic type validation.  
- **Optimized Communication**: Agents interact through a dedicated "send message" tool based on their unique descriptions.  
- **State Management**: Efficiently handles assistant states on OpenAI, storing configurations in a dedicated `settings.json` file.  
- **Production-Ready Deployment**: Designed for reliability and seamless deployment in production environments.  


## Installation

```bash
pip install -U agent-flow
```

## Getting Started


1. **Set Your OpenAI Key**:

    ```python
    from agent_flow import set_openai_key
    set_openai_key("YOUR_API_KEY")
    ```

2. **Create Tools**:
Define your custom tools with [Instructor](https://github.com/jxnl/instructor):
    ```python
    from agent_flow.tools import BaseTool
    from pydantic import Field

    class MyCustomTool(BaseTool):
        """
        A brief description of what the custom tool does.
        The docstring should clearly explain the tool's purpose and functionality.
        """

        # Define the fields with descriptions using Pydantic Field
        example_field: str = Field(
            ..., description="Description of the example field, explaining its purpose and usage."
        )

        # Additional fields as required
        # ...

        def run(self):
            """
            The implementation of the run method, where the tool's main functionality is executed.
            This method should utilize the fields defined above to perform its task.
            Doc string description is not required for this method.
            """

            # Your custom tool logic goes here
            do_something(self.example_field)

            # Return the result of the tool's operation
            return "Result of MyCustomTool operation"
    ```

    or convert from OpenAPI schemas:

    ```python
    from agent_flow.tools import ToolFactory
    # using local file
    with open("schemas/your_schema.json") as f:
        tools = ToolFactory.from_openapi_schema(
            f.read(),
        )

    # using requests
    tools = ToolFactory.from_openapi_schema(
        requests.get("https://api.example.com/openapi.json").json(),
    )
    ```

3. **Define Agent Roles**: Start by defining the roles of your agents. For example, a CEO agent for managing tasks and a developer agent for executing tasks.

    ```python
    from agent_flow import Agent

    ceo = Agent(name="CEO",
                description="Responsible for client communication, task planning and management.",
                instructions="You must converse with other agents to ensure complete task execution.", # can be a file like ./instructions.md
                files_folder="./files", # files to be uploaded to OpenAI
                schemas_folder="./schemas", # OpenAPI schemas to be converted into tools
                tools=[MyCustomTool],
                temperature=0.5, # temperature for the agent
                max_prompt_tokens=25000, # max tokens in conversation history
                )
    ```

    Import from existing agents:

   ```bash
   agent-flow import-agent --name "Devid" --destination "./"
   ```

   This will import Devid (Software Developer) Agent locally, including all source code files, so you have full control over your system. Currently, available agents are: `Devid`, `BrowsingAgent`.



4. **Define Agency Communication Flows**:
Establish how your agents will communicate with each other.

    ```python
    from agent_flow import Agency
    # if importing from local files
    from Developer import Developer
    from VirtualAssistant import VirtualAssistant

    dev = Developer()
    va = VirtualAssistant()

    agency = Agency([
           ceo,  # CEO will be the entry point for communication with the user
           [ceo, dev],  # CEO can initiate communication with Developer
           [ceo, va],   # CEO can initiate communication with Virtual Assistant
           [dev, va]    # Developer can initiate communication with Virtual Assistant
         ],
         shared_instructions='agency_manifesto.md', #shared instructions for all agents
         temperature=0.5, # default temperature for all agents
         max_prompt_tokens=25000 # default max tokens in conversation history
    )
    ```

    In AgentFlow AI, communication flows follow a directional structure, moving from left to right as defined in the agency_chart. For example, in the scenario above, the CEO can start a conversation with the developer (dev), who can then respond within that chat. However, the developer cannot initiate a conversation with the CEO. Instead, the developer can start a chat with the virtual assistant (va) and assign new tasks.

5. **Run Demo**:
Run the demo to see your agents in action!

    Web interface:

    ```python
    agency.demo_gradio(height=900)
    ```

    Terminal version:

    ```python
    agency.run_demo()
    ```

    Backend version:

    ```python
    completion_output = agency.get_completion("Please create a new website for our client.")
    ```

# CLI

## Genesis Agency

The `genesis` command starts the genesis agency in your terminal to help you create new agencies and agents.

#### **Command Syntax:**

```bash
agent-flow genesis [--openai_key "YOUR_API_KEY"]
```

Make sure to include:
- Your mission and goals.
- The agents you want to involve and their communication flows.
- Which tools or APIs each agent should have access to, if any.

## Importing Existing Agents

This CLI command allows you to import existing agents from local files into your agency.

#### **Command Syntax:**

```bash
agent-flow import-agent --name "AgentName" --destination "/path/to/directory"
```

To check available agents, simply run this command without any arguments.

## Creating Agent Templates Locally

This CLI command simplifies the process of creating a structured environment for each agent.

#### **Command Syntax:**

```bash
agent-flow create-agent-template --name "AgentName" --description "Agent Description" [--path "/path/to/directory"] [--use_txt]
```

### Folder Structure

When you run the `create-agent-template` command, it creates the following folder structure for your agent:

```
/your-specified-path/
│
├── agency_manifesto.md or .txt # Agency's guiding principles (created if not exists)
└── AgentName/                  # Directory for the specific agent
    ├── files/                  # Directory for files that will be uploaded to openai
    ├── schemas/                # Directory for OpenAPI schemas to be converted into tools
    ├── tools/                  # Directory for tools to be imported by default.
    ├── AgentName.py            # The main agent class file
    ├── __init__.py             # Initializes the agent folder as a Python package
    ├── instructions.md or .txt # Instruction document for the agent
    └── tools.py                # Custom tools specific to the agent

```

This structure ensures that each agent has its dedicated space with all necessary files to start working on its specific tasks. The `tools.py` can be customized to include tools and functionalities specific to the agent's role.

## Contributing

For details on how to contribute you agents and tools to AgentFlow AI, please refer to the [Contributing Guide](CONTRIBUTING.md).

## License

AgentFlow AI is open-source and licensed under [MIT](https://opensource.org/licenses/MIT).



## Need Help?

If you need help creating custom agent swarms for your business, check out our [Agents-as-a-Service](https://agents.vrsen.ai/) subscription, or schedule a consultation with me at https://calendly.com/vrsen/ai-project-consultation
