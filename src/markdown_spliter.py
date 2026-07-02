def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type : TextType) -> list[TextNode] :
    splited_old_node = []
    delimiter_list = [
        "", #TEXT
        "**", #BOLD
         "*", #ITALIC
         "'", #CODE
         "[tilte]", #LINK
         "!" #IMAGE
          ]
    
    for old_node in old_nodes : 
        if old_node in not TextType.TEXT : 
            splited_old_node.extend(old_node)
        elif delimiter not in delimiter_list :
            raise Exception(f"Delimiter ({delimiter}) not handeled !")
        else :
            splited_old_node.extend(old_node.split(delimiter))      #Pas bon, le fichier doit retourner différents TextNodes pour chaque string, avec le texte et le type de texte du bloc.

    return splited_old_node

