# -*- coding: UTF-8 -*-
from spsbuild.tools.helpers import get_out
import os
import semantic_version
from spsbuild.tools.s3deploy import S3Deloyment


# find out the current gitsha
release_version = get_out(['git', 'rev-parse', 'HEAD'])

print "building", release_version

# find all the tags for this build
tags = get_out(['git', 'tag', '--points-at', release_version])
if len(tags):
    tags = tags.split("\n")
else:
    tags = []
versions = get_out(['git', 'tag']).split("\n")
versions = [ver[1:] for ver in versions]
versions.sort(key=semantic_version.Version, reverse=True)

current_version = tags[0] if len(tags) else release_version

ignore = ['local', 'get-tools.py', 'requirements.pip', 'setup.py', 'test_consolidation.py', 'node_modules', 'coverage', 'karma.conf.js']

# we do not want to deploy pull requests
if os.environ.get("TRAVIS") == "true" and os.environ.get("TRAVIS_PULL_REQUEST") == "false":
    deploy = S3Deloyment("static-assets.spscommerce.com")
    if "dist" in deploy.always_ignore:
        deploy.always_ignore.remove("dist")
    if len(tags):
        #  Only update current if we have a tagged commit
        deploy.deploy_to_file("function getCurrentStyleguideVersion() { return '" + current_version + "'; }", "style/current_version.js")
        for tag in tags:
            prefix = "style/{0}".format(tag)
            deploy.deploy_to(os.path.realpath(os.path.join(".", "dist")), prefix, ignore)
    else:
        prefix = "style/{0}".format(release_version)
        deploy.deploy_to(os.path.realpath(os.path.join(".", "dist")), prefix, ignore)
