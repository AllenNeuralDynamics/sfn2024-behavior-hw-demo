# Import core types
from __future__ import annotations

# Import core types
from typing import Literal, Optional

import aind_behavior_services.rig as rig
from aind_behavior_services.calibration import aind_manipulator
from aind_behavior_services.calibration.treadmill import Treadmill
from aind_behavior_services.rig import (
    AindBehaviorRigModel,
    HarpLickometer,
    Screen,
)
from pydantic import BaseModel, Field

__version__ = "0.0.0"


class AindManipulatorAdditionalSettings(BaseModel):
    """Additional settings for the manipulator device"""

    spout_axis: aind_manipulator.Axis = Field(default=aind_manipulator.Axis.Y1, description="Spout axis")


class AindManipulatorDevice(aind_manipulator.AindManipulatorDevice):
    """Overrides the default settings for the manipulator device by spec'ing additional_settings field"""

    additional_settings: AindManipulatorAdditionalSettings = Field(
        default=AindManipulatorAdditionalSettings(), description="Additional settings"
    )


class Rig(AindBehaviorRigModel):
    version: Literal[__version__] = __version__
    harp_lickometer: Optional[HarpLickometer] = Field(..., description="Harp lickometer")
    harp_treadmill: Treadmill = Field(..., description="Harp treadmill")
    manipulator: AindManipulatorDevice = Field(..., description="Manipulator")
    screen: rig.Screen = Field(default=Screen(), description="Screen settings")
