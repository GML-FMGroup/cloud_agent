"""Chat channels module with plugin architecture."""

from cloud_agent.channels.base import BaseChannel
from cloud_agent.channels.manager import ChannelManager

__all__ = ["BaseChannel", "ChannelManager"]
