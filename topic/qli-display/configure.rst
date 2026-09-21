

Configure
############

.. container:: persistenttab-soc

  .. tabs::

      .. group-tab:: QCS6490

        .. class:: tabincludedirective


         Qualcomm Linux display supports the third-party DSI-to-HDMI bridge chip
         extensions. The basic configurations required to integrate the bridge
         chips are explained as follows:

         .. image:: ../../media/qli-display/Reference_bridge_chip_configuration2.png
            :align: center
         .. centered:: **Figure : Bridge chip configuration**

         .. _section_cl5_rcb_p1c_mneogi_02-29-24-1319-33-720:

         Configure reference bridge chip 
         ================================

         The LT9611uxc DSI-to-HDMI bridge chip is used in the reference platform. For
         more information on the LT9611uxc DSI-to-HDMI bridge chip, see the
         Lontium semiconductor datasheet.
            
         To use the reference DSI-to-HDMI bridge chip, see the `.dtsi <https://git.codelinaro.org/clo/le/platform/vendor/opensource/display-devicetree/-/blob/display-kernel.qclinux.1.0.r2-rel/display/dsi-panel-ext-bridge-1080p.dtsi?ref_type=heads>`__ file.

         The following table lists the configurations that are required to integrate bridge chips.

            .. list-table::  Table : Configurations for bridge chip integration
               :header-rows: 1
               :class: longtable table-wrap
               :align: center

               - 

                  - Description
                  - DTSI node
               - 

                  - Set the DSI-to-HDMI bridge panel as Primary
                  - 
                 
                     .. container:: nohighlight

                        .. code::
                        
                           &sde_dsi {
                           qcom,dsi-default-panel = <&dsi_ext_bridge_1080p>;
               - 

                  - Configure reference power supply entries for the bridge chip
                  - 
                  
                     .. container:: nohighlight

                        .. code::

                           &sde_dsi {
                           vddio-supply = <&vreg_l8c_1p62>;
                           vdda-0p9-supply = <&vreg_l10c_0p88>;
                           vdda-0p9-supply = <&vreg_l10c_0p88>;
               - 

                  - Configure panel reset GPIOs for the bridge chip
                  - 
                  
                     .. container:: nohighlight

                        .. code::
                           
                           lt9611: lt,lt9611@2b { 
                           reset-gpios = <&pm7250b_gpios 2 0>;
               - 

                  -  Configure the DSI host driver in the external bridge mode to
                     work with the third-party DSI-to-HDMI bridge chip
                  - 
                  
                     .. container:: nohighlight

                        .. code::

                           qcom,mdss-dsi-ext-bridge-mode;


         Set up custom splash logo in UEFI
         ===================================

         Setting up the custom splash logo in UEFI is available to licensed developers with authorized access. For more information, see **Configure** in
         `Qualcomm Linux Display Guide -
         Addendum <https://docs.qualcomm.com/bundle/resource/topics/80-70033-18A/configure.html>`__.



      .. group-tab:: IQ-9075

         Not applicable.


      .. group-tab:: IQ-9075

         Not applicable.





                  


