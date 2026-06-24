.. _features_for_qcs6490_5430:

See the appropriate chip product for device-specific information.

.. container:: persistenttab-soc

  .. tabs::

   .. group-tab:: QCS6490

    .. class:: tabincludedirective

        .. _troubleshoot_hdmi_display:

        Debug HDMI display
        =========================

          You can do the following to debug your HDMI display:

          - Upgrade Lontium firmware
          - View DSI clock information
    
        **Upgrade Lontium firmware**

        LT9611uxc is the DSI-to-HDMI bridge chip firmware. The recommended firmware version is ``LT9611UXC_DSI_PortA_HDCP_Disable_V5.0.21.bin``. If you experience a no-display screen on the HDMI, upgrade the firmware.

        To upgrade the Lontium firmware, do the following:

        #. Download the recommended LT9611uxc firmware version ``LT9611UXC_DSI_PortA_HDCP_Disable_V5.0.21.bin`` from the `Lontium <http://www.lontiumsemi.com/download>`__ website and go to the Qualcomm section.

            .. note:: 
                
                - Enable SSH to access your host device. For more information, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                - When prompted for a password, enter ``oelinux123``.
    
        #. To upgrade the firmware, run the following Linux shell command:

            .. container:: nohighlight

              .. code::

                mount -o rw,remount /usr 


            .. note:: Close SSH and copy the Lontium firmware using the following ``scp`` command:

            .. container:: nohighlight

              .. code::

                scp <LT firmware bin> root@<IP of the device>:/lib/firmware/lt9611uxc_fw.bin

            .. note:: Before running the following command, enable SSH again. 

            .. container:: nohighlight

              .. code::

                sync

            .. container:: nohighlight

              .. code::

                echo 0 > /sys/bus/i2c/devices/0-002b/lt9611uxc_firmware

            .. note:: Wait for at least 3 minutes for the firmware upgrade to complete.


        #. To retrieve the lt9611 logs, run the following command:


            .. container:: nohighlight

              .. code::

                dmesg | grep lt9611

        The ``Firmware updates successfully`` log confirms that the firmware upgrade is successful. To ensure that the new firmware is in effect, hard reboot (unplug and plug in the power cable) the device.

        **View DSI clock information**

        .. note:: 

                - You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                - To mount the ``debugfs`` file system to access the ``debugfs`` details of the display subsystem, run the following commands:

                    .. container:: nohighlight

                      .. code::

                        mount -o remount,rw /


                    .. container:: nohighlight

                      .. code::

                        mount -t debugfs none /sys/kernel/debug


        To check the DSI clock information, run the following command:

            .. raw:: latex
    
                \scriptsize
            
            .. container:: nohighlight

              .. code::

                cat /sys/kernel/debug/clk/disp_cc_mdss_pclk0_clk/clk_rate


   .. group-tab:: IQ-9075

        .. class:: tabincludedirective

            .. _debug_displayport:

            Debug DisplayPort
            =========================
        
                .. note:: 
                
                    - You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                    - To mount the ``debugfs`` file system to access the ``debugfs`` details of the display subsystem, run the following commands:

                        .. container:: nohighlight

                          .. code::

                            mount -o remount,rw /


                        .. container:: nohighlight

                          .. code::

                            mount -t debugfs none /sys/kernel/debug

                    
            **View DisplayPort information**

            To check the selected DisplayPort, run the following command:
      
            .. container:: nohighlight

              .. code::

                cat /sys/kernel/debug/dri/0/DP-1/dp_debug 


            **Sample output**

            .. container:: nohighlight

              .. code::

                name = msm_dp
                drm_dp_link
                        rate = 270000
                        num_lanes = 4
                        capabilities = 1
                dp_panel_info:
                        active = 3840x2160
                        back_porch = 80x23
                        front_porch = 48x3
                        sync_width = 32x5
                        active_low = 0x0
                        h_skew = 0
                        refresh rate = 30
                        pixel clock khz = 262750
                        bpp = 30
                dp_link:
                        test_requested = 512
                        num_lanes = 4
                        bw_code = 10
                        lclk = 270000000
                        v_level = 1
                        p_level = 0
                                        

            **View status of DisplayPort cable**

            To verify the DisplayPort connection, run the following command:
            
            .. container:: nohighlight

              .. code::

                cat  /sys/class/drm/card0-DP-1/status


            **Sample output**

            .. container:: nohighlight

              .. code::

                Connected


            **Check EDID mode**

            To check for the EDID mode of the DisplayPort connected, run the following command:

            .. container:: nohighlight

              .. code::

                cat  /sys/class/drm/card0-DP-1/modes

            **Sample output**

            .. container:: nohighlight

              .. code::

                3840x2160
                2048x1080
                1920x1080
                1280x720



   .. group-tab:: IQ-8275

      .. class:: tabincludedirective


          Debug DisplayPort
          ==========================
    
            .. note:: 
            
                - You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                - To mount the ``debugfs`` file system to access the ``debugfs`` details of the display subsystem, run the following commands:

                    .. container:: nohighlight

                      .. code::

                        mount -o remount,rw /


                    .. container:: nohighlight

                      .. code::

                        mount -t debugfs none /sys/kernel/debug

                    

            **View DisplayPort information**

            To check the selected DisplayPort, run the following command:

            
            .. container:: nohighlight

              .. code::

                cat /sys/kernel/debug/dri/0/DP-1/dp_debug 


            **Sample output**

            .. container:: nohighlight

              .. code::

                name = msm_dp
                drm_dp_link
                        rate = 270000
                        num_lanes = 4
                        capabilities = 1
                dp_panel_info:
                        active = 3840x2160
                        back_porch = 80x23
                        front_porch = 48x3
                        sync_width = 32x5
                        active_low = 0x0
                        h_skew = 0
                        refresh rate = 30
                        pixel clock khz = 262750
                        bpp = 30
                dp_link:
                        test_requested = 512
                        num_lanes = 4
                        bw_code = 10
                        lclk = 270000000
                        v_level = 1
                        p_level = 0
                                        

            **View status of DisplayPort cable**

            To verify whether the DisplayPort cable is connected, run the following command:

            
            .. container:: nohighlight

              .. code::

                cat  /sys/class/drm/card0-DP-1/status


            **Sample output**

            .. container:: nohighlight

              .. code::

                Connected


            **Check EDID mode**

            To check for the EDID mode of the DisplayPort connected, run the following command:

            .. container:: nohighlight

              .. code::

                cat  /sys/class/drm/card0-DP-1/modes

            **Sample output**

            .. container:: nohighlight

              .. code::

                  3840x2160
                  2048x1080
                  1920x1080
                  1280x720

