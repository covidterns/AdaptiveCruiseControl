# AdaptiveCruiseControl

**Main Idea:** Create a basic adaptive cruise control that will work in most cars with light modification.

**Implementation Description:** Implement an ACC system that reads in data from a camera and identifies and tracks cars using OpenCV. It then tracks only the nearest car in the current lane and activates the cruise control to either increase or decrease speed to maintain a specified distance away from the car as well as keeping speed upper bounded by a user defined value.

**Constraints** 
- Should only require a lower power device (No Alienware PC sitting in the trunk...) such as a Raspberry Pi or likewise device.
- Should not impede driver inputs in any way.
- Must be used in conjunction with driver input.

**Potential Problems**
- Car width unknown (how far do we want to keep the car in front of us).
- Motorcycles? (maybe just don't use it around them / deactivate if detected).

**Possible Technologies used / learning experience**
- IOT (maybe we use in conjunction with other sensors, more for exposure)
- OpenCV
- Car detection can use tons of different tools and styles, can use multiple AI/ML strategies (insert fancy keyword here)
- Python (probably, but an implementation detail)
- Linux (Raspbian, others...)
- Some wiring

**Initial Inputs**
- Camera

**Possible Future Inputs**
- LIDAR
- RADAR
- Multi Camera

**Initial Outputs**
- Cruise Control increase speed
- Cruise Control decrease speed

**Possible Future Outputs**
- Communication through CAN Bus
- Cruise Control activation?
- Cruise Control deactivation?
