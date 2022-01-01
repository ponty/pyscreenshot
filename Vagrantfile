Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #   vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot_ubuntu.server.18.04"
  end

  config.vm.provision "shell", path: "tests/vagrant/ubuntu.server.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end