.. _enable_x11:

Enable the XWayland compositor
================================

XWayland is a compatibility layer that allows X11 applications to run in a Wayland environment. It translates X11 protocol requests into Wayland-compatible operations.

  Run the following commands to enable XWayland for the display subsystem:

  .. note:: 
    
    You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

  .. container:: nohighlight

      .. code::

        systemctl stop init_display.service


  .. container:: nohighlight

      .. code::

        export XDG_RUNTIME_DIR=/dev/socket/weston && mkdir -p $XDG_RUNTIME_DIR && weston --continue-without-input --idle-time=0 --backend=drm-backend.so --xwayland

    .. note:: If the XWayland compositor fails to launch, restart the device and run the commands again.

    Upon running the commands, you should see the following Weston flower pattern on the display monitor.

    .. image:: ../../media/qli-display/Weston_flower_pattern.PNG
        :align: center
    .. centered:: **Figure: Weston flower pattern**


.. _debug_user_mode_weston:

Set up Weston launch and relaunch Weston
========================================

Do the following to configure Weston launch and manually relaunch Weston. 

**Configure Weston**

  The ``/etc/initscripts/init_qti_display`` script file includes the Weston configurations.

  .. note:: You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.


  .. container:: nohighlight

    .. code::

      mount -o remount,rw /


  .. container:: nohighlight

    .. code::

      cat /etc/initscripts/init_qti_display


.. _relaunch_weston:

**Relaunch Weston**

To manually relaunch the Weston server after closing the Weston process, do the following:

.. note:: You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

1. To identify the ID of the Weston processes, run the following
   commands:

   .. container:: nohighlight

    .. code::

          mount -o remount,rw /


    .. container:: nohighlight

      .. code::

          ps -A | grep weston


      Sample output:

    .. container:: nohighlight

      .. code::

          824 ?        00:00:12 weston
            1090 ?        00:00:00 weston-keyboard
            1092 ?        00:00:01 weston-desktop-

2. To kill the Weston process, run the following command:

   .. note:: You can skip the following command if the modetest application is already running. 

   .. container:: nohighlight

      .. code::

        killall weston

3. To relaunch the Weston server, run the following commands:

   .. container:: nohighlight

      .. code::

          mount -o remount,rw /


    .. container:: nohighlight

      .. code::

          systemctl start init_display.service


.. _connect_hdmi_cable_bootup:

Troubleshoot display issue when HDMI/eDP cable is connected after boot   
===========================================================================

Explains the procedure to troubleshoot a no-display screen issue upon connecting the HDMI/eDP cable after the device is powered on.

**Prerequisite**

Create the ``weston.ini`` file and add the following Weston configurations to the file:

      .. container:: nohighlight

          .. code::

              # configuration file for Weston
              [core]
              require-outputs=none

To push the ``weston.ini`` file, do the following:

1. To push the file to the ``/etc/xdg/weston/weston.ini`` path, run the following command:
 
      .. container:: nohighlight

            .. code::
              
                scp <weston.ini> root@<IP of the device>:/etc/xdg/weston/weston.ini

2. Restart the device.
  
  After powering on the device, connect the HDMI/eDP cable to see the Weston flower pattern appear on the monitor.









            

    

      
      


   