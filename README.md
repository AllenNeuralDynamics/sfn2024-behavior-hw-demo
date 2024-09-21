# sfn2024-behavior-hw-demo
A repository for demos of hardware used by the behavior team


## Getting started


1. Install Bonsai by running `./bonsai/setup.cmd`
2. If you are not creating a settings file, skip to 3. Else:
    - Create a python environment using `./pyproject.toml`
    - Create your settings `.json` file with the rig configuration. An example can be found in `./examples/examples.json`
3. Use the created settings file (e.g. `./examples/rig.json`) as an input to the Bonsai workflow. You can launch the demo by running:
    - `"./bonsai/bonsai.exe" "./src/demo.bonsai" -p RigPath="../examples/rig.json" --start`

4. The user interfaces can be accessed by double-clicking the `ControlUserInterface` and `AindManipulatorGui` at the bottom of the workflow canvas.
