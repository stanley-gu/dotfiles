#!/usr/bin/env python
import os

if __name__ == "__main__":
    # The first argument of sys.argv is always the filename,
    # meaning that the length of system arguments will be
    # more than one, when command-line arguments exist.
    dotfiles = ['.vimrc.local', '.vimrc.bundles.local']
    for dotfile in dotfiles:
        try:
            os.symlink('./' + dotfile, str(os.environ['HOME']))
        except OSError as e:
            print "Problem creating symlink for: {2} \n OSError error({0}): {1}".format(e.errno, e.strerror, dotfile)
    print "Finished running installer"
