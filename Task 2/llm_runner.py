from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
    filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    n_ctx=4096,
    verbose=True
)

def ask_llm(prompt: str) -> str:
    result = llm(prompt=prompt, max_tokens=512)
    return result["choices"][0]["text"]
