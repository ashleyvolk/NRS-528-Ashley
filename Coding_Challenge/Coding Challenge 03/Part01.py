# 1. Simple directory tree
# Replicate this tree of directories and subdirectories:
#
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# Using os.system or os.mkdirs replicate this simple directory tree.
# Delete the directory tree without deleting your entire hard drive.

# import os
# os.mkdir("draft_code")
# os.mkdir("draft_code/pending")
# os.mkdir("draft_code/pending/complete")
# os.mkdir("includes")
# os.mkdir("layouts")
# os.mkdir("layouts/default")
# os.mkdir("layouts/default/post")
# os.mkdir("layouts/default/post/posted")
# os.mkdir("site")
#
# os.rmdir("site")
# os.rmdir("layouts/default/post/posted")
# os.rmdir("layouts/default/post")
# os.rmdir("layouts/default")
# os.rmdir("layouts")
# os.rmdir("includes")
# os.rmdir("draft_code/pending/complete")
# os.rmdir("draft_code/pending")
# os.rmdir("draft_code")