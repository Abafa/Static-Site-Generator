def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type : TextType) -> list[TextNode] :
    splited_old_node = []
    delimiter_dict = {
        "": "TEXT",
        "**": "BOLD",
        "*": "ITALIC",
        "'": "CODE",
        "[tilte]": "LINK",
        "!":  "IMAGE",
    }
    
    for old_node in old_nodes : 
        if old_node.text_type not is TextType.TEXT : 
            splited_old_node.extend(old_node)
        elif delimiter not in delimiter_list :
            raise Exception(f"Delimiter ({delimiter}) not handeled !")
        else :
            split = ""
            for char in old_node : 
                if char != delimiter :
                    split += char
                else :
                    splited_old_node.extend(TextNode(split, TextType.))
            
            
            
            
            #splited_old_node.extend(old_node.split(delimiter))      #Pas bon, le fichier doit retourner différents TextNodes pour chaque string, avec le texte et le type de texte du bloc.
            #split = old_node.split(delimiter)

    return splited_old_node



