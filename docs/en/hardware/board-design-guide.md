# Product Board Design Guide

## About This Document

The AI camera-glasses product board uses KM02G-series and AK1090-series controller chips. Using the AI-glasses main board as an example, this document describes design considerations for each functional unit of those chips.

```{note}
This page is textual hardware guidance. Schematic and layout design files were not included in this release, and the guidance has not been validated on a physical board for this documentation release.
```

## KM02G-Series Module Circuit Design

### Clock-Generation Circuit

The KM02G 24 MHz clock-generation circuit supplies the chip's operating clock. See the chip Specification for the detailed system-clock relationships.

#### 24 MHz Crystal Circuit

Figure 2-1 shows the 24 MHz crystal circuit for a crystal with load capacitance CL = 10 pF.

![24 MHz crystal circuit](../../zh_CN/hardware/img/design-24mhz-crystal.png)

Figure 2-1 24 MHz crystal circuit

**Crystal-selection considerations:**

- The 24 MHz crystal frequency error must not exceed ±20 ppm.
- The recommended maximum ESR is 50 Ω; match CL to 10 pF. Calculate load capacitance with `CL = C1*C2 / (C1+C2) + CS`, then select capacitors according to the crystal's CL.
- The maximum drive level must not exceed 100 µW. Otherwise add an external RD resistor to limit current and prevent crystal damage.

#### AVDD18_ANA

AVDD18_ANA uses a 1.8 V supply for the audio module and 24 MHz crystal circuit. It may share the VDDIO18 supply. Isolate the two supply pins with a ferrite bead or 0 Ω resistor.

### System Reset

The KM02G `#RESET` pin controls system reset. Pulling it low resets every module except RTC to its predefined reset state. If the system becomes abnormal, use `#RESET` or the internal watchdog to restart it.

Three reset methods are supported: hardware reset, watchdog reset, and system software reset.

Figure 2-2 shows the power-on RC hardware-reset circuit.

![Power-on RC hardware-reset circuit](../../zh_CN/hardware/img/design-power-on-reset.png)

Figure 2-2 Power-on RC hardware-reset circuit

### System-Module Supply Pins

#### VDD0P8

VDD0P8 is the KM02G core supply. For lower power consumption at the typical `CPU_CLK=800MHz` and `DDR3_CLK=900MHz` configuration, use a DC-DC supply producing 0.8 V and feed VDD0P8 through a ferrite bead. If ambient temperature is below the Specification range or operating frequency exceeds these typical values, increase the core voltage to 0.85 V. For good transient response, provide a decoupling capacitor at every pin where possible.

**Note:** The DC-DC output must support at least 2 A.

#### AVDD0P8_DPLL / AVDD0P8_CPLL

These pins have strict voltage requirements and may share the VDD0P8 supply. Add a ferrite bead or 0 Ω resistor between VDD0P8 and AVDD0P8_DPLL/AVDD0P8_CPLL. At each pin, provide one small and one large capacitor; 100 nF plus 4.7 µF or 10 µF is recommended.

**Note:** Do not use an inductor or another component with a large voltage drop.

#### VDD1P35_DDR / VDD1P35_DDRCK

These pins supply the on-chip memory. For optimal operation and lower power, use a DC-DC supply producing 1.35 V and feed the DDR pins through a ferrite bead. Provide a decoupling capacitor at each pin for better transient response.

**Note:** The DC-DC output must support at least 1 A.

### Power-Up Sequence and Supply Description

Use the power-up sequence in Figure 2-3.

![Power-up reset sequence](../../zh_CN/hardware/img/design-power-up-sequence.png)

Figure 2-3 Power-up reset sequence

Timing:

1. 0 ms ≤ T0 ≤ 2 ms
2. 0 ms ≤ T1 ≤ 20 ms
3. 0 ms ≤ T2 ≤ 5 ms
4. Typical T3 is 10 ms

Provide a decoupling capacitor for every supply pin. Place it close to the pin and route the supply through the capacitor before the chip pin. Table 2-1 lists the supply pins and voltage ranges.

Table 2-1 KM02G supply pins

