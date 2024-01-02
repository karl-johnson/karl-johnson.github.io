---
date: 2023-07-01
description: Yonder Dynamics - Spectrometer
thumbnail: yonder-thumb.jpg
layout: markup-project
draft: true
---
# yonder raman spectrometer

Motivation: description of science mission, tests we decided to go with
- After lots of research, science team came back with 4 tests
    - Raman
    - DAPI
    - Nilered
    - pH
- We realized we could do pH optically, so we went with a testing platform that was entirely optical

Raman testing:
- Most difficult test is Raman
- Lessons learned from optical bench testing
    - Use as high power laser as possible
    - Use microscope objective - much better collection efficiency
    - Filtering is super key, used razor blade with prism to test this

Design for on-rover:
- Started with a raman design and tacked other features on
    - [key elements of raman design]
- Re-use green laser for nilered
- DAPI UV excitation from below
    - In order to see this, need notch and not LPF
- White excitation behind cuvette
- Can't do all at the same time, must rotate cuvettes in and out of optical path
- Everything by itself is simple, should be easy, right?
requirements, how we satisfied them

Main problems that arose:
- green lasers break a lot
    - Went through 10
    - How they broke: Over voltage on power supply, overheated, broke pins when extracting, just die when using anything except a lipo
- angular spectrum of filters
- adjustment of fiber alignment
- 

How did it work at competition?
- Up late the night before handling other issues
- Barely had any time to test module, never did a proper full run-through
- On the day of, carousel jammed
This is what you get for trying something too complex with single points of failure!