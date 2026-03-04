from langchain.chat_models import init_chat_model

mode = init_chat_model("qwen3:32b", model_provider="ollama")
result = mode.invoke("랭체인이 뭔가요?")
print(result.content)
