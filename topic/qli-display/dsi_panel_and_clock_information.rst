.. _dsi_panel_and_clock_information:

Panel and clock information
===========================


   .. note:: You must enable SSH in Permissive mode to securely access your host device. For instructions, see `How to SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-254/how_to.html#use-ssh->`__.

   .. note:: Ensure that you mount the ``debugfs`` file system to access the ``debugfs`` details of the display subsystem. To mount the ``debugfs`` file system, use the following commands:

               ::

                  mount -o remount,rw /

               ::

                  mount -t debugfs none /sys/kernel/debug

.. tabs::

   .. tab:: QCS6490

            The DSI panel and clock information can be obtained as follows:

            **Check the selected display panel**

            To check which panel was selected, run the following command:

            ::

               cat /sys/kernel/debug/qcom,mdss_dsi_ext_bridge_rb3gen2/dump_info

            **Sample output**:

            ::

               name = qcom,mdss_dsi_ext_bridge_rb3gen2
                                 Resolution = 1920(148|88|44|1)x1080(36|4|5|1)@60fps 0 Hz
                                 CTRL_0:
                                       ctrl = dsi-ctrl-0
                                       phy = dsi-phy-0
                                 Panel = ext video mode dsi bridge
                                 Clock master = dsi-ctrl-0    

            **Check DSI clock information**

            To check the DSI clock information, run the following command:

            ::

               cat /sys/kernel/debug/qcom,mdss_dsi_ext_bridge_rb3gen2/dsi-ctrl-0/state_info

            Sample output:

            ::

                  Current State:
                        CTRL_ENGINE = ON
                        VIDEO_ENGINE = ON
                        COMMAND_ENGINE = OFF
                  Clock Info:
                        BYTE_CLK = 111375000, PIXEL_CLK = 148500000, ESC_CLK = 19200000


   .. tab:: IQ-9075

      The DisplayPort panel and clock information can be obtained as follows:

 
      **Check which panel was selected**

      To check which panel was selected, run the following command:

      ::

         cat  /sys/kernel/debug/dri/0/msm_dp-DP-1/dp_debug 

      Sample output:

      ::

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

      **Check status of DisplayPort cable**

      To check if the DisplayPort cable is connected, run the following command:

      ::

         cat  /sys/class/drm/card0-DP-1/status

      Sample output:

      ``connected``

      **Check EDID mode**

      To check the EDID mode of the DisplayPort panel connected, run the following command:

      ::

         cat  /sys/class/drm/card0-DP-1/modes

      Sample output:

      ::

         3840x2160
         2048x1080
         1920x1080
         1280x720



