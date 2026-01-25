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
        response = requests.post(API_URL, json=data, headers=headers)
        res = response.json()
        return res['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"DeepSeek API 调用失败: {e}")
        return None

# --- 关键修改：更稳健的路径扫描 ---
search_path = Path("content") # 先定位到 content 文件夹
print(f"开始扫描目录: {search_path.absolute()}")

files_found = 0
for path in search_path.rglob("*.md"):
    files_found += 1
    post = frontmatter.load(path)
    
    # 打印每一篇扫到的文章状态，方便排查
    has_description = "已有摘要" if post.get('description') else "缺少摘要"
    is_draft = "草稿" if post.get('draft') else "正式发布"
    print(f"发现文件: {path} | 状态: {has_description}, {is_draft}")

    if not post.get('description') and not post.get('draft'):
        print(f">>> 正在为 {path.name} 生成摘要...")
        summary = get_summary(post.content)
        if summary:
            post['description'] = summary
            with open(path, 'wb') as f: 
                frontmatter.dump(post, f)
            print(f"成功写入摘要: {summary[:30]}...")
        else:
            print(f"摘要生成失败，请检查 API Key 或网络。")

if files_found == 0:
    print("⚠️ 警告：在 content 目录下没有找到任何 .md 文件！请检查仓库目录结构。")
