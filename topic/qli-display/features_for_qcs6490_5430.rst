.. _features_for_qcs6490_5430:

Display features
******************

See the appropriate chip product for device-specific information. 

.. container:: persistenttab-soc

   .. tabs::

      .. group-tab:: QCS6490

         
         **Key features**

         The display subsystem supports the following key features:

         -  Wayland and Weston with upstream aligned protocol
         -  Weston with direct rendering manager (DRM) backend module
         -  Weston remote desktop protocol (RDP) backend
         -  DSI interface
         -  Native eDP 1.4 interface 
         -  Type-C over DisplayPort

         **Capabilities**

         The device supports two displays simultaneously and offers various configurations for maximum concurrency. The following table summarizes the capabilities.

         .. list-table:: Table: Interfaces and capabilities
            :class: longtable table-wrap
            :align: center
  
            - 
           
               - **Interface**
               - **Capabilities**
               
            - 
               - DSI0
               - 

                | FHD+ (1200 × 2520) at 120 fps (8-bit)
                | Supports Video Electronics Standards Association (VESA) display stream compression (DSC) 1.2
            - 

               - DSI0 to HDMI
               - 

                 | Supports up to 3840 × 2160 at 30 fps
                 | Supports dynamic resolution switch up to  3840 × 2160 at 30 fps
                 
            - 

               - DisplayPort
               - 
                  
                 | 3840 × 2160 resolution at 30 fps, 24 bpp (requires two lanes at HBR3)
                 | Single stream transport
      
            - 

               - eDP
               - Supports a maximum resolution of 3840 × 2160 at 60 fps

            -

              - Maximum concurrency
              - 

                | HD+ (1200 × 2520) (8‑bit) at 60 fps with DSI primary + 4K at 30 fps DisplayPort

                Or

                | 1920 × 1080p at 60 fps with DSI to HDMI primary + 4K at 30 fps DisplayPort

                Or

                | 1920 × 1080p at 60 fps with eDP primary + 4K at 30 fps DisplayPort 
                    


         **Advanced features**

         The display subsystem enhances the visual performance and
         efficiency of the device. A key feature of the display subsystem is to
         provide improved picture quality with HDR10 support for internal
         display. This feature is available to licensed developers with authorized access.


      .. group-tab:: IQ-9075

         **Key features**

            The display subsystem supports the following key features:

            -  Wayland and Weston with upstream protocol
            -  Weston compositor with direct rendering manager (DRM) backend module
            -  DSI interface
            -  2xDisplayPort with single stream transport (SST) and 2xDisplayPort with multi-stream transport (MST)
            -  Dual DPU support for extended ports
                 
         **Capabilities**

            The device supports two displays simultaneously and offers various configurations for maximum concurrency. The following table summarizes the capabilities.

             .. list-table:: Interfaces and capabilities
               :class: longtable table-wrap
               :align: center
              
               - 
              
                  - **Interface**
                  - **Capabilities**
               -  

                  - DSI0
                  -

                    | Supports 1280 × 720 with reference RPi panel
                    | Supports Video Electronics Standards Association (VESA) display stream compression (DSC) 1.2

               -

                  - eDP0
                  - Supports 3840 × 2160 at 60 fps 30 bpp
                      
               -
                  - eDP1
                  - Supports 3840 × 2160 at 60 fps 30 bpp

               -

                  - Maximum concurrency
                  - Supports 3840 × 2160 at 60 fps 30 bpp with DP0 as Primary + 3840 × 2160 at 60 fps 30 bpp with DP1 as Secondary
                     
                     .. note:: Software supports maximum concurrency (only 4 streams supported between DSI, eDP0, and eDP1 including multi-stream transport (MST)).

                     
      .. group-tab:: IQ-8275

         **Key features**

            The display subsystem supports the following key features:

            -  Wayland and Weston with upstream protocol
            -  Weston compositor with direct rendering manager (DRM) backend module
            -  DSI interface
            -  2xDisplayPort with single stream transport (SST)
                  

         **Capabilities**

           The following table summarizes the capabilities.

           .. list-table:: Capabilities and configurations
               :class: longtable table-wrap
               :align: center
              
               -  
              
                  - **Interface**
                  - **Capabilities**
                  
               - 

                  - DSI0
                  -

                    | Supports 1280 × 720 with reference RPi panel
                    | Supports Video Electronics Standards Association (VESA) display stream compression (DSC) 1.2
                   
               -

                  - eDP0
                  - Supports 3840 × 2160 at 60 fps 30 bpp
                      
               -

                  - eDP1
                  - Supports 3840 × 2160 at 60 fps 30 bpp



Next steps
***************

- :ref:`Troubleshoot display <toubleshoot_display>`







