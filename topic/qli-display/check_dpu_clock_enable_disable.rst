.. _check_dpu_clock_enable_disable:

General DPU debugging information
=================================

The common DPU debugging information to identify and troubleshoot errors is helpful when you encounter such problems in your deployment.

.. _section_ncy_cxg_rzb_mneogi_12-06-23-1258-57-313:

DPU clock rate
--------------

.. note:: You must enable SSH in Permissive mode to securely access your host device. For instructions, see `How to SSH <https://docs.qualcomm.com/bundle/publicresource/topics/80-70014-254/how_to.html#how-to-ssh->`__.

To check the DPU clock rate, run the following command:

::

   cat /sys/kernel/debug/clk/clk_summary | grep disp_cc

.. _section_ydx_gxg_rzb_mneogi_12-06-23-1300-6-978:

Set DPU to the Performance mode
-------------------------------

To set the DPU to the Performance mode, run the following commands:

::

   cd /sys/kernel/debug/dri/0/debug/core_perf/

::

   echo 1 > perf_mode


