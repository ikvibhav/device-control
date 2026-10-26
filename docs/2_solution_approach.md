## Solution Approach

### Part 1: Setup

Implemented classes:
1. `Vector2D`: Coordinate the base coordintae system
2. `PositioningUnit`: Manages PU movement and MD position
3. `MeasuringDevice`: Simulates measurements with calibration
4. `Wafer`: Manages wafer geometry and coordinate transforms
5. `CalibrationStation`: Reference location
6. `DeviceController`: Orchestrator of the executions

### Part 2: Execution

1. **Calibration** (Step 1)
   - Move PU to calibration station
   - Measure actual MD offset
   - Store calibration offset for future corrections

2. **Wafer Position Determination** (Step 2)
   - Measure center mark position
   - Measure left mark position (2 shots left)
   - Calculate rotation angle using vector between marks
   - Calculate actual wafer center in PU_CS

3. **Center Mark Measurement** (Step 3)
   - Move MD to center mark
   - Perform 2D measurement

4. **Offset Mark Measurement** (Step 4)
   - Move MD to mark (2 up, 1 right from center)
   - Perform 2D measurement