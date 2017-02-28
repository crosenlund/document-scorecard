# -*- coding: UTF-8 -*-
from spsbuild.tools.helpers import get_out
import os
import semantic_version


#=================================================
# housekeeping
#=================================================

# hack to get the right version of git installed
if os.environ.get("TRAVIS") == "true":
    print get_out(['sudo', 'apt-get', 'update'])
    print get_out(['sudo', 'apt-get', 'install', 'git'])


# find out the current gitsha
build_version = get_out(['git', 'rev-parse', 'HEAD'])

print "building", build_version

# find all the tags for this build
tags = get_out(['git', 'tag', '--points-at', build_version])
if len(tags):
    tags = tags.split("\n")
else:
    tags = []

versions = get_out(['git', 'tag']).split("\n")
versions = [ver[2:] for ver in versions]
versions.sort(key=semantic_version.Version, reverse=True)

current_version = tags[0] if len(tags) else build_version
