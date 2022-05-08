Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/jammy64"
  # config.vm.box_version = "20220104.0.0"
  # config.vm.box = "virusstyle/ubuntu-22.04-desktop-amd64"
  # config.vm.box_version = "1.0.0"

  config.vm.boot_timeout = 600
  config.vm.provider "virtualbox" do |vb|
    #vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot_ubuntu.22.04"
    vb.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]

    # 	https://bugs.launchpad.net/cloud-images/+bug/1829625
    # vb.customize ["modifyvm", :id, "--uart1", "0x3F8", "4"]
    # vb.customize ["modifyvm", :id, "--uartmode1", "file", "./ttyS0.log"]
  end

  config.vm.provision "shell", path: "tests/vagrant/ubuntu.22.04.sh", privileged: true

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.ubuntu.22.04.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
