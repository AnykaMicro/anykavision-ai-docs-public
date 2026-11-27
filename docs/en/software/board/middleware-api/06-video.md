# Video

&emsp;&emsp;Video-processing modules primarily include video input (VI), the video processing subsystem (VPSS), video encoding (VENC), video decoding (VDEC), and video output (VO).

```{admonition} TODO
:class: warning

This documentation does not include API descriptions for the video decoding (VDEC) or video output (VO) modules. Anyka still needs to confirm whether the KM02G series supports these two modules.
```

&emsp;&emsp;The main processing flow is shown in Figure 6-1:

![Figure 6-1 Video-processing flow](../../../../zh_CN/software/board/middleware-api/img/video-processing-flow.png)

<br/>

​        Before running video samples, including the VI and VPSS samples, load the capture-related drivers: ak_vi.ko, sensor_xxx.ko, ak_vicap.ko, ak_isp.ko, and ak_pp.ko. This is normally done by running a script. For a GC5603 CIS, refer to gc5603.sh; the commands are:

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        For other CIS devices, refer to the corresponding xxx.sh loading script.

​        The VENC and video samples also require the encoding drivers ak_venc_adapter.ko and ak_venc_bridge.ko. Load them with:

​        insmod /usr/modules/ak_venc_adapter.ko

​        insmod /usr/modules/ak_venc_bridge.ko

​        When running a video sample, its parameters must specify the full path to the ispconf file for the corresponding CIS; otherwise, the sample cannot run.
