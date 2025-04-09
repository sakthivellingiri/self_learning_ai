from autogen import UserProxyAgent, config_list_from_json
from autogen.agentchat.contrib.capabilities.teachability import Teachability  
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()  #

# Filter configuration for specific models
filter_dict = {
    "model": ["gpt-3.5-turbo"] #gpt-3.5-turbo and #gpt-4
}

# Load configuration from environment or file
config_list = config_list_from_json(
    env_or_file="OAI_CONGI_LIST", filter_dict=filter_dict
)

# LLM configuration
llm_config = {"config_list": config_list, "timeout": 120}

# Initialize the teachable agent
teachable_agent = ConversableAgent(
    name="teachable_agent", llm_config=llm_config
)

# Set up the Teachability capability
teachability = Teachability(
    reset_db=False,
    path_to_db_dir="./tmp/teachability_db"  
)

# Add teachability to the agent
teachability.add_to_agent(teachable_agent)

# Create user proxy agent with input mode always
user = UserProxyAgent("user", human_input_mode="ALWAYS")

# Initiate chat with the user
teachable_agent.initiate_chat(
    user, message='Hi, what is on your mind?'
)
