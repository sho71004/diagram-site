#!/usr/bin/env python3
import sys, os, datetime, openai

# 受け取る引数
slug, src = sys.argv[1], sys.argv[2]

# 入力テキスト読込
with open(src, encoding="utf-8") as f:
    user_input = f.read()

# ChatGPT用システムプロンプト
prompt = (
    "あなたは複雑な技術概念を5分で理解できる"
    "縦スクロール図解を生成するライター兼デザイナーです。"
    "インタラクティブで読みやすいHTMLを返してください。"
)

client = openai.OpenAI()

# 図解HTMLを取得
html_core = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user",   "content": user_input},
    ],
    max_tokens=4096
).choices[0].message.content

# HTMLテンプレートに挿入
html = f"""<!doctype html><html lang="ja"><meta charset="utf-8">
<title>{slug}</title><style>
body{{font-family:sans-serif;line-height:1.7;margin:0;padding:2rem;}}
</style><body>{html_core}</body></html>"""

# docs/ に書き出し
os.makedirs("docs", exist_ok=True)
with open(f"docs/{slug}.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ generated", slug, datetime.datetime.now())
