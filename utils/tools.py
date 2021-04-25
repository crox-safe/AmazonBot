import re

def check_domain(url: str) -> str:
    return re.search('(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9][/]', url).group(0)
