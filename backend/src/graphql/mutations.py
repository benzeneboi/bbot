import graphene
import subprocess
from src import db
from ..graphql.objects import UserObject as User, \
    ConsiderationsObject as Considerations
from ..models import User as UserModel, \
    Consideration as ConsiderationsModel

from .. import globals


class UserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
    
    user = graphene.Field(lambda: User)

    def mutate(self, info, email):
        user = UserModel(email=email)
        db.session.add(user)
        db.session.commit()

        return UserMutation(user=user)


class ConsiderationsMutation(graphene.Mutation):
    """add another entry to current game considerations"""
    """
    mutation {
  mutateConsiderations(team1: "team A", team2: "team B", sport: "NBA", gameDateTime: "2023-02-02T06:54:47",betWindow: "10")
	{
    consideration {
      team1
      team2
      sport
      gameDateTime
      currDateTime
      
    }
  }
}
    """
    class Arguments:
        team_1 = graphene.String()
        team_2 = graphene.String()
        game_date_time = graphene.DateTime()#graphene.String()##String()
        #curr_date_time = graphene.DateTime
        sport = graphene.String()
        bet_window = graphene.String()#Time() # datetime.time(0,10) -> 10mins

    consideration = graphene.Field(lambda: Considerations)

    def mutate(self, info, team_1=None, team_2=None, sport=None, game_date_time=None, curr_date_time=None, bet_window=None):
        consideration = ConsiderationsModel(team_1=team_1, team_2=team_2, sport=sport, game_date_time=game_date_time, curr_date_time=curr_date_time, bet_window=bet_window)
        db.session.add(consideration)
        db.session.commit()

        return ConsiderationsMutation(consideration=consideration)

class StartProgramMutation(graphene.Mutation):
    class Arguments:
        pass
    
    success = graphene.Boolean()
    
    def mutate(self, info, **kwargs):
        if globals.betbot_process is not None:
            return StartProgramMutation(success=True)

        p = subprocess.Popen(["python", "test_worker.py"])
        success = False
        if p.poll() is None:
            globals.update_process(p)
            globals.update_state("running")
            success = True
        return StartProgramMutation(success=success)

class KillProgramMutation(graphene.Mutation):
    class Arguments:
        pass

    killed = graphene.Boolean()

    def mutate(self, info, **kwargs):
        
        if globals.betbot_process.poll() is None:
            globals.betbot_process.kill()
            globals.update_process(None)
            globals.update_state("not running")
        killed = True
        return KillProgramMutation(killed=killed)
    

class Mutation(graphene.ObjectType):
    mutate_user = UserMutation.Field()
    mutate_considerations = ConsiderationsMutation.Field()
    mutate_start_program = StartProgramMutation.Field()
    mutate_kill_program = KillProgramMutation.Field()