| **No.** | **Name** | **Description** | **Voltage range (V)** | **Type** | **Requirement** |
| ------: | -------- | --------------- | --------------------- | -------- | --------------- |
| 1 | VDD0P8 | Core supply | 0.72-0.88 | Input | Required |
| 2 | AVDD_CPLL | PLL supply | 0.72-0.88 | Input | Required |
| 3 | AVDD_DPLL | | 0.72-0.88 | Input | Required |
| 4 | VDD1P35_DDR | Memory supply | 1.283-1.45 | Input | Required |
| 5 | VDD1P35_DDRCK | | 1.283-1.45 | Input | Required |
| 6 | VDDIO33 | I/O supply | 2.97-3.63 | Input | Required |
| 7 | VDDIO18 | | 1.62-1.98 | Input | Required |
| 8 | VDDIO33_SFC | SFC I/O supply | 2.97-3.63 | Input | Required |
| 9 | VDDIO18_SFC | | 1.62-1.98 | Input | Required |
| 10 | AVDD33_USB | USB supply | 2.97-3.63 | Input | Required |
| 11 | AVDD18_USB | | 1.62-1.98 | Input | Required |
| 12 | VDDIO18_MIPI | MIPI-interface supply | 1.62-1.98 | Input | Required |
| 13 | VDDIO18_CSI | CSI-interface supply | 1.62-1.98 | Input | Required |
| 14 | AVDD18_ANA | Audio supply | 1.62-1.98 | Input | Required |
| 15 | VR1P6 | 1.6 V reference | 1.6 | Output | Required |
| 16 | VCM | 0.8 V reference | 0.8 | Output | Required |

**KM02G power-on/off consideration:**

- When KM02G is powered off and sleeping, drive connected peripheral pins low to prevent back-powering KM02G and disrupting its power-on reset.

### Analog Module

#### Analog-Circuit Supply Pins

The analog supplies are VDDIO18_MIPI, VCM, VR1P6, and AVDD18_ANA.

1. VDDIO18_MIPI supplies the analog section and has a strict ripple requirement. Keep it away from noise sources and isolate it with a ferrite bead.
2. VCM is the 0.8 V analog reference and requires an external 10 µF capacitor.
3. VR1P6 is the 1.6 V analog supply and requires an external 4.7 µF or 10 µF capacitor. It may bias the microphone circuit.
4. See the AVDD18_ANA section above for that supply.

#### Audio Interfaces

KM02G supports microphone and headphone functions.

##### MIC

1. Use VR1P6 for an analog microphone. Connect analog-microphone ground to the KM02G ePAD at a single PCB point and provide ground guards along MIC_P and MIC_N, as shown in Figure 2-4.

![Analog microphone circuit](../../zh_CN/hardware/img/design-analog-mic.png)

Figure 2-4 Analog microphone circuit

2. Digital microphones use the PDM interface, which supports up to four inputs, as shown in Figure 2-5.

![Digital microphone circuit](../../zh_CN/hardware/img/design-digital-mic.png)

Figure 2-5 Digital microphone circuit

**Notes:**

1. The analog microphone supports differential input only, not single-ended input.
2. The PDM interface supports four digital microphones. Audio ADC cannot be used in that configuration. Every microphone uses the same sample rate and interface frequency.
3. Recommended microphone specifications:
   - SNR ≥ 58 dB; SNR ≥ 62 dB is preferred.
   - Sensitivity: -32 dB to -38 dB.
   - Use an omnidirectional microphone.
4. Mechanical design considerations:
   - Provide a separate acoustic chamber. Both 6 mm and 4 mm microphones require an external vibration-damping rubber sleeve. A thicker sleeve generally improves isolation; 1.5 mm wall thickness is sufficient. Design the chamber accordingly.
   - Point the microphone away from the speaker where possible; a perpendicular arrangement is also possible. Choose angle and distance to minimize acoustic coupling.

##### HPOUT

HPOUT is the audio output. Add a PA when driving a speaker and use an I/O pin to switch the PA enable, as in Figure 2-6.

![PA-control circuit](../../zh_CN/hardware/img/design-pa-control.png)

Figure 2-6 PA-control circuit

Check the selected GPIO's default level. If it defaults high, modify the PA-enable circuit to prevent a pop at power-on.

**PA selection:**

1. Output power must meet the design requirement.
2. Consider the THD+N curve. At 70% rated output, 0.5% distortion is generally adequate and 0.15% gives optimal results.

