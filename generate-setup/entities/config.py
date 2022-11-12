from os import path, getcwd

current_dirname = getcwd()
root_dirname = path.abspath(current_dirname)
templates_dirname = path.join(root_dirname, "templates")

class Config:
  path = {
    "ROOT": root_dirname,
    "TEMPLATES": templates_dirname
  }