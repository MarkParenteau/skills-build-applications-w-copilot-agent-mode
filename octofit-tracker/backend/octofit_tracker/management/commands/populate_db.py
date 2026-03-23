from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data

        # Use raw collection deletion for reliability with Djongo
        # Use pymongo to clear all relevant collections directly
        from django.conf import settings
        import pymongo
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client[settings.DATABASES['default']['NAME']]
        db['octofit_tracker_user'].delete_many({})
        db['octofit_tracker_team'].delete_many({})
        db['octofit_tracker_activity'].delete_many({})
        db['octofit_tracker_leaderboard'].delete_many({})
        db['octofit_tracker_workout'].delete_many({})

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users (Superheroes)


        users = [
            {'email': 'tony@marvel.com', 'username': 'IronMan', 'team_name': 'Marvel'},
            {'email': 'steve@marvel.com', 'username': 'CaptainAmerica', 'team_name': 'Marvel'},
            {'email': 'bruce@marvel.com', 'username': 'Hulk', 'team_name': 'Marvel'},
            {'email': 'clark@dc.com', 'username': 'Superman', 'team_name': 'DC'},
            {'email': 'bruce@dc.com', 'username': 'Batman', 'team_name': 'DC'},
            {'email': 'diana@dc.com', 'username': 'WonderWoman', 'team_name': 'DC'},
        ]
        user_objs = []
        for u in users:
            user = User.objects.create_user(email=u['email'], username=u['username'], password='password', team_name=u['team_name'])
            user_objs.append(user)

        # Create Activities
        for user in user_objs:
            app_models.Activity.objects.create(username=user.username, type='run', duration=30)
            app_models.Activity.objects.create(username=user.username, type='cycle', duration=45)

        # Create Workouts
        for user in user_objs:
            app_models.Workout.objects.create(username=user.username, name='Morning Cardio', description='Cardio session', duration=40)

        # Create Leaderboard
        for team_name in ['Marvel', 'DC']:
            app_models.Leaderboard.objects.create(team_name=team_name, score=100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
