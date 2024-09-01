import os
from bs4 import BeautifulSoup

def remove_section_with_href(filename, section_class, href_pattern):
  """Removes the specified HTML section if its href contains the given pattern.

  Args:
    filename: The name of the HTML file.
    section_class: The class name of the section to remove.
    href_pattern: The pattern to match in the href attribute.
  """

  with open(filename, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

  sections = soup.find_all('section', class_=section_class)
  for section in sections:
    for a_tag in section.find_all('a'):
      if href_pattern in a_tag['href']:
        section.decompose()
        break

  with open(filename, 'w') as f:
    f.write(str(soup))

# Replace 'display-7' and 'mobi' with your actual values
section_class = 'display-7'
href_pattern = 'mobi'

for filename in os.listdir('.'):
  if filename.endswith('.html'):
    remove_section_with_href(filename, section_class, href_pattern)