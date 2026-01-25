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
    except Exception as e:
        print(f"API 请求出错了: {e}")
        return None

# --- 修改开始：地毯式搜索 ---
# 获取当前脚本所在位置的根目录（即仓库根目录）
base_dir = Path(__file__).resolve().parent.parent.parent
print(f"当前仓库根目录定位在: {base_dir}")

files_checked = 0
# 使用 rglob("**/*.md") 搜索全仓库所有 .md 文件，确保万无一失
for path in base_dir.rglob("*.md"):
    # 跳过 .github 文件夹和隐藏文件夹
    if ".github" in str(path) or "archetypes" in str(path):
        continue
        
    files_checked += 1
    post = frontmatter.load(path)
    
    # 打印每个文件的状态，帮你排查为什么它被跳过
    print(f"检测到文件: {path.relative_to(base_dir)}")
    
    # 逻辑判断：没有 description，且不是草稿，且文件名不是 _index.md
    if not post.get('description') and not post.get('draft') and path.name != "_index.md":
        print(f"  🚀 正在生成摘要...")
        summary = get_summary(post.content)
        if summary:
            post['description'] = summary
            with open(path, 'wb') as f:
                frontmatter.dump(post, f)
            print(f"  ✅ 摘要已写入！")
    elif post.get('description'):
        print(f"  ⏩ 跳过：已有摘要")
    elif post.get('draft'):
        print(f"  ⏩ 跳过：是草稿(draft: true)")

print(f"扫描完毕，共检查了 {files_checked} 个 Markdown 文件。")