Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot.debian10.kde.x11"
  end

  config.vm.provision "shell", path: "tests/vagrant/debian10.kde.x11.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.debian10.kde.x11.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
