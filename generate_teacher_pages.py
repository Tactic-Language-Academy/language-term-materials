import os

template_path = "template.html"
teachers = {
    "AliReza": "teacher01_AliReza",
    "Sara": "teacher02_Sara",
    "Hossein": "teacher03_Hossein",
}

with open(template_path, "r", encoding="utf-8") as tpl:
    template = tpl.read()

with open("links.txt", "w", encoding="utf-8") as link_file:
    for name, folder in teachers.items():
        html_content = template.replace("[Teacher Name]", name)
        teacher_dir = os.path.join("teachers", folder)
        os.makedirs(teacher_dir, exist_ok=True)
        html_path = os.path.join(teacher_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as out_file:
            out_file.write(html_content)

        link = f"https://yourusername.github.io/language-term-materials/teachers/{folder}/"
        link_file.write(f"{name}: {link}\n")
        print(f"{name} page generated: {link}")