**Speaker selection:**

1. SPL must be at least 89 dB; for better local audio use at least 90 dB. Higher SPL means higher sensitivity.
2. The driver fundamental resonance `f0` must be below 1 kHz. The acoustic chamber shifts `f0` upward, so about 600 Hz is recommended. Above 1 kHz, the response should be as flat as possible without impulsive peaks.
3. Recommended sensitivity: 95 dB/1 W/0.1 m.
4. Recommended rated impedance: 8 Ω, measured at 1 kHz and 1 W.
5. At 1 W with `f0` below 1 kHz, distortion should be below 10%. If measured results are acceptable, cost considerations may justify relaxing this requirement. A speaker with an integrated acoustic chamber is recommended.

#### SAR ADC Interface

KM02G provides three SAR ADC inputs: AIN0, AIN1, and AIN2. Their reference is the precise internal AVDD18_ANA 1.8 V supply.

Add a filter capacitor to every AIN signal for accurate sampling; 10 nF or 100 nF is recommended.

### SFC/SPI

KM02G provides one SFC interface and two SPI interfaces, SPI0 and SPI1.

#### SFC

SFC is the boot interface and supports up to 100 MHz. With Flash it supports one-line and four-line bidirectional modes as shown in Figure 2-7. Four-line mode is recommended for higher throughput.

Design considerations:

1. SFC supports controller mode only, not peripheral mode.
2. SFC supports Flash hardware reset, so connect SFC_HOLD to the Flash chip.
3. Use SFC only for program-boot Flash.
4. Connect the two SFC data lines according to the MOSI/MISO relationship.
5. Above 25 MHz, consider termination to preserve signal integrity.
6. With dual Flash, the system boots SFC_CS0 first by default.

![SFC Flash one-line and four-line modes](../../zh_CN/hardware/img/design-sfc-flash-modes.png)

Figure 2-7 SFC Flash one-line and four-line modes

#### SPI0 and SPI1

SPI0 and SPI1 are general-purpose SPI interfaces:

1. Both support controller and peripheral modes.
2. Their pins are multiplexed with other functions; use pins as adjacent groups in pin-list order.

### Camera

#### MIPI Interface

The camera interface provides one MIPI interface supporting cameras up to 13 MP and up to four data lanes. Figure 2-8 shows the signals.

![MIPI interface](../../zh_CN/hardware/img/design-mipi-interface.png)

Figure 2-8 MIPI interface

**Notes:**

1. Up to four data lanes and one clock lane are supported.
2. Software can configure a differential pair as data or clock; for example, MIPI_RX_L0P/N may be either.
3. Polarity may be swapped within a differential pair; MIPI_RX_L0P and MIPI_RX_L0N can exchange positive/negative roles.
4. Isolate the traces from high-interference devices to prevent image noise.
5. Control differential impedance to 100 Ω within ±10%. Use controlled impedance and length matching, with ground guards for data and clock. Because MIPI is fast, a four-layer board is recommended to preserve ground continuity.
6. Do not use unused MIPI pins as GPIOs.

#### External CIS Considerations

AI camera glasses normally use an FPC CIS module. For image quality:

1. Use an LDO for the CIS analog supply. If a DC-DC supplies the CIS core to reduce power, keep ripple and noise within the CIS requirements.
2. For a long FPC, place bulk and decoupling capacitors near the CIS connector and account for FPC voltage drop.
3. Set supply voltage and current exactly as required by the CIS manufacturer. Incorrect voltage, ripple, or noise can cause horizontal bands or image noise.

### USB Interface

KM02G provides one USB 2.0 interface supporting Device and Host modes. Reserve it for program download. If other devices are connected for debugging, provide resistors that can disconnect them to avoid USB communication errors during download.

The schematic only needs correct DP/DM ordering. Add ESD protection when the product has an ESD-rating requirement.

**ESD component selection:**

1. Parasitic capacitance on USB_DM and USB_DP must be below 3 pF.
2. To improve ESD immunity, ground the connector shell through a ferrite bead or small inductor, or add a common-mode choke in series with USB_DM/USB_DP.

### I2C

KM02G supports four I2C interfaces:

1. I2C supports controller mode only.
2. Use adjacent pin combinations.
3. External pull-ups should be 4.7-10 kΩ.

