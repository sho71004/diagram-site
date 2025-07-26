import sys, openai, os, datetime
slug, src = sys.argv[1], sys.argv[2]
txt = open(src, encoding="utf-8").read()
client = openai.OpenAI()
html = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role":"user","content":txt}]
).choices[0].message.content
os.makedirs("docs", exist_ok=True)
with open(f"docs/{slug}.html","w",encoding="utf-8") as f:
  f.write(html)
print("done", datetime.datetime.now())
