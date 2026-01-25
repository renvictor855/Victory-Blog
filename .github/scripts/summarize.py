import os, requests, frontmatter
from pathlib import Path

API_KEY = os.environ.get("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_summary(content):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": f"请为这篇文章写一段100字以内的中文摘要，直接给内容：\n\n{content[:3000]}"}]
    }
    try:
        res = requests.post(API_URL, json=data, headers=headers).json()
        return res['choices'][0]['message']['content'].strip()
    except: return None

for path in Path("content/post").rglob("*.md"): # 检查你的文章目录是不是 content/post
    post = frontmatter.load(path)
    if not post.get('description') and not post.get('draft'):
        print(f"Generating for {path.name}...")
        summary = get_summary(post.content)
        if summary:
            post['description'] = summary
            with open(path, 'wb') as f: frontmatter.dump(post, f)