### MMC/SDIO/SD

KM02G provides three MMC/SDIO/SD interfaces supporting MMC 4.2, SDIO 2.0, and SD 2.0.

1. Only SD0 supports MMC, in one-bit and four-bit modes.
2. Every SD interface supports SD and SDIO protocols in one-bit and four-bit modes.
3. Where SD is pin-multiplexed, use an adjacent pin group.
4. SD0 is recommended for an external SD NAND.

#### SD NAND

SD NAND supports one-bit and four-bit modes.

1. SD_CMD and SD_D0-D3 need no external pull-ups; the chip provides internal pull-ups.
2. SD NAND quality varies. Control its power through software; Figure 2-10 shows the circuit.

![SD NAND one-bit and four-bit modes](../../zh_CN/hardware/img/design-sd-nand-modes.png)

Figure 2-9 SD NAND one-bit and four-bit modes

![SD NAND power-control circuit](../../zh_CN/hardware/img/design-sd-nand-power-control.png)

Figure 2-10 SD NAND power-control circuit

#### SDIO

The KM02G SDIO Wi-Fi interface supports one-bit and four-bit modes.

![SDIO reference circuit](../../zh_CN/hardware/img/design-sdio.png)

Figure 2-11 SDIO reference circuit

1. If the connected chip pins have internal pull-ups, the SDIO data-line pull-ups may be omitted.
2. In one-bit mode, retain SDIO_D1 for the interrupt and do not omit its pull-up.
3. Check internal pull-up/pull-down configuration when choosing SDIO pins.

### UART

KM02G provides multiple UARTs at up to 6 Mbit/s.

1. UART0 is the default debug port; do not use it for another purpose.
2. UART1 is the default AK1090 communication port; do not use it for another purpose.

### GPIO

Fifteen KM02G I/Os support software-configurable high- or low-level wake: GPIO[2], GPIO[6], GPIO[8], GPIO[18], GPIO[20], GPIO[22], GPIO[24], GPIO[26], GPIO[28], GPIO[32:33], GPIO[36], GPIO[38], AIN0, and USB_DP.

## AK1090-Series Module Circuit Design

### Lithium-Battery Charging

AK1090 provides lithium-battery charge management. VIN is the external charge input and VBAT connects to the battery. Add an external lithium-battery protection device as in Figure 3-1.

![Lithium-battery protection circuit](../../zh_CN/hardware/img/design-battery-protection.png)

Figure 3-1 Lithium-battery protection circuit

The charger built into one AK1090 supports at most 200 mA. Decide whether to add an external charger according to the required charging time.

VIN is also a single-wire communication interface. Isolate it from the input supply with a diode as in Figure 3-2.

![Charge/single-wire communication reference circuit](../../zh_CN/hardware/img/design-charge-single-wire.png)

Figure 3-2 Charge/single-wire communication reference circuit

**Note:** Single-wire communication requires no VBUS input and C123 to have finished discharging.

### Digital Microphones

AK1090 supports two PDM digital-microphone inputs for stereo.

![Stereo DMIC reference circuit](../../zh_CN/hardware/img/design-stereo-dmic.png)

Figure 3-3 Stereo DMIC reference circuit

### UART

AK1090 provides one UART used as the debug port and multiplexed with other functions.

### GPIO

AK1090 has 14 I/Os. IO17, IO18, IO19, and IO20 use 1.8 V; the others use 3.3 V.

### KM02G Power Control and Communication

1. For AK1090 control of KM02G camera-module power, use a soft-start switch. C19 and R20 set the timing to reduce the power-on voltage dip. Dual PMOS devices Q4 and Q5 reduce on-resistance, as shown in Figure 3-4.

![Soft-start reference circuit](../../zh_CN/hardware/img/design-soft-start.png)

Figure 3-4 Soft-start reference circuit

2. AK1090/KM02G communication-UART considerations:

   1. Cross-connect RXD and TXD. A series resistor no greater than 100 Ω may be used for EMI optimization.
   2. While KM02G is powered off and sleeping, drive the AK1090-connected UART pins low to prevent back-powering KM02G and disrupting its power-on reset.

## Wi-Fi Module Design Considerations

The product board uses a dual-band 2.4/5.8 GHz ATBM Wi-Fi chip.

