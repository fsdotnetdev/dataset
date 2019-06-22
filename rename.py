import os
#path =  os.getcwd()
path = "./nsfw/ikuta_erika"
filenames = os.listdir(path)
i = 0
for filename in filenames:
    name = "ikuta_erika." + str(i) + ".jpg"
    os.rename(os.path.join(path, filename), os.path.join(path, name))
    #os.rename(filename, "ikuta_erika_" + str(i) + ".jpg")
    i += 1
