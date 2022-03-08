#!/bin/sh
{ #try - update escape-room
    echo Try to update game...
    cd escape_room/
    git pull
} || { #catch - install escape-room
  echo There is no instance of the game in this directory.
  echo Installing game... 
  { #try - Linux install
    sudo apt update
    sudo apt -y install git
    #install python3
    echo "Installing python..."
    sudo apt -y install python3
    sudo apt -y install python3-pip python3-pil.imagetk python-tk python3-tk tk-dev
  } || { #catch - macOS install
    #install xcode-select for git
    xcode-select --install
    #install Homebrew
    echo "Installing homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    brew update
    #install python3
    echo "Installing python..."
    brew install python
  }
  #clone git-repo
  git clone https://github.com/user-name-1230/escape_room.git
  
  #install dependencies
  echo "Installing required methods..."
  echo "Installing adventurelib..."
  pip3 install adventurelib
  echo "Installing pillow..."
  pip3 install Pillow
  echo "Installing termcolor..."
  pip3 install termcolor
}

#Spiel starten
echo Spiel wird jetzt gestartet...
cd escape_room/
python3 escaperoom_main.py