1. Supply Wi-Fi and other high-current devices directly from the battery or input supply; do not share a supply with CPU, DDR, or analog circuitry.
2. Wi-Fi has strict power requirements; a dedicated DC-DC regulator is recommended.
3. Length-match the SDIO bus between Wi-Fi and KM02G on the PCB.

## External Gyroscope Considerations

The platform uses gyroscope data to correct image deformation and recording shake.

1. The analog supply range is 1.71-3.6 V, and the device has an internal LDO. Use low-impedance power routing at least 15 mil wide to prevent voltage drop. At both supply input and chip supply pins, place a 100 nF ceramic capacitor in parallel with a 1 µF tantalum capacitor to filter high- and low-frequency noise and stabilize zero offset across voltages.
2. With I2C, use 4.7-10 kΩ external pull-ups.
3. Device-selection requirements:

   1. Range: ±2000 dps
   2. Output data rate: ≥800 Hz
   3. ADC resolution: 16 bits
   4. Operating temperature: -40 °C to +85 °C
   5. Sensitivity: ±1%
   6. Sensitivity temperature coefficient: ±0.05%/°C

4. CIS-module installation:

   1. Observe the specified CIS installation and horizontal orientation.

      ![CIS module](../../zh_CN/hardware/img/design-cis-module.png)

      Figure 2-13 CIS module

   2. The gyroscope Y axis must be perpendicular to the product's horizontal plane. Its XOY plane must be parallel to the CIS target plane.

````{only} anyka_review
```{admonition} Pending source figure
:class: warning

The figure was removed because it came from a third party. Anyka must redraw it.
```

Figure 2-14 Gyroscope-axis orientation
````

   3. Keep the temperature-sensitive gyroscope away from heat sources.

## PCB Design Guide

### Main-Chip Peripheral-Circuit PCB Design

#### Power

##### DC-DC

External DC-DC circuits supply VDD0P8 (core), VDD1P35_DDR/VDD1P35_DDRCK (memory), and VDDIO33/VDDIO18 (I/O). Follow these layout and routing recommendations:

1. Keep input and output loops short and traces at least 20 mil wide.
2. Route the input through its decoupling capacitor before the chip pin.
3. Route the output through its filter capacitor before the load.
4. Keep feedback routing short.
5. Place the power inductor close to and on the same layer as the DC-DC IC.
6. Provide an adjacent, continuous ground plane for the module to improve ripple performance.

![3.3 V DC-DC circuit](../../zh_CN/hardware/img/design-dcdc-3v3.png)

Figure 2-1 3.3 V DC-DC circuit

![DC-DC layout and routing](../../zh_CN/hardware/img/design-dcdc-layout.png)

Figure 2-2 DC-DC layout and routing

##### Supply Pins

1. Every AK chip supply pin requires a decoupling capacitor as close as possible to the pin. Route the supply through the capacitor to the pin and keep capacitor and chip on the same layer where possible. Figures 2-3 through 2-5 show examples.
2. Connect the AVDD_PLL decoupling capacitor to main ground at one point where possible, do not share surface-layer ground with other components, and keep it away from high-frequency signals.
3. Keep the trace from the DC-DC output to VDD0P8 as short as possible and at least 20 mil wide.

![Chip supply-pin decoupling capacitor](../../zh_CN/hardware/img/design-power-decoupling.png)

Figure 2-3 Chip supply-pin decoupling capacitor

![CORE supply decoupling layout and routing](../../zh_CN/hardware/img/design-core-decoupling-layout.png)

Figure 2-4 CORE supply decoupling layout and routing

![DDR supply decoupling layout and routing](../../zh_CN/hardware/img/design-ddr-decoupling-layout.png)

Figure 2-5 DDR supply decoupling layout and routing

#### USB Differential Traces

USB is a high-speed differential link with good interference rejection. The AK chip supports USB 2.0 at up to 480 Mbit/s, so route it as a transmission line rather than an ordinary data signal.

##### Impedance Control

Trace width and spacing, copper thickness, dielectric constant and thickness, and proximity to ground/power planes all affect impedance. Account for them in design and tell the PCB manufacturer where controlled differential pairs are located.

Figure 2-6 shows a cross-section of a ground-guarded differential pair on a two-layer board. W1-W2 and G1-G2 are the differential traces; the outer sections are ground guards.

