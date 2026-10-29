"""Check active README images, local links, anchors and SVG; optionally check HTTP links."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            assert attrs.get('alt'), 'Image needs alt text'
            self.images.append(attrs['src'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--online', action='store_true')
    args = parser.parse_args()
    source = re.sub(r'<!--.*?-->', '', (ROOT / 'README.md').read_text(), flags=re.S)
    html = Links()
    html.feed(source)
    urls = set(html.links + html.images + re.findall(r'\]\(([^)\s]+)\)', source))
    headings = re.findall(r'^#{1,6} (.+)$', source, re.M)
    anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
    errors = []
    for url in sorted(urls):
        parsed = urllib.parse.urlsplit(url)
        if not parsed.scheme:
            if not parsed.path and parsed.fragment not in anchors:
                errors.append(f'Missing anchor: {url}')
            elif parsed.path and not (ROOT / urllib.parse.unquote(parsed.path)).is_file():
                errors.append(f'Missing file: {url}')
        elif parsed.scheme not in ('https', 'http'):
            errors.append(f'Unexpected scheme: {url}')
        elif args.online:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Nico-profile-link-check/1.0'})
                with urllib.request.urlopen(req, timeout=25) as response:
                    print(f'HTTP {response.status}: {url}')
            except (urllib.error.URLError, TimeoutError) as exc:
                errors.append(f'Needs manual verification: {url}: {exc}')
    ET.parse(ROOT / 'assets/cover.svg')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(urls)} unique active references; {len(html.images)} HTML images; SVG is valid XML.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
