Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot.debian11.gnome.x11"
  end

  config.vm.provision "shell", path: "tests/vagrant/debian10.gnome.x11.sh", privileged: true
  # config.vm.provision "shell", path: "tests/vagrant/debian10_gnome.sh", privileged: true
  config.vm.provision "shell", inline: "echo 'WaylandEnable=false' >> /etc/gdm3/daemon.conf", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.debian11.gnome.x11.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
