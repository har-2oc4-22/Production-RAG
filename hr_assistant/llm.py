"""Step 6: connect to the LLM (the "brain" of the assistant)."""

from langchain_groq import ChatGroq

from hr_assistant import config
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def get_llm():
    """Return a Groq chat model directly."""
    logger.info("Initializing LLM via Groq directly")
    return ChatGroq(
        model=config.LLM_MODEL_NAME,
        api_key=config.GROQ_API_KEY,
    )
