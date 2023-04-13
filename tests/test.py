from langchain.agents import AgentType, load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from langchain_tools_nicovideo.tools.nicovideo.tool import NicovideoQueryRun
from langchain_tools_nicovideo.utilities import NicovideoSnapshotApiWrapper

llm = OpenAI(temperature=0)
tools = load_tools(["human"], llm=llm)
tools.append(
    NicovideoQueryRun(
        api_wrapper=NicovideoSnapshotApiWrapper()
    )
)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.run("千本桜の再生回数は？")
