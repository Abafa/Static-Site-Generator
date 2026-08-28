from textnode import TextNode, TextType
import shutil, os

def copy_content(target_list : list[str], destination_path : str, origin_path = "./static") :
    for target in target_list :
        if os.path.isfile(f"{origin_path}/{target}") :
            shutil.copy(f"{origin_path}/{target}", destination_path)
            print(f"copied {target} from {origin_path} to {destination_path}")
        else :
            if os.path.exists(f"{destination_path}/{target}") :
                raise FileExistsError(f"destination path {destination_path} already exists")
            os.mkdir(f"{destination_path}/{target}")
            new_destination_path = os.path.join(destination_path, target)
            new_origin_path = os.path.join(origin_path, target)
            recursive_list = os.listdir(new_origin_path)
            print(f"new dir created, going deeper")
            copy_content(recursive_list, new_destination_path, new_origin_path)




def static_to_public () :
    shutil.rmtree("./public", ignore_errors=True)
    os.mkdir("./public")
    list_targets = os.listdir("./static")
    copy_content(list_targets, "./public")
    print("Copying done")





def main() :
    static_to_public()

main()
