import os
import json
import re


def generate_html(root_folder):
    with open(
        os.path.join(root_folder, "ext", "snippets", "snippets.code-snippets"), "r"
    ) as json_file:
        snippets_json = json.load(json_file)

    # break out classes into separate files
    classes = {}
    for classname, attrs in snippets_json.items():
        if "." not in classname:
            classes[classname] = [
                {
                    "prefix": snippet["prefix"],
                    "description": snippet["description"],
                    "body": snippet["body"],
                }
                for snippet_name, snippet in snippets_json.items()
                if classname in snippet_name
            ]

    for classname, snippets in classes.items():
        with open(
            os.path.join(root_folder, "html", f"{classname}.html"), "w"
        ) as html_file:
            html = ""
            bodies = []
            for snippet in snippets:
                html += f"<hr><h5>{snippet['prefix']}</h5>"
                description = (
                    snippet["description"]
                    .replace("<", "|")
                    .replace(">", "|")
                    .replace("\n", "<br>")
                )
                html += f"<code>{description}</code><br>"
                # body = re.sub(r"\${.*}", "", snippet["body"])
                # if not body.startswith("["):
                #     body = body[: body.find("=") + 1]
                # body = body.replace("\n", "")
                body = snippet["body"]
                html += f"<kbd>{body}</kbd>"
                bodies.append(body)

            header = f"<h2>{classname} object.</h2><pre><code>"
            for b in bodies:
                header += b + "<br>"
            html = header + "</pre></code>" + html
            html_file.write(html)
