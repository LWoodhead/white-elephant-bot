from .action import Action
from .game import Game
from .actionRecord import ActionRecord
from .player import Player

class StealAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int, stealer: Player, 
           stolenFrom: Player) -> ActionRecord:
        stealerGift = stealer.get_game_gift()
        stolenFromGift = stolenFrom.get_game_gift()
        stealer.set_game_gift(stolenFromGift)
        stolenFrom.set_game_gift(stealerGift)
        if(stolenFromGift != None):
            stolenFromGift.steal()
        data = { "type" : "steal", "stealer" : stealer, "stolenFrom" : stolenFrom}    
        steal_record = ActionRecord(actionId,data)
        return steal_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        stealer = record.data['stealer']
        stolenFrom = record.data['stolenFrom']
        stealerGift = stealer.get_game_gift()
        stolenFromGift = stolenFrom.get_game_gift()
        if(stealerGift != None):
            stealerGift.release()
        stealer.set_game_gift(stolenFromGift)
        stolenFrom.set_game_gift(stealerGift)