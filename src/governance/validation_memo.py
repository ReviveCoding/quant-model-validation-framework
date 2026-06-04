from datetime import date


def make_report(title, sections):
    text = [f'# {title}', '', f'Generated: {date.today().isoformat()}', '']
    for header, body in sections:
        text.extend([f'## {header}', '', str(body), ''])
    return '\n'.join(text)
