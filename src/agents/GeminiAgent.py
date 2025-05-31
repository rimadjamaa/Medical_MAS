import json


class GeminiAgent:
    def __init__(self, name, model, prompt, tools=None, structured_outputs=True, stream=False):
        self.name = name
        self.model = model
        self.prompt = prompt
        self.tools = tools
        self.structured_outputs = structured_outputs
        self.stream = stream

    def __call__(self, input):
        return self.run(input)

    def run(self, question):
        full_prompt = f"{self.prompt}\n\nQuestion: {question}"
        response = self.model.generate_content(full_prompt)
        text = response.text.strip()

        # Remove code block markers if present
        if text.startswith("```"):
            # Remove triple backticks and possible language hints
            lines = text.split('\n')
            # Remove first line (```python or ```json)
            lines = lines[1:] if lines[0].startswith("```") else lines
            # Remove last line if it's ```
            if lines and lines[-1].strip().startswith("```"):
                lines = lines[:-1]
            text = "\n".join(lines).strip()

        # Try to parse as JSON or Python dict
        try:
            # Try JSON first
            return json.loads(text)
        except Exception:
            try:
                # Try Python literal eval as fallback
                import ast
                return ast.literal_eval(text)
            except Exception:
                # Fallback: return as string in a dict
                return {"output": text}
