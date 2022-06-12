Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot_kubuntu.20.04"
  end

  config.vm.provision "shell", path: "tests/vagrant/kubuntu.20.04.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.kubuntu.20.04.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
