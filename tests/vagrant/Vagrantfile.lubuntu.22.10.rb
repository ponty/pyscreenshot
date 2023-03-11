Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/kinetic64"

  config.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.name = "pyscreenshot_lubuntu.22.10"
  end

  config.vm.provision "shell", path: "tests/vagrant/lubuntu.22.10.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

