#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/freebies.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    companies = session.query(Company).all()
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()
    
    print("-----Testing Freebie Tracker-----")
    
    print(f"Total Companies: {len(companies)}")
    print(f"Total Devs: {len(devs)}")
    print(f"Total Freebies: {len(freebies)}")
    
    print(f"\nFirst company: {companies[0].name}")
    print(f"    First company's freebies: {[freebie.item_name for freebie in companies[0].freebies]}")
    print(f"    First company's devs: {[dev.name for dev in companies[0].devs]}")
        
    print(f"\nFirst dev: {devs[0].name}")
    print(f"    First dev's freebies: {[freebie.item_name for freebie in devs[0].freebies]}")
    print(f"    First dev's companies: {[company.name for company in devs[0].companies]}")
        
    print(f"\nFirst freebie details: {freebies[0].print_details()}")
        
    print(f"\nOldest company: {Company.oldest_company(session).name} (founded {Company.oldest_company(session).founding_year})")
    print(f"Does {devs[0].name} have a Diary? {devs[0].received_one('Diary')}")
    print(f"Does {devs[0].name} have a Umbrella? {devs[0].received_one('Umbrella')}")
    

    moringa = session.query(Company).filter_by(name="Moringa").first()
    anne = session.query(Dev).filter_by(name="Anne").first()
    
    print(f"\nGive freebie: {moringa.name} giving 'Notebook' to {anne.name}")
    print(f"    Anne's freebies before: {[freebie.item_name for freebie in anne.freebies]}")
    
    new_freebie = moringa.give_freebie(anne, "Water Bottle", 300, session)
    
    session.refresh(anne)
    print(f"    Anne's freebies after: {[freebie.item_name for freebie in anne.freebies]}")
    print(f"    New freebie added: {new_freebie.print_details()}")
    session.commit()
    

    andrew = session.query(Dev).filter_by(name="Andrew").first()
    frank = session.query(Dev).filter_by(name="Frank").first()
    
    andrew_freebie = session.query(Freebie).filter_by(dev_id=andrew.id).first()
    
    print(f"\nGive Away: {andrew.name} giving '{andrew_freebie.item_name}' to {frank.name}")
    print(f"    Andrew's freebies before: {[freebie.item_name for freebie in andrew.freebies]}")
    print(f"    Frank's freebies before: {[freebie.item_name for freebie in frank.freebies]}")
    print(f"    Freebie owner before: {andrew_freebie.dev.name}")
    
    result = andrew.give_away(frank, andrew_freebie, session)
    
    session.refresh(andrew)
    session.refresh(frank) 
    session.refresh(andrew_freebie)
    
    print(f"\n  Andrew's freebies after: {[freebie.item_name for freebie in andrew.freebies]}")
    print(f"    frank's freebies after: {[freebie.item_name for freebie in frank.freebies]}")
    print(f"    Freebie new owner: {andrew_freebie.dev.name}")
    session.commit()
    
    import ipdb; ipdb.set_trace()
