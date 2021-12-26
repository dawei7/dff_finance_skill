import deepl
import os

translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

result = translator.translate_text("Hello, world!", target_lang="DE")
print(result)


