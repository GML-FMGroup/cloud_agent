"""
Entry point for running cloud_agent as a module: python -m cloud_agent
"""

from cloud_agent.cli.commands import app

if __name__ == "__main__":
    app()
