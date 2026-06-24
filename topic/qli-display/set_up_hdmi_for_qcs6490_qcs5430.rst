.. _set_up_hdmi_for_qcs6490_qcs5430:

Set up HDMI display
===================

To view the output of sample applications on your HDMI display, set up HDMI display.

See the appropriate chip product for device-specific information. 

    .. container:: persistenttab-soc

      .. tabs::

          .. group-tab:: QCS6490

            .. class:: tabincludedirective

                   .. figure:: ../../media/qli-display/set_up_HDMI_2_colourchange.svg
                        :align: center
                   .. centered:: **Figure: HDMI setup workflow** 
                  
                  The display subsystem provides the Weston and Wayland compositors, along with
                  ``libdrm`` APIs, which interact with the DPU driver to render the Wayland
                  client applications. Use the sample test applications to evaluate
                  the basic rendering of Wayland applications and to connect to the HDMI
                  display.

                  Prerequisites
                  --------------
                  
                  Ensure that you configure the following settings on the device:

                  1. Set Switch 4 of DIP_SW_0 to OFF.
                  2. Connect the device to the HDMI display.

                  .. figure:: ../../media/qli-display/HDMI_display.PNG
                        :align: center
                  .. centered:: **Figure: DIP switch selection for HDMI**


                  Verify HDMI or eDP display setup
                  -----------------------------

                  To verify the HDMI or embedded DisplayPort (eDP) setup, do the following:
                  
                  1. Connect the display using one of the following options:

                        - HDMI cable
                        - Mini-DisplayPort cable (as applicable)

                  #. Power on the device. Weston starts automatically during boot.

                  #. Verify the display.
                  
                        The following Weston flower pattern displays on the screen, indicating a successful setup:

                              ..  image:: ../../media/qli-display/Weston_flower_pattern.PNG
                                    :align: center
                              .. centered:: 

                        .. note:: 

                              - If you are experiencing a no-display screen issue on HDMI, see :ref:`Debug HDMI display <troubleshoot_hdmi_display>`.
                              - If you connect the HDMI cable after powering on the device, see :ref:`Troubleshoot display issue when HDMI/eDP cable is connected after boot <connect_hdmi_cable_bootup>`.
                  
                        After you have set up the HDMI display, run the following display test applications to verify the display functionality. 

                  
                  .. _run_the_weston_simple_egl_client_application:

                  Run the Weston simple EGL client application
                  --------------------------------------------------

                  Weston simple EGL is a sample test application used to verify the composition and rendering of frames on your HDMI display. To run the application, run the following commands:

                  .. note:: 

                      You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.
                        

                  .. container:: nohighlight

                        .. code::

                              mount -o remount,rw /


                  .. container:: nohighlight

                        .. code::

                              su


                  .. container:: nohighlight

                        .. code::

                              . /etc/profile


                  .. container:: nohighlight

                        .. code::

                              export XDG_RUNTIME_DIR=/dev/socket/weston && mkdir -p $XDG_RUNTIME_DIR 


                  .. container:: nohighlight

                        .. code::

                              cd /usr/bin


                  .. container:: nohighlight

                        .. code::

                              export WAYLAND_DISPLAY=wayland-1 && weston-simple-egl


                  The following figure shows the Weston simple EGL client application running on the display monitor.

                  .. image:: ../../media/qli-display/Weston_simple_EGL_client_application.PNG
                        :align: center
                  .. centered:: 

                  .. note:: To kill the application, select **CTRL + C**.

                  .. _mode_test_binary:

                  Run DRM modetest
                  ---------------------
                  
                  DRM modetest ensures that the DSI and the DPU paths are working effectively. To verify the display driver topology, run the DRM modetest.

                  **Prerequisite**
                  
                  To run the DRM modetest application, first you need to generate the DRM modetest binary. 

                  **Generate the DRM modetest binary**

                  By default, the DRM modetest binary isn't included in the display subsystem. To generate the DRM modetest binary file, do the following:

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                  1.  Ensure that you have the latest software. If you don't, see `Release Notes <https://docs.qualcomm.com/doc/80-70030-300>`__ and `Qualcomm Linux Build Guide <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/introduction.html>`__.

                  #. To generate the binary, go to the workspace <workspace> and run the following commands:
                  

                        .. container:: nohighlight

                          .. code::
                              
                              export SHELL=/bin/bash

                  
                        .. container:: nohighlight

                          .. code::
                  
                              MACHINE=qcs6490-rb3gen2-core-kit DISTRO=qcom-wayland source setup-environment

                  
                        .. container:: nohighlight

                              .. code::
                              
                                bitbake -fc install libdrm


                        The system generates the binary at ``<workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest`` directory.
                  

                  #. To push the modetest binary file to the device, run the following commands:

                        .. container:: nohighlight

                          .. code::
                        
                            mount -o remount,rw /usr
                        
                        .. container:: nohighlight

                          .. code::

                            scp <workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest  root@<IP of the device>:/usr/bin

                        .. note:: If prompted for a password, enter ``oelinux123``.
                        
                        .. To use the DRM modetest application, you must :ref:`Generate the DRM modetest binary <generate_drm_binary>`.

                  **Run DRM modetest application**

                  To run the drm modetest application, do the following:

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                  #. To kill the Weston client application, run the following commands in the device shell:

                        .. container:: nohighlight

                            .. code::

                              mount -o remount,rw /


                        .. container:: nohighlight

                              .. code::

                                    ps -A | grep weston

                        **Sample output:**

                        ::

                              824 ?        00:00:12 weston
                              1090 ?        00:00:00 weston-keyboard
                              1092 ?        00:00:01 weston-desktop-

                        Use the Weston process ID from the sample Weston process list to kill the Weston processes.

                  #. To kill all Weston processes, run the following command:

                        .. container:: nohighlight

                              .. code::

                                    systemctl stop init_display.service


                  #. To change permissions of the modetest application, run the following command:

                        .. container:: nohighlight

                              .. code::

                                    chmod 0777 /usr/bin/modetest

                  #. To view the connector IDs and modes, run the following command:

                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm > /opt/drm_mode.txt

                  #. To verify DRM modes and connector information, pull the ``/opt/drm_mode.txt`` file locally on your host computer. Use the Secure Copy Protocol (SCP) to pull the ``drm_mode.txt`` file from the device to your host computer. For example,


                              .. container:: nohighlight

                                    .. code::

                                          scp -r root@<IP of the device>:/opt/drm_mode.txt <directory path of the host machine>

                                    .. note:: When prompted for a password, enter ``oelinux123``.

                                    The output as shown in the following figure is from the
                                    ``/opt/drm_mode.txt`` file.

                                    .. image:: ../../media/qli-display/Command_prompt_output.png
                                          :align: center
                                    .. centered:: 

                  #. To fetch the connector ID and mode name, use the relevant values from the ``/opt/drm_mode.txt`` file:


                        .. container:: nohighlight

                              .. code::

                                    modetest -c msm_drm -s <Connector id>:<mode name>

                  #. To start the modetest application, run the following sample command using the connector ID and the mode name retrieved from the ``/opt/drm_mode.txt`` file. For example:


                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm -s 32:1920x1080-60

                        .. note:: Start the DRM test application and ignore the warning log: ``Failed to set gamma: Function not implemented``.

                        .. image:: ../../media/qli-display/DRM_mode_test_sample_application_output_screen.PNG
                              :align: center
                        .. centered:: 

                  #. To kill the modetest application, select **CTRL + C**.
                  
                        .. note:: 

                              Ensure that you :ref:`Relaunch Weston <relaunch_weston>`.


            
          .. group-tab:: IQ-9075

            .. class:: tabincludedirective

                  Not applicable.


          .. group-tab:: IQ-8275

            .. class:: tabincludedirective

                  Not applicable.



