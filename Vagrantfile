# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/bionic64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
   config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
     # Customize the amount of memory on the VM:
     vb.memory = "512"
   end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  $script = "
  export DEBIAN_FRONTEND=noninteractive
  echo 'export distutils_issue8876_workaround_enabled=1' >> /home/vagrant/.profile
  echo 'export export LC_ALL=C' >> /home/vagrant/.profile
  
# install python versions
  sudo add-apt-repository --yes  ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install -y python2.7-dev
  sudo apt-get install -y python3.6-dev
  sudo apt-get install -y python3.7-dev
  sudo apt-get install -y python3.8-dev
  sudo apt-get install -y python3-distutils

# tools
  sudo apt-get install -y mc xvfb
  sudo apt-get install -y tox
  sudo apt-get install -y python-pip
  sudo apt-get install -y python3-pip

# for pillow source install
  sudo apt-get install -y libjpeg-dev zlib1g-dev

# project dependencies
  sudo apt-get install -y scrot
  sudo apt-get install -y imagemagick
  sudo apt-get install -y gnome-screenshot
  
  sudo apt-get install -y python-gtk2
  sudo apt-get install -y libcanberra-gtk-module

  sudo apt-get install -y python-gi
  sudo apt-get install -y python3-gi
  sudo apt-get install -y gir1.2-gtk-3.0
  sudo apt-get install -y libcanberra-gtk3-module
    
  sudo apt-get install -y python-wxgtk3.0
  #sudo apt-get install -y python-wxgtk4.0 # this is for dev only
  sudo apt-get install -y python3-wxgtk4.0

  sudo apt-get install -y python-qt4
  sudo apt-get install -y python3-pyqt4
  
  sudo apt-get install -y python-pyqt5
  sudo apt-get install -y python3-pyqt5
  
  sudo apt-get install -y python-pyside
  sudo apt-get install -y python3-pyside
  
  #sudo apt-get install -y python-pyside2 # no python-pyside2 before disco (19.04)
  sudo pip install pyside2 --no-cache-dir
  #sudo apt-get install -y python3-pyside2 # no python3-pyside2 before disco (19.04)
  sudo pip3 install pyside2 --no-cache-dir
  
  sudo apt-get install -y python-qtpy
  sudo apt-get install -y python3-qtpy

# test dependencies
  #sudo pip install -r /vagrant/requirements-test.txt
  
# doc dependencies
  sudo apt-get install -y graphviz
  #sudo pip install -r /vagrant/requirements-doc.txt
  
  "
      config.vm.provision "shell", inline: $script
          
       
end
     

# osx:
# brew install imagemagick wxmac pyqt pyside gdk-pixbuf gtk+3 mc sdl_image sdl_ttf sdl_mixer portmidi 
# python3 -m pip install pygame==2.0.0.dev6 pillow qtpy wxpython pyobjc-framework-Quartz pyobjc-framework-LaunchServices nose path.py
# PATH="$PATH:/Users/vagrant/Library/Python/3.7/bin"