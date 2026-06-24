.. _displayport_panel_and_clock_information:

DisplayPort panel and clock information for IQ-9075
===================================================

The subsequent sections provide information on the panel selected and
the DisplayPort clock information.

.. note:: You must enable SSH in Permissive mode to securely access your host device. For instructions, see `How to SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70014-254/how_to.html#how-to-ssh->`__.

Ensure that you mount the ``debugfs`` file system to access the
``debugfs`` details of the display subsystem. 
To mount the ``debugfs`` file system, use the following commands:

::

   mount -o remount,rw /

::

   mount -t debugfs none /sys/kernel/debug

.. _section_pfq_qjg_rzb_mneogi_12-06-23-1116-20-385:

Check which panel was selected
------------------------------

To check which panel was selected, run the following command:

::

   cat  /sys/kernel/debug/dri/0/msm_dp-DP-1/dp_debug 

**Sample output:**

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

.. _section_stg_dlg_rzb_mneogi_12-06-23-1127-39-456:

Check status of DisplayPort cable
---------------------------------

To check if the DisplayPort cable is connected, run the following
command:

::

   cat  /sys/class/drm/card0-DP-1/status

**Sample output:** 

``connected``

.. _section_wgz_kb1_mcc:

Check EDID mode
---------------

To check the EDID mode of the DisplayPort panel connected, run the
following command:

::

   cat  /sys/class/drm/card0-DP-1/modes

**Sample output:**

::

   3840x2160
   2048x1080
   1920x1080
   1280x720


