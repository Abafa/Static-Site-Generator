from textnode import TextNode, TextType

def copy_content(path, destination) :
    if os.path.isfile(path) :
        shutil.copy(path, destination)
    else :
        os.mkdir(destination)
        copy_content(path, destination)




def static_to_public () :
    shutil.rmtree("./public", ignore_errors=True)
    list_targets = os.listdir("./static")
    for target in list_targets :
        copy_content(f"./static/{target}", f"./public/{target}")



def main() :
    pass

main()
