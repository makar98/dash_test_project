from application.data_generation.data_generation import ArtificialDataGenerator
from application.models import Well, Data
from application import db
import random


def generate(n_well: int, wellnames: list, user_id: int):
    well_list = []
    for index, well_data in enumerate(ArtificialDataGenerator().gen_data(n_well)):
        if wellnames is not None:
            if n_well != len(wellnames):
                for n in range(n_well - len(wellnames)):
                    wellnames.append(random.randint(0, 1000))
        else:
            wellnames = []
            for i in range(n_well):
                wellnames.append((random.randint(0, 1000)))

        well = Well(name=wellnames[index], user_id=user_id)
        db.session.add(well)
        for dot in well_data:
            d = Data(well_id=well.id,
                     min=dot['min'],
                     gas=dot['gas'],
                     oil=dot['oil'],
                     water=dot['water']
                     )
            db.session.add(d)
            db.session.flush()
        well_list.append(well)
    db.session.commit()
    return well_list

# generate(2, [1, 2])