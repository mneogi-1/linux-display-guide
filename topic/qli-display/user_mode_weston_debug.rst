.. _user_mode_weston_debug:

Debug User mode/Weston
======================
  
Autolaunch Weston
==================

   When you power On the device, the Weston screen launches automatically.
   The following script file has the Weston configurations and its
   command-line parameters that have been used to set up the Weston screen
   autolaunch: ``/etc/initscripts/init_qti_display``

   .. note:: You must enable SSH in Permissive mode to securely access your host device. For instructions, see `How to SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-254/how_to.html#how-to-ssh->`__.

   ::

      mount -o remount,rw /

   ::

      cat /etc/initscripts/init_qti_display



Configure Weston display
=========================

      .. note:: This content is only applicable to QCS6490.

      Weston uses the ``weston.ini`` configuration file. When Weston starts,
      it searches for the ``weston.ini`` file from the Weston init script as
      ``--config=/etc/xdg/weston/weston.ini`` and configures the Weston
      display pipeline. The detailed configurations are described at
      https://manpages.ubuntu.com/manpages/focal/en/man5/weston.ini.5.html.

      To fetch the Weston configuration file, run the following commands:

      ::

         mount -o remount,rw /

      ::

         cat /etc/xdg/weston/weston.ini

      On running the commands, you see the following ``weston.ini`` configuration sample output:

      ::

         configuration file for Weston
         [core]
         idle-time=0
         backend=sdm-backend.so
         repaint-window=10
         
         [output]
         name=DSI-1
         mode=on
         
         [output]
         name=DP-1
         mode=on
         
         [shell]
         clock-format=seconds

.. _user_mode_relaunch_weston:

Relaunch Weston
=============== 

To kill the Weston process and manually relaunch the Weston server, do the following:

.. note:: You must enable SSH in Permissive mode to securely access your host device. For instructions, see `How to SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-254/how_to.html#how-to-ssh->`__.

1. To identify the ID of the Weston processes, run the following
   commands:

   ::

      mount -o remount,rw /

   ::

      ps -A | grep weston

   Sample output:

   ::

      824 ?        00:00:12 weston
         1090 ?        00:00:00 weston-keyboard
         1092 ?        00:00:01 weston-desktop-

2. To kill the Weston process, run the following command:

   ::

      killall weston

3. To relaunch the Weston server, run the following commands:

   ::

      mount -o remount,rw /

   ::

      su

   ::

      . /etc/profile

   ::

      export XDG_RUNTIME_DIR=/dev/socket/weston

   ::

      mkdir --parents $XDG_RUNTIME_DIR

   ::

      chmod 0700 $XDG_RUNTIME_DIR

   ::

      cd /usr/bin

   ::

      ./weston --tty=2 --continue-without-input   
