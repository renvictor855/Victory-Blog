import os, requests, frontmatter
from pathlib import Path

API_KEY = os.environ.get("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_summary(content):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    # 优化后的结构化 Prompt
    prompt = (
        "你是一个专业的博文摘要助手。请阅读以下文章内容，并遵循以下准则：\n"
        "1. 撰写一段150字以内的中文摘要。\n"
        "2. 摘要必须准确、客观地概括全文核心论点或主要内容，严禁臆想或加入文中未提及的事实。\n"
        "3. 语言要精炼，直接输出摘要正文，不要有'这篇文章介绍了'、'摘要如下'等废话。\n"
        "4. 尊重原意，保持中立的专业语气。\n\n"
        f"文章内容如下：\n{content[:10000]}" # 稍微增加了截取长度以提供更多上下文
    )
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3 # 降低随机性，让输出更严谨、更尊重原文
    }
    try:
        res = requests.post(API_URL, json=data, headers=headers).json()
        return res['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"API 请求出错了: {e}")
        return None

# --- 地毯式搜索 ---
base_dir = Path(__file__).resolve().parent.parent.parent
print(f"当前仓库根目录定位在: {base_dir}")

files_checked = 0
for path in base_dir.rglob("*.md"):
    # 1. 过滤掉 .github, archetypes 以及所有 index.md (包括 _index.md)
    if any(part in str(path) for part in [".github", "archetypes"]) or path.name.lower() in ["index.md", "_index.md"]:
        continue
        
    files_checked += 1
    post = frontmatter.load(path)
    
    print(f"检测到文件: {path.relative_to(base_dir)}")
    
    # 2. 逻辑判断：没有 description，且不是草稿
    if not post.get('description') and not post.get('draft'):
        print(f"  🚀 正在生成摘要...")
        summary = get_summary(post.content)
        if summary:
            # 移除摘要中可能出现的换行符，保证 Front Matter 格式整洁
            post['description'] = summary.replace('\n', ' ')
            with open(path, 'wb') as f:
                frontmatter.dump(post, f)
            print(f"  ✅ 摘要已写入！")
    elif post.get('description'):
        print(f"  ⏩ 跳过：已有摘要")
    elif post.get('draft'):
        print(f"  ⏩ 跳过：是草稿(draft: true)")

print(f"扫描完毕，共检查了 {files_checked} 个有效的文章文件。")