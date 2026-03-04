# OPENAI_API_KEY 환경변수 설정 필요
from langchain.chat_models import init_chat_model

mode = init_chat_model("gpt-5-mini", model_provider="openai")
result = mode.invoke("랭체인이 뭔가요?")
print(result.content)