Set up DisplayPort
=====================

To view the output of sample applications on your DisplayPort, set up the DisplayPort. 

See the appropriate chip product for information about your device.

    .. container:: persistenttab-soc

       .. tabs::

          .. group-tab:: QCS6490

             .. class:: tabincludedirective


                              Not applicable.


          .. group-tab:: IQ-9075

             .. class:: tabincludedirective

                  .. _setup_displayport:

                  .. figure:: ../../media/qli-display/set_up_HDMI_2_lemans_colourchange.svg
                        :align: center
                  .. centered:: **Figure: DisplayPort setup workflow** 


                  The display subsystem provides the Weston and Wayland compositors, along with
                  ``libdrm``, which interact with the DPU driver to render the Wayland
                  client applications. Use the sample test applications to evaluate
                  the basic rendering of the Wayland applications and to connect to the
                  DisplayPort. 


                 Verify the DisplayPort setup
                 ----------------------------
                  
                  To verify the DisplayPort setup, do the following:
                  
                  1. Connect the DisplayPort cable to the eDP0 connector as shown in the following figure.
            
                        .. image:: ../../media/qli-display/Lemans_dip_switch_and_rb8.png
                              :align: center
                        .. centered:: **Figure: DisplayPort setup**  
                        
                  #. Power on the device. Weston launches automatically during boot. 
                     
                  #. Verify the display. 
                  
                      The following Weston flower pattern displays on both DisplayPort screens, indicating successful setup.

                        .. image:: ../../media/qli-display/Weston_flower_pattern.PNG
                              :align: center
                        .. centered:: 

                  .. note:: 
                        
                        If you connect the DisplayPort cable after powering on the device, see :ref:`Troubleshoot display issue when HDMI/eDP cable is connected after boot <connect_hdmi_cable_bootup>`.

                  After you have set up the DisplayPort, run the following display test applications to verify the display functionality.

                 Run the Weston simple EGL client application
                 --------------------------------------------------

                  Weston simple EGL is a sample test application used to verify the composition and rendering of frames on your DisplayPort. To run the application, run the following commands:

                  .. note:: 

                        You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.
                        

                  .. container:: nohighlight

                        .. code::

                              mount -o remount,rw /


                  .. container:: nohighlight

                        .. code::

                              su


                  .. container:: nohighlight

                        .. code::

                              . /etc/profile


                  .. container:: nohighlight

                        .. code::

                              export XDG_RUNTIME_DIR=/dev/socket/weston && mkdir -p $XDG_RUNTIME_DIR 


                  .. container:: nohighlight

                        .. code::

                              cd /usr/bin


                  .. container:: nohighlight

                        .. code::

                              export WAYLAND_DISPLAY=wayland-1 && weston-simple-egl


                  The following figure shows the Weston simple EGL client application running on the display monitor.

                  .. image:: ../../media/qli-display/Weston_simple_EGL_client_application.PNG
                        :align: center
                  .. centered:: 

                  .. note:: To kill the application, select **CTRL + C**.

      
                 Run DRM modetest
                 ---------------------

                  DRM modetest ensures that the DSI and the DPU paths are working effectively. To verify the display driver topology, run the DRM modetest. 

                  **Generate the DRM modetest binary**

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                  By default, the DRM modetest binary isn't included in the display subsystem. To generate the DRM modetest binary file, do the following:

                  1. Ensure that you have the latest software. If you don't, see `Release Notes <https://docs.qualcomm.com/doc/80-70030-300>`__ and `Qualcomm Linux Build Guide <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/introduction.html>`__.

                  #. To generate the binary, go to the workspace <workspace> and run the following commands:
                  
                        .. container:: nohighlight

                          .. code::
                              
                              export SHELL=/bin/bash

                  
                        .. container:: nohighlight

                          .. code::
                  
                              MACHINE=qcs9075-iq-9075-evk DISTRO=qcom-wayland source setup-environment
                  
                        .. container:: nohighlight

                            .. code::
                              
                              bitbake -fc install libdrm


                        The system generates the binary at ``<workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest`` directory.
                  

                  #. To push the modetest binary file to the device, run the following commands:

                        .. container:: nohighlight

                           .. code::
                  
                             mount -o remount,rw /usr
                  
                        .. container:: nohighlight

                          .. code::

                            scp <workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest  root@<IP of the device>:/usr/bin


                     .. note:: If prompted for a password, enter ``oelinux123``.
              
                       ..  To use the DRM modetest application, you must :ref:`Generate the DRM modetest binary file <generate_drm_binary>`.
                  
                  **Run DRM modetest application**

                  To run the DRM modetest application, do the following: 

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                  1. To kill the Weston client application, run the following commands in the device shell:

                        .. container:: nohighlight

                              .. code::

                                    mount -o remount,rw /


                        .. container:: nohighlight

                              .. code::

                                    ps -A | grep weston

                        **Sample output:**

                        ::

                              824 ?        00:00:12 weston
                              1090 ?        00:00:00 weston-keyboard
                              1092 ?        00:00:01 weston-desktop-

                        Use the Weston process ID from the sample Weston process list to kill the Weston processes.

                  #. To kill all Weston processes, run the following command:


                        .. container:: nohighlight

                              .. code::

                                    systemctl stop init_display.service


                  #. To change permissions of the modetest application, run the following command:

                        .. container:: nohighlight

                              .. code::

                                    chmod 0777 /usr/bin/modetest

                  #. To know the connector IDs and modes, run the following command:


                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm > /opt/drm_mode.txt

                  #. To check for DRM modes and connector information, pull the ``/opt/drm_mode.txt`` file locally on your host computer. Use the Secure Copy Protocol (SCP) to pull the ``drm_mode.txt`` file from the device to your host computer. For example,


                              .. container:: nohighlight

                                    .. code::

                                          scp -r root@<IP of the device>:/opt/drm_mode.txt <directory path of the host machine>

                                    .. note:: When prompted for a password, enter ``oelinux123``.

                                    The output as shown in the following figure is from the
                                    ``/opt/drm_mode.txt`` file.

                                    .. image:: ../../media/qli-display/Command_prompt_output.png
                                          :align: center
                                    .. centered:: 

                  #. To fetch the connector ID and mode name, use the relevant values from the ``/opt/drm_mode.txt`` file:


                        .. container:: nohighlight

                              .. code::

                                    modetest -c msm_drm -s <Connector id>:<mode name>

                  #. To start the modetest application, run the following sample command using the connector ID and the mode name retrieved from the ``/opt/drm_mode.txt`` file. For example:


                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm -s 32:1920x1080-60

                        .. note:: Start the DRM modetest application and ignore the warning log: ``Failed to set gamma: Function not implemented``.

                        .. image:: ../../media/qli-display/DRM_mode_test_sample_application_output_screen.PNG
                              :align: center
                        .. centered:: 

                  #. To kill the modetest application, select **CTRL + C**.
                  
                        .. note:: 

                              Ensure that you :ref:`Relaunch Weston <relaunch_weston>`.


          .. group-tab:: IQ-8275

            .. class:: tabincludedirective

        
                  .. figure:: ../../media/qli-display/set_up_HDMI_2_lemans_colourchange.svg
                        :align: center
                  .. centered:: **Figure: DisplayPort setup workflow**  

                  The display subsystem provides the Weston and Wayland compositors, along with
                  ``libdrm``, which interact with the DPU driver to render the Wayland
                  client applications. Use the sample test applications to evaluate
                  the basic rendering of the Wayland applications and to connect to the
                  DisplayPort. 

 

                 Verify DisplayPort setup
                 -------------------------
                  
                  To verify the setup, do the following:

                  1. Connect the DisplayPort cable to the eDP0 connector as shown in the following figure:

                        .. image:: ../../media/qli-display/Monaco_DPU_setup.png
                              :align: center
                        .. centered:: **Figure: IQ-8275 DisplayPort setup**

                  #. Power on the device. Weston launches automatically during boot. 
                     
                  #. Verify the display. 
                  
                     The following Weston flower pattern displays on the screen, indicating a successful setup.

                        .. image:: ../../media/qli-display/Weston_flower_pattern.PNG
                              :align: center
                        .. centered:: 

                        .. note:: 
                              
                              If you connect the DisplayPort cable after powering on the device, see :ref:`Troubleshoot display issue when HDMI/eDP cable is connected after boot <connect_hdmi_cable_bootup>`.


                 After you have set up the DisplayPort, run the following display test applications to verify the display functionality. 


                 Run the Weston simple EGL client application
                 --------------------------------------------------

                   Weston simple EGL is a sample test application that you can use to verify the composition and rendering of frames on the DisplayPort. To run the application, run the following commands:

                  .. note:: 

                        You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.
                        

                  .. container:: nohighlight

                        .. code::

                              mount -o remount,rw /


                  .. container:: nohighlight

                        .. code::

                              su


                  .. container:: nohighlight

                        .. code::

                              . /etc/profile


                  .. container:: nohighlight

                        .. code::

                              export XDG_RUNTIME_DIR=/dev/socket/weston && mkdir -p $XDG_RUNTIME_DIR 


                  .. container:: nohighlight

                        .. code::

                              cd /usr/bin


                  .. container:: nohighlight

                        .. code::

                              export WAYLAND_DISPLAY=wayland-1 && weston-simple-egl


                  The following figure shows the Weston simple EGL client application running on the display monitor.

                  .. image:: ../../media/qli-display/Weston_simple_EGL_client_application.PNG
                        :align: center
                  .. centered:: 

                  .. note:: To kill the application, select **CTRL + C**.

      
                 Run DRM modetest
                 ---------------------
                 
                 DRM modetest ensures that the DSI and the DPU paths are working effectively. To verify the display driver topology, run the DRM modetest. 

                 **Generate the DRM modetest binary**

                  By default, the DRM modetest binary isn't included in the display subsystem. To generate the DRM modetest binary file, do the following:

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.

                  1.  Ensure that you have the latest software. If you don't, see `Release Notes <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-300>`__ and `Qualcomm Linux Build Guide <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/introduction.html>`__.

                  #. To generate the binary, go to the workspace <workspace> and run the following commands:
                  

                        .. container:: nohighlight

                              .. code::
                              
                                    export SHELL=/bin/bash

                  
                        .. container:: nohighlight

                              .. code::
                  
                                    MACHINE=qcs8275-iq-8275-evk DISTRO=qcom-wayland source setup-environment

                  
                        .. container:: nohighlight

                              .. code::
                              
                                    bitbake -fc install libdrm


                        The system generates the binary at ``<workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest`` directory.


                  #. To push the modetest binary file to the device, run the following commands:

                        .. container:: nohighlight

                            .. code::
                        
                              mount -o remount,rw /usr
                  
                        .. container:: nohighlight

                            .. code::

                              scp <workspace>/build-qcom-wayland/tmp-glibc/work/armv8-2a-qcom-linux/libdrm/2.4.120/image/usr/bin/modetest  root@<IP of the device>:/usr/bin

                        .. note:: If prompted for a password, enter ``oelinux123``.
                                          
                        .. To use the DRM modetest application, you must :ref:`Generate DRM modetest binary file <generate_drm_binary>`.
                   
                  **Run DRM modetest**

                  To run the DRM modetest application, do the following:

                  .. note::

                       You must enable SSH to access your host device. For instructions, see `Sign in using SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-254/how_to.html#use-ssh>`__.


                  1. To kill the Weston client application, run the following commands in the device shell:

                        .. container:: nohighlight

                              .. code::

                                    mount -o remount,rw /


                        .. container:: nohighlight

                              .. code::

                                    ps -A | grep weston

                        **Sample output:**

                        ::

                              824 ?        00:00:12 weston
                              1090 ?        00:00:00 weston-keyboard
                              1092 ?        00:00:01 weston-desktop-

                        Use the Weston process ID from the sample Weston process list to kill the Weston processes.

                  #. To kill all Weston processes, run the following command:


                        .. container:: nohighlight

                              .. code::

                                    systemctl stop init_display.service


                  #. To change permissions of the modetest application, run the following command:

                        .. container:: nohighlight

                              .. code::

                                    chmod 0777 /usr/bin/modetest

                  #. To know the connector IDs and modes, run the following command:


                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm > /opt/drm_mode.txt

                  #. To check for DRM modes and connector information, pull the ``/opt/drm_mode.txt`` file locally on your host computer. Use the Secure Copy Protocol (SCP) to pull the ``drm_mode.txt`` file from the device to your host computer. For example,


                              .. container:: nohighlight

                                    .. code::

                                          scp -r root@<IP of the device>:/opt/drm_mode.txt <directory path of the host machine>

                                    .. note:: When prompted for a password, enter ``oelinux123``.

                                    The output as shown in the following figure is from the
                                    ``/opt/drm_mode.txt`` file.

                                    .. image:: ../../media/qli-display/Command_prompt_output.png
                                          :align: center
                                    .. centered:: 

                  #. To fetch the connector ID and mode name, use the relevant values from the ``/opt/drm_mode.txt`` file:


                        .. container:: nohighlight

                              .. code::

                                    modetest -c msm_drm -s <Connector id>:<mode name>

                  #. To start the modetest application, run the following sample command using the connector ID and the mode name retrieved from the ``/opt/drm_mode.txt`` file. For example:


                        .. container:: nohighlight

                              .. code::

                                    /usr/bin/modetest -c msm_drm -s 32:1920x1080-60

                        .. note:: Start the DRM test application and ignore the warning log: ``Failed to set gamma: Function not implemented``.

                        .. image:: ../../media/qli-display/DRM_mode_test_sample_application_output_screen.PNG
                              :align: center
                        .. centered:: 

                  #. To kill the modetest application, select **CTRL + C**.
                  
                        .. note:: 

                              Ensure that you :ref:`Relaunch Weston <relaunch_weston>`.


            ..      Run GStreamer video playback applications
            ..      --------------------------------------------------

            ..       To run the GStreamer sample applications, you must ensure that the DisplayPort setup is verified. For information on prerequisites, see `Sample applications <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-50/example-applications.html>`__.

            ..       To run the sample video test cases using ``gst-launch-1-0``, see `With video playback as an example <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-50/video-playback-use-cases.html>`__.

            ..       .. note:: 
                        
            ..             Before running the test cases, ensure that you meet the `prerequisites <https://docs.qualcomm.com/bundle/publicresource/topics/80-70030-50/gstreamer-application-use-cases.html>`__.




                     



     
   










