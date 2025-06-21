from random import randint, choice as rc
from faker import Faker
from models import db, Recipe, User
from config import app
from sqlalchemy import inspect

fake = Faker()

def seed_database():
    with app.app_context():
        print("Deleting all records...")
        
        # Create inspector to check for tables
        inspector = inspect(db.engine)
        
        # Check if tables exist before trying to delete
        if 'recipes' in inspector.get_table_names():
            db.session.query(Recipe).delete()
        if 'users' in inspector.get_table_names():
            db.session.query(User).delete()
        db.session.commit()

        print("Creating users...")
        users = []
        usernames = set()

        for i in range(20):
            username = fake.first_name().lower()
            while username in usernames:
                username = fake.first_name().lower()
            usernames.add(username)

            user = User(
                username=username,
                bio=fake.paragraph(nb_sentences=3),
                image_url=fake.image_url(),
            )
            user.password_hash = f"{username}password"
            users.append(user)

        db.session.add_all(users)
        db.session.commit()

        print("Creating recipes...")
        recipes = []
        for i in range(100):
            instructions = fake.paragraph(nb_sentences=8)
            while len(instructions) < 50:
                instructions += " " + fake.paragraph(nb_sentences=2)
            
            recipe = Recipe(
                title=fake.sentence(),
                instructions=instructions,
                minutes_to_complete=randint(15, 90),
                user_id=rc(users).id
            )
            recipes.append(recipe)

        db.session.add_all(recipes)
        db.session.commit()
        print("Seeding complete!")

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        seed_database()