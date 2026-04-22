# Sentinel-Agent: Autonomous Ops & Social Monitor

Sentinel is a production-ready AI agent framework designed for high-precision intent classification, operational routing, and social media performance monitoring.

## 🏗 System Architecture
The system is built on a modular "Agent-as-a-Service" model:
* **agents/routing_agent.py**: Handles internal communications and triaging for Slack and ClickUp.
* **agents/social_monitor.py**: Tracks LinkedIn/social metrics to automate content drafting.
* **config/settings.yaml**: Centralized environment management for API endpoints and agent behavior.

## 🚀 Key Features
* **Multi-Intent Detection**: Automatically distinguishes between Leads, Support issues, and Content ideas.
* **Performance-Driven Content**: Uses historical engagement data to guide LLM-based drafting.
* **Modular Configuration**: Designed for seamless deployment into Anthropic Claude and Cowork environments.

## 🛠 Setup & Installation
```bash
pip install -r requirements.txt
python agents/routing_agent.py
