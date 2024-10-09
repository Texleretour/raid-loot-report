from jinja2 import Environment, FileSystemLoader

class ReportGenerator:
    def __init__(self, template_folder):
        self.env = Environment(loader=FileSystemLoader(template_folder))

    def generate_report(self, data, output_path):
        template = self.env.get_template('report_template.html')
        html_content = template.render(data)

        with open(output_path, 'w') as f:
            f.write(html_content)
