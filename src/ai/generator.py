from loguru import logger
from src.ai.ollama_client import OllamaClient

class CommentGenerator:
    def __init__(self):
        self.client = OllamaClient()

    def generate_networking_comment(self, post_content: str, platform: str) -> str:
        """
        Generates a context-aware comment tailored for the specific platform.
        """
        if not post_content:
            logger.warning("No post content provided to generator.")
            return ""

        system_prompt = (
            "You are a thoughtful professional commenting on social media posts.\n\n"
            "Rules:\n"
            "- maximum 2 sentences long\n"
            "- respond to the idea in the post\n"
            "- avoid generic phrases like \"great post\"\n"
            "- optionally include 1 relevant hashtag if it makes sense\n"
            "- optionally include 1 generic human emoji (e.g. 🤔, 🤝, 💡, 🙌) but STRICTLY NO rockets (🚀) or spammy emojis, not necessary to use every time\n"
            "avoid using double brackets in the start and end of the comment\n"
            "- sound intelligent and human\n\n"
            "Output ONLY the comment text, nothing else."
        )

        user_prompt = f"Post:\n{post_content}"
        
        logger.info(f"Generating comment for {platform} post...")
        generated_comment = self.client.generate_response(system_prompt, user_prompt)
        
        # Clean up any potential quotation marks that some LLMs add
        if generated_comment.startswith('"') and generated_comment.endswith('"'):
            generated_comment = generated_comment[1:-1]
            
        logger.debug(f"Generated comment: {generated_comment}")
        return generated_comment
