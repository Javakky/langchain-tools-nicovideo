# langchain-tools-nicovideo

## What is Snapshot Search API ?
Plugin to enable [nicovideo "Snapshot Search API v2"](https://site.nicovideo.jp/search-api-docs/snapshot) from [hwchase17/langchain](https://github.com/hwchase17/langchain). <br>
The Snapshot Search API is used to obtain statistical information about videos posted on nicovideo, such as titles, descriptions, and view counts.

## Terms of Use
API [terms of use](https://site.nicovideo.jp/search-api-docs/snapshot#api%E5%88%A9%E7%94%A8%E8%A6%8F%E7%B4%84) apply.

For example, the following are prohibited.

2. Business activities, for-profit use, or preparation for such activities.


4. Any action that adversely affects or interferes with the functions or performance of niconico.

## Way to use

```python
llm = OpenAI(temperature=0)
tools = load_tools(["requests_all"], llm=llm)
tools.append(
    NicovideoQueryRun(
        api_wrapper=NicovideoSnapshotApiWrapper()
    )
)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent.run("千本桜の再生回数は？")

```