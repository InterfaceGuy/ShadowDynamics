import importlib
import pydeation.imports
importlib.reload(pydeation.imports)
from pydeation.imports import *
from MolochConsciousness.MolochConsciousness import MolochConsciousness


class MagnetizedGrid(CustomObject):

    def __init__(self, input_object, **kwargs):
        self.input_object = input_object
        super().__init__(**kwargs)

    def specify_parts(self):
        self.target_null = Null(name="Target")
        self.target_effector = TargetEffector(target=self.target_null)
        self.cloner = Cloner(clones=self.input_object, mode="honeycomb", effectors=[self.target_effector])

        self.parts += [self.cloner, self.target_effector, self.target_null]

class ShadowDynamics(ThreeDScene):

    def construct(self):

        moloch_consciousness = MolochConsciousness(creation=True)
        magnetized_grid = MagnetizedGrid(input_object=moloch_consciousness)

        self.play(Create(moloch_consciousness), run_time=3)


if __name__ == "__main__":
    shadow_dynamics = ShadowDynamics()