USB differential impedance must be 90 Ω within ±10%. For an ordinary two-layer board thicker than 0.6 mm, trace width 0.2 mm (`W1=0.2mm`), pair spacing 0.1 mm, and ground-guard spacing 0.1 mm (`D1=S1=0.1mm`) meet the requirement. Alternatively calculate impedance with Si9000 and route from its results.

![Two-layer PCB stack-up for a ground-guarded differential pair](../../zh_CN/hardware/img/design-usb-stackup.png)

Figure 2-6 Two-layer PCB stack-up for a ground-guarded differential pair

Additional considerations:

1. Do not add ferrite beads, capacitors, or other filters to the differential pair; they seriously disturb impedance.
2. Keep a continuous ground plane below the pair to avoid impedance discontinuity and noise susceptibility.
3. Avoid vias. If unavoidable, change layers no more than twice and use small vias.
4. Keep pair spacing constant.

##### Layout

Route USB pairs in parallel, length-matched, and with few vias:

1. Place the AK chip close to the USB connector and place ESD devices close to the connector.
2. Plan USB and other differential pairs first. Put the USB signal layer adjacent to ground. Ground-guard USB_DM/USB_DP and provide the shortest return path. Keep the underlying ground plane continuous where space permits. Keep other signals, especially fast-edge digital signals, at least 150 mil away.
3. Use 45° or curved bends, not 90° bends. Keep the pair short and length-matched; add serpentine length to the shorter trace if needed. Put test points directly on the pair to avoid stubs. Figure 2-7 is not recommended; Figure 2-8 is recommended.

![USB routing with an unrecommended stub](../../zh_CN/hardware/img/design-usb-stub-avoid.png)

Figure 2-7 Unrecommended stub routing

![Recommended USB routing](../../zh_CN/hardware/img/design-usb-stub-recommended.png)

Figure 2-8 Recommended routing

#### SPI Flash

Place the SFC SPI Flash close to the AK chip. Keep data and clock traces short, ground-guard the entire clock trace, length-match high-speed SFC signals, and preserve impedance continuity.

#### Crystal

1. Place the crystal and load capacitors close to the AK chip. Connect ground pins directly to main ground and avoid sharing nearby surface ground.
2. Keep traces short.
3. Provide a ground plane below the crystal and keep other signals away.
4. Ground-guard the crystal traces.

![Crystal layout](../../zh_CN/hardware/img/design-crystal-layout.png)

Figure 2-9 Crystal layout

#### Microphone

The microphone receives small signals and is susceptible to interference:

1. Place microphone components close to the controller, as in Figures 2-10 and 2-11.
2. Ground-guard microphone traces and connect them directly to the corresponding chip pins. Keep guard-ground returns away from high-power-device return paths.
3. Do not place fast-switching signals or high-power components such as PA and Wi-Fi on the opposite side below the microphone circuit.

![Microphone routing](../../zh_CN/hardware/img/design-mic-routing.png)

Figure 2-10 Microphone routing

![Microphone application circuit](../../zh_CN/hardware/img/design-mic-circuit.png)

Figure 2-11 Microphone application circuit

#### Camera Interface

##### MIPI Routing

Control impedance and match length. A four-layer board is recommended for ground continuity at MIPI speeds.

###### Impedance Control

MIPI differential impedance must be 100 Ω within ±10%. Using the Figure 2-6 two-layer 1.6 mm board and Si9000 results, example combinations are:

- `W2/G2=6.0mil`, `D1=4mil`, `T=1OZ`, `H1=58mil`, `Er=4.3`: 100.92 Ω.
- `W2/G2=8.2mil`, `D1=5mil`, `T=1OZ`, `H1=58mil`, `Er=4.3`: 103.55 Ω.
- `W2/G2=12mil`, `D1=6mil`, `T=1OZ`, `H1=58mil`, `Er=4.3`: 101.96 Ω.

###### Layout

1. Provide a reference plane below MIPI signals, preferably a continuous ground plane. If that is impossible, the plane must extend at least 4W beyond each side of each trace, where W is trace width.

````{only} anyka_review
2. Length- and spacing-match MIPI pairs to prevent receive errors. Within a pair, mismatch must be less than 10 mil; between pairs, mismatch must be less than 100 mil. Keep serpentine sections separated by four times the trace width.

