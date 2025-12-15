import re

def clean_text(text: str) -> str:
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.S)
    text = re.sub(r"<style.*?>.*?</style>", "", text, flags=re.S)
    text = re.sub(r"\s+", " ", text)
    return text.strip()