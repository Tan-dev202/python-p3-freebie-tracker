#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()
session.commit()

moringa = Company(name="Moringa", founding_year=2014)
safaricom = Company(name="Safaricom", founding_year=1997)
britam = Company(name="Britam", founding_year=1965)
microsoft = Company(name="Microsoft", founding_year=1975)

session.add_all([moringa, safaricom, britam, microsoft])
session.commit()

anne = Dev(name="Anne")
frank = Dev(name="Frank")
andrew = Dev(name="Andrew")
thomas = Dev(name="Thomas")

session.add_all([anne, frank, andrew, thomas])
session.commit()

freebies = [
    Freebie(dev_id=anne.id, company_id=moringa.id, item_name="Diary", value=300),
    Freebie(dev_id=anne.id, company_id=safaricom.id, item_name="Mug", value=100),
    Freebie(dev_id=frank.id, company_id=moringa.id, item_name="Umbrella", value=500),
    Freebie(dev_id=frank.id, company_id=britam.id, item_name="Notebook", value=300),
    Freebie(dev_id=andrew.id, company_id=microsoft.id, item_name="Hood", value=500),
    Freebie(dev_id=thomas.id, company_id=britam.id, item_name="Bag", value=1000),
    Freebie(dev_id=thomas.id, company_id=moringa.id, item_name="Phone", value=20000)
]
session.add_all(freebies)
session.commit()
session.close()
