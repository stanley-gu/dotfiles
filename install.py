#!/usr/bin/env python
import os
import subprocess

if __name__ == "__main__":
    # The first argument of sys.argv is always the filename,
    # meaning that the length of system arguments will be
    # more than one, when command-line arguments exist.
    dotfiles = ['.vimrc.local', '.vimrc.bundles.local', '.editorconfig']
    for dotfile in dotfiles:
        try:
            source = os.path.dirname(os.path.realpath(__file__)) + \
                '/' + dotfile
            link = os.environ['HOME'] + '/' + dotfile
            print 'Creating a symlink from ' + link + ' to ' + source
            os.symlink(source, link)
        except OSError as e:
            print("Problem creating symlink for:"
                  " {2} \n OSError error({0}): {1}").format(
                e.errno, e.strerror, dotfile)
            print 'Will try to overwrite this file'
            os.unlink(link)
            os.symlink(source, link)
            print '\n'
    subprocess.call(['sudo', 'npm', 'install', '-g', 'jshint',
                     'grunt-cli', 'bower'])
    subprocess.call(['vim', '+BundleInstall', '+qall'])
    subprocess.Popen(['npm', 'install'],
                     cwd=os.environ['HOME'] +
                     '/' + '.vim/bundle/tern_for_vim')
    print "Finished running installer"
