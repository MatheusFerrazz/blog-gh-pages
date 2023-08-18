import markdown
import json

with open("post1.md", "r") as md_file:
    content = md_file.read()
    html_content = markdown.markdown(content)

with open("post1.html", "w") as html_file:
    html_file.write(html_content)

# Abra o arquivo JSON e carregue as configurações
with open('blog_info.json', 'r') as config_file:
    config_data = json.load(config_file)

# Acesse as configurações individualmente
blog_name = config_data["title"]
author = config_data["author"]
email = config_data["email"]
