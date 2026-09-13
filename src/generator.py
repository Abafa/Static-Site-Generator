from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path) :
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path).read()
    template = open(template_path).read()
    html_noded_file = markdown_to_html_node(file)
    title = extract_title(file)
    




    #aaaaaah Nopenopenope