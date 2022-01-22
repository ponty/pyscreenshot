Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.box_version = "2020.02.02"

  config.vm.boot_timeout = 600

  config.vm.provider "virtualbox" do |vb|
    #  vb.gui = true
    vb.memory = "2048"
    vb.name = "pyscreenshot_arch.kde.wayland"
  end

  config.vm.provision "shell", inline: <<-SHELL

  mkdir /etc/sddm.conf.d
  echo '[Autologin]
User=vagrant
#Session=plasma.desktop
Session=plasmawayland.desktop' > /etc/sddm.conf.d/autologin.conf

  /vagrant/tests/vagrant/arch_kde.sh

  SHELL

  config.ssh.extra_args = ["-t", "cd /vagrant; bash --login"]
end

# export VAGRANT_VAGRANTFILE=Vagrantfile.arch.kde.wayland.rb;export VAGRANT_DOTFILE_PATH=.vagrant_${VAGRANT_VAGRANTFILE}
# vagrant up && vagrant ssh
