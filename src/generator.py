from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path) :
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path)
    template = open(template_path)
    html_noded_file = markdown_to_html_node(file)
    title = extract_title(file)
    template.replace("{{ Title }}" , title)
    template.replace("{{ Content }}" , html_noded_file)
    destination = dest_path.os.makedirs
    destination.write(template)

    #Et la ca marche pas parce que je sais que c'est de la merde et que j'ai rien panné aux assignements !




    #aaaaaah Nopenopenope