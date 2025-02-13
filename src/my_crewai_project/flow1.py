import os
from dotenv import load_dotenv
from crewai.flow.flow import Flow, start, listen
from litellm import completion  # Using LiteLLM for Gemini API

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set API key for LiteLLM
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY

class TopicOutlineFlow(Flow):
    model = "gemini/gemini-pro"

    @start()
    def generate_topic(self):
        """Generates a creative blog topic."""
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": "Generate a creative blog topic for 2025."}]
        )
        topic = response["choices"][0]["message"]["content"].strip()
        print(f"Generated Topic: {topic}")
        return topic

    @listen(generate_topic)
    def generate_outline(self, topic):
        """Creates a blog outline based on the topic."""
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": f"Based on the topic '{topic}', create a detailed outline for a blog post."}]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("Generated Outline:")
        print(outline)
        return outline


# if __name__ == "__main__":
def kickoff():
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    print("Final Output:")
    print(final_outline)
