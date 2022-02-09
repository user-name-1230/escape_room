#!/bin/sh
{ #try - Linux install
  #install python3
  echo "Installing python..."
  sudo apt -y install python3
  #install dependencies
  sudo apt -y install python3-pip python3-pil.imagetk python-tk python3-tk tk-dev
} || { #catch - macOS install
  #install Homebrew
  echo "Installing homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
  brew update
  brew upgrade
  #install python3
  echo "Installing python..."
  brew install python
}
echo "Installing required methods..."
echo "Installing adventurelib..."
pip3 install adventurelib
echo "Installing pillow..."
pip3 install Pillow
echo "Installing termcolor..."
pip3 install termcolor
