from server.repositories.teams import TeamsRepository


class TeamsService:
    def __init__(self, teams_repository: TeamsRepository):
        self._teams_repository = teams_repository

    def get_all_teams(self):
        return self._teams_repository.get_all()
