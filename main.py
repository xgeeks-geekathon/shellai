from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Verifica se a seguinte pergunta tem haver com GitBash: "
                       "'Como posso fazer um commit do projeto x no diretorio y' "
                       "A resposta tem se ser [s/n] e caso seja 's', deverá ser seguido por "
                       "'|hlp|' + o comando que responde à dúvida inicial Responde apenas numa linha de código seguida",
        }
    ],
    model="gpt-4",
)

escolha = chat_completion.choices[0]
conteudo = escolha.message.content

print(conteudo)
