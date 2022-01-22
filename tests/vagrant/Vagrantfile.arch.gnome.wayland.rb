Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.box_version = "2020.02.02"

  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot_arch.gnome.wayland"
  end

  config.vm.provision "shell", inline: <<-SHELL

  /vagrant/tests/vagrant/arch_gnome.sh

  SHELL

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.arch.gnome.wayland.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
