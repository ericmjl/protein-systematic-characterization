import os
from pypandoc import convert_file

def get_md_files(directory):
    """
    Iterates over all files in a directory and returns a list of markdown
    files that are present in that directory.
    """
    md_files = []

    for f in os.listdir(directory):
        if f.endswith(('.md', '.MD', '.markdown', '.mdown')):
            md_files.append(f)

    return md_files

def write_index(directory, md_files):
    """
    Writes the index to a text file. It is markdown-formatted, but ends with
    '.rst' in order to no confuse the get_md_files function.

    Parameter types:
    ================
    - directory: str
    - md_files: list of str
    """
    with open('{0}/index.rst'.format(directory), 'w') as f:
        f.write('Index automatically generated using make_index.py.\n\n')
        f.write('Reports:\n\n')
        for md in md_files:
            f.write('- `{0} <./{0}>`_ \n'.format(md))


def convert_index_to_html(directory):
    """
    Looks for the index.rst file, and converts it to index.html using pypandoc.
    """
    convert_file('{0}/index.rst'.format(directory),
                 'html',
                 outputfile='{0}/index.html'.format(directory))

def build_index(directory):
    # Get the markdown files from a directory
    md_files = get_md_files(directory)
    write_index(directory, md_files)
    convert_index_to_html(directory)

def build_all_indexes():
    print(os.getcwd())
    for d in os.listdir(os.getcwd()):
        if os.path.isdir(d):
            print(os.path.join(os.getcwd(), d))
            build_index(os.path.join(os.getcwd(), d))

if __name__ == '__main__':
    build_all_indexes()
