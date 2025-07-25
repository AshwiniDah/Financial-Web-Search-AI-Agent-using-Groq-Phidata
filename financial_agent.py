from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# web search agent
web_search_agent=Agent(
    name="web search agent",
    role="search the web for the information",
    model=Groq(id="Compound-Beta-Kimi"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,

)

# financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="Compound-Beta-Kimi"),
    tools=[
        YFinanceTools(stock_price=True,stock_fundamentals=True),
    ],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","use table to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for NVDA",stream=True)

