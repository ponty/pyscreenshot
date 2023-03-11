Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot.ubuntu.22.04.sway"
    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
    vb.customize ["modifyvm", :id, "--accelerate3d", "on"]
  end

  config.vm.provision "shell", path: "tests/vagrant/ubuntu.22.04.sway.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.ubuntu.22.04.sway.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
