.. _hdmi_troubleshooting:

Troubleshoot HDMI
====================

   .. note:: This content is only applicable to QCS6490.

   LT9611uxc is the DSI-to-HDMI bridge chip firmware. The recommended firmware version is ``LT9611UXC_DSI_PortA_HDCP_Disable_V5.0.21.bin``. In case you experience a no-display screen on the HDMI, upgrade the firmware.

   **Lontium firmware upgrade**

   The following are the Lontium firmware upgrade steps:

   1. Download the recommended LT9611uxc firmware version
      ``LT9611UXC_DSI_PortA_HDCP_Disable_V5.0.21.bin`` from
      http://www.lontiumsemi.com/download and go to the Qualcomm section.

      .. note:: Enable SSH in Permissive mode to securely access your host device. For more information, see `How to SH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-254/how_to.html#how-to-ssh->`__.

      .. note:: When prompted for a password, enter *oelinux123*.

   2. To upgrade the firmware, run the following Linux shell commands :

      ::

         mount -o rw,remount /


      ::

         scp <LT firmware bin> root@<IP of the device>:/lib/firmware/lt9611uxc_fw.bin

      ::

         sync

      ::

         echo 0 > /sys/bus/i2c/devices/0-002b/lt9611uxc_firmware

      .. note:: Wait for at least three minutes for the firmware upgrade to complete.

   3. To retrieve the lt9611 logs, run the following command :

      ::

         dmesg | grep lt9611

   The following log confirms that the firmware upgrade is successful: ``Firmware updates successfully``

   To ensure that the new firmware is in effect, hard reboot (unplug and plug in the power cable) the device.


   **Known issues**
   
   You might experience a no-display screen on powering on the device or the hot-plug HDMI cable.

   To fetch the UART serial logs, select `UART serial
   console <https://docs.qualcomm.com/bundle/publicresource/topics/80-70017-254/how_to.html#how-to-connect-to-a-uart-shell->`__.
   After obtaining the UART logs, you may encounter one of the two known issues as follows:

   .. list-table:: Table : Workaround for known issues
      :widths: 36 36
      :header-rows: 1

      - 

         - Known issue
         - Workaround
      - 

         -  If the following EDID timeout log error occurs:
            
            .. code:: pre

               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
         - 

            #. Power ON the Dev kit without the HDMI cable.
            #. Insert the HDMI cable (wait for two minutes) only after
               the device is successfully powered ON.
      - 

         -  If the following disconnected and connected logs occur
            continuously:
            
            .. code:: pre

               lt9611uxc 0-002b: [name=HDMI-A-1]:[status=connected]
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: wait for EDID timeout
               lt9611uxc 0-002b: release edid
               lt9611uxc 0-002b: [name=HDMI-A-1]:[status=disconnected]
               lt9611uxc 0-002b: [name=HDMI-A-1]:[status=connected]
               lt9611uxc 0-002b: release edid
               lt9611uxc 0-002b: [name=HDMI-A-1]:[status=disconnected]
               lt9611uxc 0-002b: [name=HDMI-A-1]:[status=connected]
         -  Kill the Weston server and relaunch the Weston server
            manually. For more information, see :ref:`Relaunch Weston <section_mr4_fkl_xbc>`.


