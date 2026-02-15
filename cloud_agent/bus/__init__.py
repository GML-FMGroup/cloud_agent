"""Message bus module for decoupled channel-agent communication."""

from cloud_agent.bus.events import InboundMessage, OutboundMessage
from cloud_agent.bus.queue import MessageBus

__all__ = ["MessageBus", "InboundMessage", "OutboundMessage"]
