import os

import aind_behavior_services.calibration.treadmill as treadmill
import sfn2024_behavior_hw_demo.rig as rig
from aind_behavior_services.calibration.aind_manipulator import (
    AindManipulatorCalibration,
    AindManipulatorCalibrationInput,
    AindManipulatorCalibrationOutput,
    Axis,
    AxisConfiguration,
    ManipulatorPosition,
)


def mock_rig() -> rig.Rig:

    manipulator_calibration = AindManipulatorCalibration(
        output=AindManipulatorCalibrationOutput(),
        input=AindManipulatorCalibrationInput(
            full_step_to_mm=(ManipulatorPosition(x=0.010, y1=0.010, y2=0.010, z=0.010)),
            axis_configuration=[
                AxisConfiguration(axis=Axis.Y1, min_limit=-0.01, max_limit=25),
                AxisConfiguration(axis=Axis.Y2, min_limit=-0.01, max_limit=25),
                AxisConfiguration(axis=Axis.X, min_limit=-0.01, max_limit=25),
                AxisConfiguration(axis=Axis.Z, min_limit=-0.01, max_limit=25),
            ],
            homing_order=[Axis.Y1, Axis.Y2, Axis.X, Axis.Z],
            initial_position=ManipulatorPosition(y1=0, y2=0, x=0, z=0),
        ),
    )

    return rig.Rig(
        rig_name="test_rig",
        harp_lickometer=rig.HarpLickometer(port_name="COM5"),
        harp_treadmill=treadmill.Treadmill(
            port_name="COM8",
            calibration=treadmill.TreadmillCalibration(
                input=treadmill.TreadmillCalibrationInput(),
                output=treadmill.TreadmillCalibrationOutput(
                    wheel_diameter=15,
                    pulses_per_revolution=28800,
                    brake_lookup_calibration=[[0, 0], [1, 65535]],
                ),
            ),
        ),
        manipulator=rig.AindManipulatorDevice(port_name="COM9", calibration=manipulator_calibration),
        screen=rig.Screen(display_index=1),
    )


def main(path_seed: str = "./local/{schema}.json"):
    example_rig = mock_rig()

    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    models = [example_rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
