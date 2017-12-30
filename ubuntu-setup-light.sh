#!/bin/sh

# Tested on Ubuntu 16.04 LTS

sudo apt-get update -qq

# Installing packages
sudo apt-get install -q -y curl
sudo apt-get install -q -y wget
sudo apt-get install -y -q python-pip
sudo apt-get install -y -q python3-pip
sudo apt-get install -y -q git
sudo apt-get install -y -q vim
sudo apt-get install -y -q byobu

# oh my zsh
sudo apt-get install -q -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# byobu settings
mkdir -p ~/.byobu
touch ~/.byobu/.tmux.conf
echo 'set-option -g utf-8 on' >> ~/.byobu/.tmux.conf
echo 'set-option -g default-shell /usr/bin/zsh' >> ~/.byobu/.tmux.conf
echo 'set-option -g default-command /usr/bin/zsh' >> ~/.byobu/.tmux.conf
echo 'set-option -g default-path "$PWD"' >> ~/.byobu/.tmux.conf

# git configs
git config --global user.email stanleygu@gmail.com
git config --global user.name "Stanley Gu"
git config --global credential.helper cache

# Adding spf13
sh <(curl https://j.mp/spf13-vim3 -L)

# Latex stuff
sudo apt-get install -y -q texlive-latex-base texlive-xetex latex-xcolor texlive-math-extra \
    texlive-latex-extra texlive-fonts-extra texlive-bibtex-extra biber
