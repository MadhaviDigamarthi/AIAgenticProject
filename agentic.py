import arxiv
import json
from datetime import datetime
from typing import List, Dict
class AgentMemory:
    def __init__(self):
        self.storage = {}

    def store(self, key, value):
        self.storage[key] = value

    def retrieve(self, key):
        return self.storage.get(key)
class PlannerAgent:
    def create_plan(self, goal: str) -> List[str]:
        print("📌 Planning steps...")
        return [
            "Search recent AI research papers related to agriculture",
            "Filter papers based on agriculture relevance",
            "Select top 3 recent papers",
            "Summarize each paper",
            "Store output in structured JSON format"
        ]
class ResearchSearchTool:
    def search_papers(self, max_results=10) -> List[Dict]:
        print("🔍 Searching papers...")

        search = arxiv.Search(
            query='("agriculture" OR "crop" OR "farming" OR "precision agriculture" OR "irrigation") AND ("AI" OR "machine learning" OR "deep learning")',
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        agriculture_keywords = [
            "agriculture", "crop", "farming",
            "irrigation", "soil", "plant", "yield"
        ]

        papers = []
        for result in search.results():
            combined_text = (result.title + result.summary).lower()

            if any(keyword in combined_text for keyword in agriculture_keywords):
                papers.append({
                    "title": result.title,
                    "authors": [author.name for author in result.authors],
                    "published": result.published.strftime("%Y-%m-%d"),
                    "summary": result.summary,
                    "url": result.entry_id
                })

            if len(papers) == 3:
                break

        return papers
class SummarizerTool:
    def summarize(self, text: str) -> str:
        sentences = text.split(". ")
        return ". ".join(sentences[:3]) + "."
class StorageTool:
    def save_to_json(self, data, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"💾 Data saved to {filename}")
class ExecutorAgent:
    def __init__(self):
        self.memory = AgentMemory()
        self.search_tool = ResearchSearchTool()
        self.summarizer = SummarizerTool()
        self.storage = StorageTool()

    def execute(self, plan: List[str]):
        # Step 1: Search papers
        papers = self.search_tool.search_papers()
        self.memory.store("selected_papers", papers)

        # Step 2: Summarize papers
        summarized_results = []
        for paper in papers:
            summary = self.summarizer.summarize(paper["summary"])
            summarized_results.append({
                "title": paper["title"],
                "authors": paper["authors"],
                "published": paper["published"],
                "url": paper["url"],
                "summary": summary
            })

        self.memory.store("summaries", summarized_results)

        # Step 3: Store final output
        final_output = {
            "task": "Top 3 recent AI research papers on agriculture",
            "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "results": summarized_results
        }

        self.storage.save_to_json(final_output)
        return final_output
class AutonomousAIAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()

    def run(self, goal: str):
        print("🎯 Goal:", goal)
        plan = self.planner.create_plan(goal)
        return self.executor.execute(plan)

if __name__ == "__main__":
    agent = AutonomousAIAgent()
    goal = "Find the top 3 recent AI research papers on agriculture, summarize them, and store the output"
    output = agent.run(goal)

    print("\n✅ Final Output:")
    print(json.dumps(output, indent=4))
