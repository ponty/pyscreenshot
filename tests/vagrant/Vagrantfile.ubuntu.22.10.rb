Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/kinetic64"

  config.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.name = "pyscreenshot_ubuntu.22.10"
    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
  end

  config.vm.provision "shell", path: "tests/vagrant/ubuntu.22.10.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