```{admonition} Pending source figure
:class: warning

The length-matching figure was removed because it came from a third party. Anyka must redraw it.
```

Figure 2-12 MIPI length-matching example

```{admonition} Pending source figure
:class: warning

The serpentine-spacing figure was removed because it came from a third party. Anyka must redraw it.
```

Figure 2-13 Serpentine-trace spacing example
````

````{only} not anyka_review
2. Length- and spacing-match MIPI pairs to prevent receive errors. Within a pair, mismatch must be less than 10 mil; between pairs, mismatch must be less than 100 mil. Keep serpentine sections separated by four times the trace width.
````

3. Space MIPI pairs by more than twice the trace width. Keep MIPI at least three trace widths from other high-speed signals such as parallel buses and clocks, do not route them in parallel, and keep them away from switching regulators.
4. Avoid vias. If vias are required, place them symmetrically on both traces and add corresponding reference-plane transition vias when changing layers.

##### Interface-Capacitor Layout

Because the glasses normally use an FPC CIS module, place interface decoupling capacitors as close to the connector as possible.

![Interface-decoupling layout example](../../zh_CN/hardware/img/design-interface-decoupling.png)

Figure 2-14 Interface-decoupling layout example

### External Wi-Fi Device Design

Place the input pin of the Wi-Fi DC-DC close to the input supply. If mechanical constraints prevent this, make the trace from supply to input pin wider than 20 mil. Place the DC-DC output close to the Wi-Fi supply pin and use at least 20 mil trace width.

### External Gyroscope Design

1. Keep this mixed-signal sensor at least 200 mil from regulators, high-frequency oscillators, and other interference sources. Separate high-power devices such as DC-DC converters into another PCB region and consider a grounded guard band to keep switching noise from reducing accelerometer/gyroscope accuracy.
2. The analog supply range is 1.71-3.6 V and an LDO is built in. Use low-impedance power traces at least 15 mil wide. Place 100 nF ceramic and 1 µF tantalum capacitors in parallel at the supply input and chip supply pin for composite high-/low-frequency filtering and stable zero offset.
3. Keep I2C/SPI traces short and straight, no longer than 1200 mil. Match critical SPI clock/data lengths within ±5 mil. Add 22-47 Ω series matching resistors to I2C SDA/SCL and follow the 3W spacing rule to reduce reflection and crosstalk.
4. Do not route INT1/INT2 parallel to supplies or high-frequency signals. Use ground isolation when crossing is required. Keep interrupt traces short and add pull-downs if necessary to prevent false triggering.

### ESD Design

1. Connect I/O-connector ground pins to main ground nearby and do not route supplies under connector layers.
2. Preserve sufficient ground-pour area around the PCB perimeter for later ESD treatment.
3. Place ESD devices close to interfaces and connect their ground locally to main ground. Route external-connector signals through the ESD device before the protected chip.

## Antenna Design Guide

(review-only-antenna-types)=
### Common Antenna Types and Key Parameters

```{note}
Source material for this section was not included in this release. Maintainers may add it after Anyka completes an original rewrite or confirms third-party authorization.
```

(review-only-antenna-design)=
### Antenna Design Essentials

```{note}
Source material for this section was not included in this release. Maintainers may add it after Anyka completes an original rewrite or confirms third-party authorization.
```

### PCB Design Essentials

```{note}
Source material for this section was not included in this release. Maintainers may add it after Anyka completes an original rewrite or confirms third-party authorization.
```

### Product-Enclosure Effects on the Antenna

An antenna is usually installed inside the product enclosure. Placing it close to plastic lowers its resonant frequency. A larger RF ground plane also lowers resonant frequency and improves the ground plane, reducing return loss. Therefore tune the antenna again with the final enclosure installed to obtain the required band.

1. Keep components, mounting screws, and ground planes away from the antenna tip and the region along its length.
2. Do not route battery or audio wires across the antenna or on the same side of the PCB antenna trace.
3. Do not completely cover the antenna with a metal enclosure or shield.
4. Orient the antenna to maximize radiation in the required final-product direction.
5. Do not place a ground plane directly below any antenna.
6. Leave enough clearance between antenna and ground plane and keep the ground-plane width to a minimum in that region.
